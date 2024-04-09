CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    available BOOLEAN NOT NULL,
    image_url varchar(255)
);
