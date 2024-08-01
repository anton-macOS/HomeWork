CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	email VARCHAR(50)
);
CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80),
	price DECIMAL
);
CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(id),
	product_id INT REFERENCES products(id),
	order_date DATE,
	quantity INT
);
CREATE TABLE suppliers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	contact_name VARCHAR(50)
);
CREATE TABLE product_suppliers (
	id SERIAL PRIMARY KEY,
	product_id INT REFERENCES products(id),
	supplier_id INT REFERENCES suppliers(id),
	supply_date DATE
);


INSERT INTO customers (name, email) VALUES ('Anton', 'anton@gmail.com');
INSERT INTO customers (name, email) VALUES ('Vlad', 'vlad@gmail.com');
INSERT INTO customers (name, email) VALUES ('Dima', 'dima@yahoo.com');
INSERT INTO customers (name, email) VALUES ('Vasiya', 'vasiya@gmail.com');


INSERT INTO products (name, price) VALUES ('product1', 1.95);
INSERT INTO products (name, price) VALUES ('product2', 100.58);
INSERT INTO products (name, price) VALUES ('product3', 19.76);
INSERT INTO products (name, price) VALUES ('product4', 36.48);
INSERT INTO products (name, price) VALUES ('product5', 1000.01);
INSERT INTO products (name, price) VALUES ('product6', 505.78);
INSERT INTO products (name, price) VALUES ('product7', 99.99);
INSERT INTO products (name, price) VALUES ('product8', 25.43);
INSERT INTO products (name, price) VALUES ('product9', 100000.99);


INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (3, 1, '2024-03-23', 10);
INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (2, 7, '2024-05-17', 3);
INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (1, 8, '2024-06-09', 7);
INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (4, 5, '2024-02-25', 12);
INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (4, 9, '2024-06-30', 1);


INSERT INTO suppliers (name, contact_name) VALUES ('Andrej', 'Andrej_LLC');
INSERT INTO suppliers (name, contact_name) VALUES ('City LLC', 'Ilona');
INSERT INTO suppliers (name, contact_name) VALUES ('Start LLC', 'Egor');

INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (9, 1, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (8, 1, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (7, 1, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (6, 1, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (5, 2, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (4, 2, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (3, 2, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (2, 3, '2024-07-13');
INSERT INTO product_suppliers (product_id, supplier_id, supply_date)
VALUES (1, 3, '2024-07-13');

-- HOMEWORK
SELECT * FROM products;
SELECT email FROM customers WHERE email LIKE '%@gmail.com';
SELECT SUM(quantity) FROM orders;
SELECT COUNT(quantity) FROM orders WHERE customer_id = '4';
SELECT name FROM products WHERE price BETWEEN 10 AND 100;






