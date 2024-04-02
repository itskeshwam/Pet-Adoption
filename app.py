from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pet_adoption_db"
)
cursor = db.cursor()

# Home route with search functionality and pagination
@app.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page
    search = request.form.get('search')
    if search:
        cursor.execute("SELECT * FROM pets WHERE name LIKE %s OR species LIKE %s LIMIT %s OFFSET %s", (f'%{search}%', f'%{search}%', per_page, offset))
    else:
        cursor.execute("SELECT * FROM pets LIMIT %s OFFSET %s", (per_page, offset))
    pets = cursor.fetchall()
    return render_template('index.html', pets=pets, page=page, per_page=per_page)

# Add pet route
@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        available = request.form.get('available', False)
        cursor.execute("INSERT INTO pets (name, species, age, available) VALUES (%s, %s, %s, %s)", (name, species, age, available))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_pet.html')

# Edit pet route
@app.route('/edit_pet/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        available = request.form.get('available', False)
        cursor.execute("UPDATE pets SET name=%s, species=%s, age=%s, available=%s WHERE id=%s", (name, species, age, available, pet_id))
        db.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
    pet = cursor.fetchone()
    return render_template('edit_pet.html', pet=pet)

# Delete pet route
@app.route('/delete_pet/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    cursor.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
