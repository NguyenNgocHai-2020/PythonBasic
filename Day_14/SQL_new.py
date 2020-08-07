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

class SQL_new:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('DATABASE', 'postgres', '123456')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

    def insert_department(self, dept_name, dept_no, dept_location):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO department(dept_name,dept_no,dept_location) VALUES ('%s','%s','%s')
        """ % (dept_name, dept_no, dept_location)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def insert_employee(self, employee_name, employee_address, dept_id):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO employee(name, address, dept_id) VALUES ('%s','%s',%s)
        """ % (employee_name, employee_address, dept_id)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def update_employee(self, name_old, name_new, address_new, dept_id_new):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        if not name_old:
            return
        update_sql = ""
        if name_new:
            update_sql += """name = '%s', """ % (name_new,)
        if address_new:
            update_sql += """address = '%s', """ % (address_new,)
        if dept_id_new:
            update_sql += """dept_id = %s """ % (dept_id_new,)
            sql = """
                UPDATE employee set %s WHERE name = '%s'        
            """ % (update_sql, name_old)
            self.cr.execute(sql)
            self.conn.commit()
        self.close_connection()

    def delete_employee(self, del_name):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        if not del_name:
            return
        sql = """
            DELETE FROM employee WHERE name = '%s'
        """ % (del_name)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

sql = SQL_new()
# sql.insert_department("SALE", "Dept_4", "HUNGYEN")
# sql.insert_employee("LE DINH K","HANOI",'2')
# sql.insert_employee("ABC","HANOI",'2')
# sql.update_employee('TA DINH T', '', '', '4')
sql.delete_employee('ABC')
