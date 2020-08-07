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
class Test:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('postgres', 'openpg', 'openpgpwd')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

    def create_job(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE jobs(
                job_id SERIAL PRIMARY KEY,
                job_title VARCHAR DEFAULT '',
                min_salary INTEGER DEFAULT 2500,
                max_salary INTEGER DEFAULT NULL
            ) 
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def create_employee(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE employees(
                emp_id SERIAL PRIMARY KEY,
                first_name VARCHAR,
                last_name VARCHAR,
                salary INTEGER,
                job_id INTEGER REFERENCES jobs(job_id)
            ) 
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def ex6_c(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT first_name, last_name, salary
                FROM employees
                WHERE salary > 3500 AND salary < 6000
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def ex6_d(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT job_title, min_salary, max_salary
                FROM jobs
                WHERE min_salary < 8000
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def ex6_e_join(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT employees.first_name,employees.last_name,salary,jobs.job_title
                FROM employees
                    INNER JOIN jobs ON employees.job_id = jobs.job_id
                
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def ex6_e_not_join(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT employees.first_name,employees.last_name,salary,jobs.job_title
                FROM public.employees,public.jobs
                WHERE employees.job_id = jobs.job_id
                
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result
