# Pet Adoption Web App

This is a simple web application built using Flask and MySQL for managing pet adoption.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- Flask
- MySQL

## Installation

1. Clone this repository to your local machine:

git clone (https://github.com/itskeshwam/pet-adoption.git)

2. Install the required Python packages:

pip install flask mysql-connector-python

3. Import the SQL schema and data:

- Execute the `schema.sql` file to create the necessary tables.
- Execute the `data.sql` file to populate the tables with sample data.

## Configuration

- Set up your MySQL database configuration by specifying the host, username, password, and database name in the environment variables or directly in the `app.py` file.

## Usage

1. Run the Flask application:

python app.py


2. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Features

- View a list of available pets.
- Add new pets to the database.
- Edit existing pet details.
- Delete pets from the database.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
