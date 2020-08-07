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

class Demo:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('DATABASE', 'postgres', '123456')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

    def create_country(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE country (
                id serial primary key,
                name varchar not null,
                code varchar not null
            )
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def insert_country(self, name, code):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO country (name, code) VALUES ('%s', '%s')
        """ % (name, code)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def update_country(self, country_id, name=False, code=False):
        if not country_id:
            return
        self.open_connection()
        if not self.conn and not self.cr:
            return
        update_query = ""
        if name:
            update_query += """ name='%s', """ % (name,)
        if code:
            update_query += """ code='%s'""" % (code,)
        if update_query:
            sql = """
                UPDATE country set %s WHERE id = %s
            """ % (update_query, country_id)
            self.cr.execute(sql)
            self.conn.commit()
        self.close_connection()

    def select_all_country(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            SELECT * FROM country
        """
        self.cr.execute(sql)
        # self.cr.fetchone()
        # self.conn.commit()
        result = self.cr.fetchall()
        self.close_connection()
        return result

    # def select_country_by_id(self, country_id):
    #     if not country_id:
    #         return
    #     self.open_connection()
    #     if not self.conn and not self.cr:
    #         return
    #     sql = """
    #         SELECT * FROM country WHERE id = %s
    #     """ % (country_id,)
    #     self.cr.execute(sql)
    #     # self.cr.fetchone()
    #     # self.conn.commit()
    #     result = self.cr.fetchone()
    #     self.close_connection()
    #     return result

    # def select_all_country(self):
    #     self.open_connection()
    #     if not self.conn and not self.cr:
    #         return
    #     sql = """
    #         SELECT * FROM country
    #     """
    #     self.cr.execute(sql)
    #     result = self.cr.fetchall()
    #     self.close_connection()
    #     return result

    # def select_country_by_id(self, country_id):
    #     if not country_id:
    #         return
    #     self.open_connection()
    #     if not self.conn and not self.cr:
    #         return
    #     sql = """
    #         SELECT * FROM country WHERE id = %s
    #     """ % (country_id,)
    #     self.cr.execute(sql)
    #     result = self.cr.fetchone()
    #     self.close_connection()
    #     return result
demo = Demo()
demo.create_country()
demo.insert_country("VN","+84")
demo.insert_country("THAI LAN","+66")
demo.insert_country("PhiLipPin","+63")
demo.insert_country("Singapo","+60")
demo.insert_country("LAO", "+856")
# demo.delete_country(1)
# demo.delete_country(2)
# demo.delete_country(3)

# demo.update_country(4,'','+65')
result = demo.select_all_country()
for i in result:
    print(i)
# print("----------------------------------")
# print(demo.select_country_by_id(4))