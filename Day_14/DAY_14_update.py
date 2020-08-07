import psycopg2

class ConnectPostgres:

    def __init__(self, db_name, user, pw, host='localhost', port=5432):

        self.db = db_name
        self.user = user
        self.pwd = pw
        self.host = host
        self.port = port

    def get_connection(self):
        try:
            conn = psycopg2.connect(database=self.db, user=self.user,
                                    password=self.pwd, port=self.port)
            return conn
        except Exception as e:
            print(str(e))
            return False

class DAY14:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('DAY_11_DATABASE', 'openpg', '123456')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

# Lấy ra nhân viên có chức vụ A
    def Fine_position(self,str):
        if not str:
            return
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            SELECT *
            FROM department
            WHERE dept_no = '%s'
        """ %str
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def insert_employee(self,name, start, phone):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO nhan_vien (name, start,phone) VALUES ('%s','%s','%s')
        """ %(name,start,phone)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()
    def update_employee(self,name_old,name_new = False,start_new = False,phone_new = False):
        if not name_old:
            return
        self.open_connection()
        if not self.conn and not self.cr:
            return
        update_employee = " "
        if name_new:
            update_employee += """name = '%s', """ %(name_new, )
            #Nên biến nó thành kiểu dict với key là tên cột và value là giá trị truyền vào
        if start_new:
            update_employee += """start = '%s', """ %(start_new, )
        if phone_new:
            # update_employee += """phone = '%s' """ % (phone_new, )
            update_employee += ('phone','%s') %(phone_new)
        if update_employee:
            sql = """
                UPDATE nhan_vien set %s WHERE name = '%s'            
            """ %(update_employee, name_old)
            self.cr.execute(sql)
            self.conn.commit()
        self.close_connection()

day_14 = DAY14()
# result = day_14.Fine_position('NS2')
# for i in result:
#     print(i)
#day_14.insert_employee('Nhân viên 3','2020-7-2',1234567)
day_14.update_employee('Nhân Viên 2','Nhân viên 4','2020-6-2','987654321')