import mysql.connector


# cursor = cnx.cursor()

# query = (
# cursor.execute(query)


class ConnecyMyDataBase:

    def __init__(self):
        self.cnx = None
        self.cursor = None

    def set_connection(self, user, password, host, database):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

    def get_connection(self):
        """Get connection"""
        return self.cnx

    def get_connection_cursor(self):
        """get cursor"""
        return self.cursor

    def insert_table_many_data(self, data, linha):
        # cnx = mysql.connector.connect(user=
        #                             'uece', password="1", host='127.0.0.1', database='EGRESSO')
        # cursor = connection.cursor()
        self.cursor = self.cnx.cursor()
        print('Inserindo dados: ' + data)
        query = 'INSERT INTO DOCENTES VALUES (' + data + ');'
        self.cursor.execute(query)
        self.cnx.commit()
        print("Dados inseridos com sucesso, na linha: " + str(linha))

    def insert_table_IES(self, data, linha):
        self.cursor = self.cnx.cursor()
        print('Inserindo dados: ' + data)
        query = 'INSERT INTO IES VALUES (' + data + ');'
        self.cursor.execute(query)
        self.cnx.commit()
        print("Dados inseridos com sucesso, na linha: " + str(linha))

    def insert_table_distrito(self, data, linha):
        self.cursor = self.cnx.cursor()
        print('Inserindo dados: ' + data)
        query = 'INSERT INTO DISTRITOS VALUES (' + data + ');'
        self.cursor.execute(query)
        self.cnx.commit()
        print("Dados inseridos com sucesso, na linha: " + str(linha))

    def insert_table_cfs(self, data, linha):
        self.cursor = self.cnx.cursor()
        print('Inserindo dados: ' + data)
        query = 'INSERT INTO CFS VALUES (' + data + ');'
        self.cursor.execute(query)
        self.cnx.commit()
        print("Dados inseridos com sucesso, na linha: " + str(linha))
