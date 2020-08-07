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

class DAY_15:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('DATABASE_Day15', 'postgres', '123456')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

    def create_club(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE club(
                club_id SERIAL PRIMARY KEY,
                club_name VARCHAR NOT NULL,
                club_year INTEGER
            ) 
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()


    def create_country(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE country(
                country_id SERIAL PRIMARY KEY,
                country_name VARCHAR NOT NULL
            ) 
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()


    def create_player(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            CREATE TABLE player(
                player_id SERIAL PRIMARY KEY,
                player_name VARCHAR NOT NULL,
                player_age INTEGER,
                club_id INTEGER REFERENCES club(club_id),
                country_id INTEGER REFERENCES country(country_id)
            ) 
        """
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def insert_country(self, name):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO country (country_name) VALUES ('%s')
        """ % (name)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def insert_club(self, name, year):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO club (club_name,club_year) VALUES ('%s',%s)
        """ % (name, year)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def insert_player(self, name, age, club, country):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
            INSERT INTO player (player_name,player_age,club_id,country_id) VALUES ('%s','%s',%s,%s)
        """ % (name, age, club, country)
        self.cr.execute(sql)
        self.conn.commit()
        self.close_connection()

    def Player_Club(self):
        self.open_connection()
        if not self.cr and not self.conn:
            return
        sql = """
                SELECT player.player_name,club.club_name
                FROM player
                    INNER JOIN club ON club.club_id = player.club_id
                ORDER BY player.player_name ASC
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def find_Player_Real(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT player.player_name,club.club_name
                FROM player
                    INNER JOIN club ON player.club_id = club.club_id
                WHERE club.club_name = 'Real'
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def Count_Player_Real(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT club.club_name,COUNT(player.player_id)
                FROM player
                    INNER JOIN club ON player.club_id = club.club_id
                WHERE club.club_name = 'Real'
                GROUP BY club.club_id
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def Find_Player_Max_Age(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT player.player_name,player.player_age
                FROM player
                ORDER BY player.player_age DESC
                LIMIT 1    
        """
        self.cr.execute(sql)
        result = self.cr.fetchone()
        self.close_connection()
        return result

    def Find_Player_A_in_Name(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT player.player_name
                FROM player
                WHERE player.player_name LIKE '%A%'
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def Find_Player_In_Club(self,club):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT player.player_name,player.player_age,country.country_name
                FROM player
                    INNER JOIN country ON country.country_id = player.country_id
                    INNER JOIN club ON club.club_id = player.club_id
                WHERE club.club_name = '%s'
                ORDER BY player.player_name ASC
            """ % club
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def Find_Player_less_Age(self,age):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
                SELECT player.player_name,player.player_age,country.country_name
                FROM player
                    INNER JOIN country ON country.country_id = player.country_id
                    INNER JOIN club ON club.club_id = player.club_id
                WHERE player.player_age <= %d
                ORDER BY player.player_name ASC
            """ % age
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result
def Insert_club_country_player():
    num = int(input("Nhập số club muốn thêm : "))
    for i in range(0, num):
        club_name = input("Nhập tên club %d : " % (i + 1))
        club_year = input("Nhập năm thành lập : ")
        day = DAY_15()
        day.insert_club(club_name, club_year)
    num = int(input("Nhập số country muốn thêm : "))
    for i in range(0, num):
        country_name = input("Nhập tên country %d : " % (i + 1))
        day = DAY_15()
        day.insert_country(country_name)
    num = int(input("Nhập số player muốn thêm : "))
    for i in range(0, num):
        player_name = input("Nhập tên player %d : " % (i + 1))
        player_age = input("Nhập age : ")
        club = input("Nhập id club : ")
        country = input("Nhập id country : ")
        day = DAY_15()
        day.insert_player(player_name, player_age, club, country)

Day_15 = DAY_15()

#Tạo bảng
# Day_15.create_club()
# Day_15.create_country()
# Day_15.create_player()

#Thêm dữ liệu cho bảng
# Insert_club_country_player()

# # Bài 3
# player_club = Day_15.Player_Club()
# for i in player_club:
#     print(i)

# #Bài 4
# find_player_real = Day_15.find_Player_Real()
# for i in find_player_real:
#     print(i)

# #Bài 5
# count_player_real = Day_15.Count_Player_Real()
# for i in count_player_real:
#     print(i)

# #Bài 6
# find_player_max_age = Day_15.Find_Player_Max_Age()
# print(find_player_max_age)

# #Bài 7
# find_key_in_name = Day_15.Find_Player_A_in_Name()
# for i in find_key_in_name:
#     print(i)

# # #Bài9
# find_player_in_club = Day_15.Find_Player_In_Club()
# for player in find_player_in_club:
#     print(player)

# # #Bài10
# find_player_less_age = Day_15.Find_Player_less_Age(30)
# for player in find_player_less_age:
#     print(player)
