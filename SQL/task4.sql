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

CREATE TABLE library_branches (
	branch_id SERIAL PRIMARY KEY,
	branch_name VARCHAR(50) NOT NULL
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
INSERT INTO books (author_id, title, genre, publish_date) VALUES (1, 'Sherlock', 'classic', '2011-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (2, 'Romeo&Juliette', 'love classic', '2010-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Python Crash Course', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book1', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book2', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book3', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book4', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book5', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book6', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book7', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book8', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book9', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book10', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book11', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book12', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book13', 'study', '2015-03-01');
INSERT INTO books (author_id, title, genre, publish_date) VALUES (3, 'Book14', 'study', '2015-03-01');

-- INSERT TO TABLE users
ALTER TABLE USERS ADD COLUMN country VARCHAR(50);
INSERT INTO	users (full_name, email, birth_date, country) VALUES ('Василий Петор', 'petrovich@gmail.com', '1995-05-08', 'Poland');
INSERT INTO	users (full_name, email, birth_date, country) VALUES ('Антон Венегретов', 'anton@gmail.com', '1991-02-16', 'Ukraine');
INSERT INTO	users (full_name, email, birth_date, country) VALUES ('Инакентий Виссарионович', 'inakentiy@gmail.com', '1957-07-30', 'Ukraine');
INSERT INTO	users (full_name, email, birth_date, country) VALUES ('Employee1', 'inakentiy@gmail.com', '1957-07-30', 'Ukraine');
INSERT INTO	users (full_name, email, birth_date, country) VALUES ('SUPEREMP', 'petrovich@gmail.com', '1995-05-08', 'Germany');

-- INSERT TO TABLE library_branches
INSERT INTO library_branches (branch_name) VALUES ('brach1');
INSERT INTO library_branches (branch_name) VALUES ('brach2');
INSERT INTO library_branches (branch_name) VALUES ('brach3');
INSERT INTO library_branches (branch_name) VALUES ('brach4');
INSERT INTO library_branches (branch_name) VALUES ('brach5');
INSERT INTO library_branches (branch_name) VALUES ('brach6');
INSERT INTO library_branches (branch_name) VALUES ('brach7');
INSERT INTO library_branches (branch_name) VALUES ('brach8');
INSERT INTO library_branches (branch_name) VALUES ('brach9');


-- INSERT TO TABLE employees
ALTER TABLE employees ADD COLUMN branch_name VARCHAR(50);
ALTER TABLE employees ADD COLUMN country VARCHAR(50);
ALTER TABLE employees ADD COLUMN branch_id INT REFERENCES library_branches(branch_id);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee1', 'branch1', 'Greece', 1);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee2', 'branch1', 'Greece', 2);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee3', 'branch2', 'Greece', 2);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee4', 'branch2', 'Poland', 3);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee5', 'branch2', 'Poland', 4);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee5', 'branch3', 'Poland', 4);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee6', 'branch3', 'Ukraine', 4);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee7', 'branch3', 'Ukraine', 5);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee8', 'branch3', 'Ukraine', 6);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee9', 'branch3', 'Ukraine', 7);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee10', 'branch3', 'Ukraine', 7);
INSERT INTO employees (full_name, branch_name, country, branch_id) VALUES ('Employee10', 'branch3', 'USA', 7);

-- INSERT TO TABLE library_branches
INSERT INTO library_branches (branch_name) VALUES ('brach1');
INSERT INTO library_branches (branch_name) VALUES ('brach2');
INSERT INTO library_branches (branch_name) VALUES ('brach3');
INSERT INTO library_branches (branch_name) VALUES ('brach4');
INSERT INTO library_branches (branch_name) VALUES ('brach5');
INSERT INTO library_branches (branch_name) VALUES ('brach6');
INSERT INTO library_branches (branch_name) VALUES ('brach7');
INSERT INTO library_branches (branch_name) VALUES ('brach8');
INSERT INTO library_branches (branch_name) VALUES ('brach9');


-- INSERT TO TABLE book_rental
INSERT INTO book_rental(book_id, user_id) VALUES (2, 3);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 2);
INSERT INTO book_rental(book_id, user_id) VALUES (1, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);
INSERT INTO book_rental(book_id, user_id) VALUES (3, 1);


-- Homework / Task 4
-- 1.

SELECT full_name, book_rental.rental_date, COUNT(full_name)
FROM users
JOIN book_rental ON users.user_id = book_rental.user_id
GROUP BY full_name;

-- 2.
SELECT full_name, COUNT(full_name)
FROM users
JOIN book_rental ON users.user_id = book_rental.user_id
GROUP BY full_name

-- 3.

SELECT full_name, books.title, COUNT(full_name)
FROM users
LEFT JOIN book_rental ON users.user_id = book_rental.user_id
LEFT JOIN books ON books.book_id = book_rental.book_id
GROUP BY full_name, books.title
ORDER BY COUNT(full_name) DESC
LIMIT 10;

-- 4.

SELECT full_name, books.title, COUNT(full_name)
FROM users
LEFT JOIN book_rental ON users.user_id = book_rental.user_id
LEFT JOIN books ON books.book_id = book_rental.book_id
WHERE books.title IS NOT NULL
GROUP BY full_name, books.title
ORDER BY COUNT(full_name) DESC
LIMIT 10;

-- 5.

SELECT full_name, library_branches.branch_name
FROM employees
FULL JOIN library_branches ON employees.branch_id = library_branches.branch_id

-- 6. 
SELECT employees.full_name, users.full_name, library_branches.branch_name
FROM employees
FULL JOIN library_branches ON employees.branch_id = library_branches.branch_id
LEFT JOIN users ON employees.country = users.country
WHERE employees.country = 'USA' OR users.country = 'USA'
























