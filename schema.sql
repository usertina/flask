DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT
);

INSERT INTO users (first_name, last_name, age, phone) VALUES
('Juan', 'Pérez', 30, '1234567890'),
('María', 'Gómez', 25, '9876543210'),
('Carlos', 'Martínez', 35, '5551234567'),
('Laura', 'López', 28, '7890123456'),
('Pedro', 'Sánchez', 40, '3216549870'),
('Javier', 'Ruiz', 44, '3216577870');
