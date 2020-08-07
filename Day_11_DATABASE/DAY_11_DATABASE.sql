CREATE TABLE department (
	dept_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(50),
	dept_no TEXT,
	dept_location TEXT	
);
--Thêm cột lương
ALTER TABLE department ADD COLUMN salary INT;
ALTER TABLE department ALTER COLUMN salary TYPE INTEGER
INSERT INTO department (dept_name,dept_no,dept_location)
VALUES ('NGUYỄN NGỌC HẢi','NS3','MỄ TRÌ');
INSERT INTO department (dept_name, dept_no,dept_location)
VALUES ('PHẠM DUY TUẤN','NS2','MỄ TRÌ');
INSERT INTO department(dept_name, dept_no,dept_location)
VALUES ('TRẦN NGUYỄN BẢO ANH','NS2','NHÂN CHÍNH');
INSERT INTO department(dept_name, dept_no,dept_location)
VALUES ('NGUYỄN BẢO ANH','NS1','BA ĐÌNH');
--Update thêm dữ liệu cho cột salary
UPDATE department SET salary = 300 WHERE dept_id = 1;
UPDATE department SET salary = 1000 WHERE dept_id = 2;
UPDATE department SET salary = 700 WHERE dept_id = 3;
UPDATE department SET salary = 200 WHERE dept_id = 4;
UPDATE department SET dept_name = 'HOÀNG BẢO ANH' WHERE dept_id = 3;
UPDATE department SET salary = 600 WHERE dept_id = 3;
UPDATE department SET salary = 1000 WHERE dept_id = 1;

--hiển thị bảng department
SELECT *
FROM department
-- sắp xếp bảng theo mức lương tăng dần ASC, và giảm dần là DESC
SELECT *
FROM department
ORDER BY salary ASC;
SELECT *
FROM department
ORDER BY dept_name ASC;
--Lấy ra tên bắt đầu là chữ A : A%, kết thúc chữ A : %A,có chữ A: %A%
SELECT *
FROM department
WHERE dept_name LIKE 'N%';
--Thêm 2 bản ghi
INSERT INTO department(dept_name, dept_no,dept_location)
VALUES ('TRẦN Thảo Vân','NS0','Ba ĐÌNH');
INSERT INTO department(dept_name, dept_no,dept_location)
VALUES ('TẠ ĐÌNH TÚ','NS4','THANH XUÂN');
--Câu lệnh update lương cho những bạn có tên bắt đầu bằng chữ T
UPDATE department SET salary = '400' WHERE dept_name LIKE 'T%';
--Tính tổng salary(Không có điều kiện)
SELECT SUM(salary)
FROM department;
--Tính tổng salary (với điều kiện của những người thuộc NS2)
SELECT SUM (salary)
FROM department
WHERE dept_no LIKE 'NS2'; /*WHERE dept_no = 'NS2'*/
--Tính tổng mức lương của những người có lương lớn hơn 300
SELECT SUM (salary)
FROM department
WHERE salary >=300








