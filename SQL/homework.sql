-- Create database library
CREATE DATABASE library;
-- CREATE TABLES
CREATE TABLE authors (
	author_id SERIAL PRIMARY KEY,
	full_name VARCHAR(80) NOT NULL
);

CREATE TABLE books (
	book_id SERIAL PRIMARY KEY,
	author_id INT REFERENCES authors(author_id),
	title VARCHAR(128) NOT NULL,
	genre VARCHAR(50),
	publish_date DATE
);

CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	full_name VARCHAR(80) NOT NULL,
	email VARCHAR(80),
	birth_date DATE
);

CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	full_name VARCHAR(80) NOT NULL
);

CREATE TABLE book_rental (
	rental_id SERIAL PRIMARY KEY,
	book_id INT REFERENCES books(book_id),
	user_id INT REFERENCES users(user_id),
	rental_date TIMESTAMP DEFAULT NOW(), 
	return_date TIMESTAMP
);

-- INSERT TO TABLE authors
INSERT INTO authors (full_name) VALUES ('Arthur Conan Doyle');
INSERT INTO authors (full_name) VALUES ('William Shakespeare');
INSERT INTO authors (full_name) VALUES ('Eric Matthes');


-- INSETR TO TABLE books
INSERT INTO books (author_id, title, genre, publish_date) VALUES (7, 'Sherlock', 'classic', '2011-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (8, 'Romeo&Juliette', 'love classic', '2010-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (9, 'Python Crash Course', 'study', '2015-03-01');

-- INSERT TO TABLE users
INSERT INTO	users (full_name, email, birth_date) VALUES ('Василий Петор', 'petrovich@gmail.com', '1995-05-08');
INSERT INTO	users (full_name, email, birth_date) VALUES ('Антон Венегретов', 'anton@gmail.com', '1991-02-16');
INSERT INTO	users (full_name, email, birth_date) VALUES ('Инакентий Виссарионович', 'inakentiy@gmail.com', '1957-07-30');

-- INSERT TO TABLE employees
INSERT INTO employees (full_name) VALUES ('Василиса Инакентивна');

-- INSERT TO TABLE book_rental
INSERT INTO book_rental(book_id, user_id) VALUES (2, 3);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 2);
INSERT INTO book_rental(book_id, user_id) VALUES (4, 1);

-- SELECT
SELECT full_name FROM authors
SELECT title, genre, publish_date FROM books
SELECT * FROM book_rental
