DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT
);

INSERT INTO users (first_name, last_name, age, phone) VALUES
('Anna', 'Iashvili', 50, '1234567890'),
('Tina', 'Calleja', 42, '9876543210'),
('Sebastian', 'Rodrigez', 34, '5551234567'),
('Keltum', 'Debour', 28, '7890123456'),
('Oussama', 'Brahmi', 33, '3216549870'),
('Jonathan', 'Ibañez', 33, '3216577870'),
('Aintzane', 'Goffard', 31, '3216277870'),
('Abderrahmane', 'Hichou', 17, '3216277870'),
('Elias', 'Riquelme', 34, '3216277970'),
('Jhony', 'Dominguez', 28, '3216277875'),
('Andress', 'Echeberry', 34, '3218277870'),
('Jesus', 'Romero', 20, '3216177870'),
('Jhon', 'Davila', 27, '3216177871'),
('Lurdes', 'Espinola', 30, '3216177872');
