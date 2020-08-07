-- CREATE product table
CREATE TABLE product (
	code SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	made_in VARCHAR,
-- 	price integer default 10000,
	price INTEGER CHECK(price > 0 AND price < 10000000)
	-- add constraint fkey in create table command
	--category_code INTEGER REFERENCES categories(code)
);

-- CREATE categories table
CREATE TABLE categories (
	code SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL
);

-- CREATE order table
CREATE TABLE orders (
	code INTEGER PRIMARY KEY,
	order_date TIMESTAMP NOT NULL
);
-- ADD column for product table
ALTER TABLE product ADD COLUMN date_made DATE;
ALTER TABLE product ADD COLUMN category_code INTEGER;
-- DROP column
ALTER TABLE product DROP COLUMN date_made;
-- ALTER column
ALTER TABLE product ADD COLUMN date_made DATE;
ALTER TABLE product ALTER COLUMN date_made TYPE TIMESTAMP;
-- RENAME column
ALTER TABLE product RENAME COLUMN date_made TO date_manufactor;
-- ADD constraint
-- add constraint fkey in alter table command
ALTER TABLE product ADD CONSTRAINT product_category_foreign 
FOREIGN KEY(category_code) REFERENCES categories(code);
-- DROP constraint
ALTER TABLE product DROP CONSTRAINT product_category_code_fkey;
--DROP table
DROP TABLE product;
-- INSERT PRODUCT
INSERT INTO product(name, made_in, price) VALUES('but bi', 'VN', 10000);
SELECT category_code FROM categories

-- INSERT CATEGORIES
INSERT INTO categories(name) VALUES('VPP');
SELECT * FROM categories

-- INSERT ORDERS
INSERT INTO orders VALUES(1, '2019-10-10 15:00:00')


INSERT INTO product(name, made_in, price, category_code) VALUES('bang den', 'VN', 30000, 1);
SELECT * FROM product
