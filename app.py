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

# Route for submitting adoption applications
@app.route('/apply_for_adoption/<int:pet_id>', methods=['POST'])
def apply_for_adoption(pet_id):
    # Code to handle adoption application submission
    pass

# Route for reviewing adoption applications (for administrators)
@app.route('/review_adoption_applications')
def review_adoption_applications():
    # Code to display adoption applications for review
    pass

# Check if the pet_reviews table exists before creating it
cursor.execute("SHOW TABLES LIKE 'pet_reviews'")
if not cursor.fetchone():
    cursor.execute("""
    CREATE TABLE pet_reviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pet_id INT,
        user_id INT,
        rating INT,
        review TEXT,
        FOREIGN KEY (pet_id) REFERENCES pets(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)


# Add a route for submitting pet reviews
@app.route('/submit_pet_review/<int:pet_id>', methods=['POST'])
def submit_pet_review(pet_id):
    # Code to handle pet review submission
    pass

# Add a route for registering pet microchip information
@app.route('/register_microchip/<int:pet_id>', methods=['POST'])
def register_microchip(pet_id):
    # Code to handle pet microchip registration
    pass

if __name__ == '__main__':
    app.run(debug=True)
