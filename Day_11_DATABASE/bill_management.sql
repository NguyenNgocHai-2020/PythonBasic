CREATE TABLE khach_hang (
	id VARCHAR(10) not NULL PRIMARY KEY,
	name VARCHAR(50) not NULL,
	address TEXT,
	phone VARCHAR(12),
	dob DATE,
	start TIMESTAMP
);
CREATE TABLE  nhan_vien (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	start DATE,
	phone VARCHAR(12)
);
CREATE TABLE sanpham (
	masp serial primary key,
	tensp varchar not null,
	dvt varchar,
	nuocsx varchar,
	gia integer default 1
);

CREATE TABLE hoadon (
	sohd serial primary key,
	ngayhd timestamp,
	makh varchar(10) not null references khach_hang(id),
	manv_lk integer not null,
	giatri integer not null,
	constraint fk_hd_nv foreign key (manv_lk) references nhan_vien(id)
);

CREATE TABLE hoadon_chitiet (
	sohd INTEGER,
	masp INTEGER,
	sl INTEGER NOT NULL,
	CONSTRAINT pk_hd_ct PRIMARY KEY (sohd, masp)
);
--Tạo dữ liệu
INSERT INTO khach_hang VALUES ('KH01', 'Nguyễn Văn A', 'Hà Nội', '0246145', '1991-01-01', '2019-06-15 20:05:30');
INSERT INTO khach_hang (id, name) VALUES ('KH02', 'LÊ THỊ B');
SELECT id FROM khach_hang;
INSERT INTO nhan_vien (name,start,phone) VALUES ('Nhân Viên 1', '2018-01-01', '00000000');
INSERT INTO nhan_vien (name,start,phone) VALUES ('Nhân Viên 2', '2018-01-01', '00000000');
SELECT id FROM nhan_vien;
INSERT INTO sanpham (tensp, dvt, nuocsx, gia) values ('xà phòng', 'chiếc', 'vn', 10000);
INSERT INTO sanpham (tensp, dvt, nuocsx, gia) values ('kem', 'chiếc', 'thái', 20000);
INSERT INTO sanpham (tensp, dvt, nuocsx, gia) values ('bàn chải', 'chiếc', 'tq', 5000);
SELECT * FROM sanpham;
INSERT INTO hoadon (ngayhd, makh, manv_lk, giatri) VALUES ('2019-01-01 08:00:05','KH01','2', '50000');
SELECT * FROM hoadon;
INSERT INTO hoadon_chitiet VALUES (1, 2, 2);
INSERT INTO hoadon_chitiet VALUES (1, 1, 1);
SELECT * FROM hoadon_chitiet;