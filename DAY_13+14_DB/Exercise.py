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

class Exercise:
    def __init__(self):
        self.connect_postgres = ConnectPostgres('DATABASE', 'postgres', '123456')

    def open_connection(self):
        self.conn = self.connect_postgres.get_connection()
        self.cr = self.conn.cursor()

    def close_connection(self):
        self.cr.close()
        self.conn.close()

    def find_customer_9(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
        SELECT  product.id,product.name ,SUM(order_line.quantity) AS total_quantity
        FROM product
        INNER JOIN order_line ON product.id = order_line.product_id
        GROUP BY product.id
        ORDER BY total_quantity DESC
        LIMIT 1
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def find_customer_10(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
        SELECT category.id,category.name,SUM(order_line.quantity) AS total_quantity
        FROM category
        INNER JOIN product ON category.id = product.category_id
        INNER JOIN order_line ON product.id = order_line.product_id
        GROUP BY category.id
        ORDER BY total_quantity DESC
        LIMIT 1
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result
    def find_customer_11(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
        SELECT category.id,category.name,SUM(order_line.price) AS total_price
        FROM category
        INNER JOIN product ON category.id = product.category_id
        INNER JOIN order_line ON product.id = order_line.product_id
        GROUP BY category.id
        ORDER BY total_price DESC
        LIMIT 1
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result
    def find_customer_12(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
        SELECT customer.address,COUNT(customer.id) AS total_name
        FROM customer
        GROUP BY customer.address
        ORDER BY total_name ASC
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

    def find_customer_13(self):
        # self.open_connection()
        # if not self.conn and not self.cr:
        #     return
        # sql = """
        # SELECT customer.address, COUNT(order_line.order_id) AS total_order
        # FROM customer
        #     INNER JOIN orders ON customer.id = orders.customer_id
        #     INNER JOIN order_line ON orders.id = order_line.order_id
        # GROUP BY customer.address
        # ORDER BY total_order DESC
        #
        # """
        # self.cr.execute(sql)
        # result = self.cr.fetchall()
        # self.close_connection()
        # return result
        self.open_connection()
        if not self.conn and not self.cr:
            return
        query = """ 
                    SELECT address, count(id) AS total_customer, SUM(total_order) AS total_orders FROM 
                    (
                        SELECT c.id, c.name, c.address, COUNT(o.id) AS total_order
                        FROM customer c 
                        INNER JOIN orders o ON c.id = o.customer_id
                        GROUP BY c.id
                    ) AS temp_q
                    GROUP BY address
                    ORDER BY total_customer DESC, total_orders DESC
                    LIMIT 1
                """
        self.cr.execute(query)
        kq = self.cr.fetchall()
        self.close_connection()
        return kq
    def find_customer_14(self):
        self.open_connection()
        if not self.conn and not self.cr:
            return
        sql = """
        SELECT product.id,product.name
        FROM product
        WHERE product.id NOT IN
            (SELECT product.id
            FROM product 
            INNER JOIN order_line ON product.id = order_line.product_id)
        """
        self.cr.execute(sql)
        result = self.cr.fetchall()
        self.close_connection()
        return result

ex = Exercise()
result = ex.find_customer_13()
for i in result:
    print(i)