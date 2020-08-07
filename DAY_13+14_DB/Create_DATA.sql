-- tao bang category (id, name)
CREATE TABLE category (
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL
);
-- tao bang product (id, name, price, category_id)

CREATE TABLE product (
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	price INTEGER,
	category_id INTEGER REFERENCES category(id)
);


--   tao bang customer (id, name, phone, address)
CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	phone INTEGER,
	-- name VARCHAR
	address TEXT
);
--   tao bang orders (id, customer_id, order_date)
CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer_id INTEGER REFERENCES customer(id),
	order_date DATE
);
--   tao bang order_line (id, order_id, product_id, quantity, price)
CREATE TABLE order_line (
	id SERIAL PRIMARY KEY,
	order_id INTEGER REFERENCES orders(id),
	product_id INTEGER REFERENCES product(id),
	quantity INTEGER,
	price INTEGER
);




-- 2. *) insert du lieu cho bang catgory (name):
-- gia dung
-- tieu dung
-- dien may

INSERT INTO category (name) VALUES('Gia dung');
INSERT INTO category (name) VALUES('Tieu dung');
INSERT INTO category (name) VALUES('Dien may');

-- *) insert du lieu cho bang product (name, price, category_id):

INSERT INTO product(name, price, category_id) VALUES('xa phong',10000,2);
INSERT INTO product(name, price, category_id) VALUES('dau goi dau',15000,2);
INSERT INTO product(name, price, category_id) VALUES('tu thuoc',100000,1);
INSERT INTO product(name, price, category_id) VALUES('vot muoi',100000,1);
INSERT INTO product(name, price, category_id) VALUES('ban an',200000,1);
INSERT INTO product(name, price, category_id) VALUES('xoong inox',150000,1);
INSERT INTO product(name, price, category_id) VALUES('dien thoai',5000000,3);
INSERT INTO product(name, price, category_id) VALUES('quat',1000000,3);
INSERT INTO product(name, price, category_id) VALUES('sac du phong',300000,3);
INSERT INTO product(name, price, category_id) VALUES('dieu hoa',12000000,3);

-- customer
INSERT INTO customer(name, phone, address) VALUES('Phong','098798789','Ha Noi');
INSERT INTO customer(name, phone, address) VALUES('Hieu','0973344333','Hai Phong');
INSERT INTO customer(name, phone, address) VALUES('Nam','0234443333','Nam Dinh');
INSERT INTO customer(name, phone, address) VALUES('Phuc','0453243343','Ha Noi');
INSERT INTO customer(name, phone, address) VALUES('Ngoc','0876766567','Khanh Hoa');
INSERT INTO customer(name, phone, address) VALUES('Ha','0913345454','Hai Phong');

-- orders
INSERT INTO orders(customer_id, order_date) VALUES(1, '2019-02-12 18:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(2, '2018-01-01 13:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(3, '2018-05-05 14:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(4, '2018-09-09 10:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(5, '2019-07-07 09:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(6, '2019-08-08 15:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(6, '2019-10-10 17:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(1, '2018-04-04 15:00:00');
INSERT INTO orders(customer_id, order_date) VALUES(2, '2018-04-04 15:00:00');

-- order_line
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(1, 1, 2, 20000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(1, 2, 2, 30000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(2, 3, 1, 100000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(3, 4, 1, 100000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(3, 3, 1, 100000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(4, 8, 1, 1000000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(4, 6, 1, 150000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(5, 8, 2, 2000000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(6, 7, 1, 5000000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(6, 9, 1, 300000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(7, 10, 1, 12000000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(8, 8, 1, 1000000);
INSERT INTO order_line(order_id, product_id, quantity, price) VALUES(8, 5, 1, 200000);




