import sqlite3


class Database:
    def __init__(self, db):
        #for Table 
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor() #to execute sql queries 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS items_table (id_number INTEGER PRIMARY KEY,user, customer, item, price)")
        self.connection.commit()

    ############################   Fetch Data   #################################################################
    def fetching_data(self):
        self.cursor.execute("SELECT * FROM items_table")
        any_row = self.cursor.fetchall()
        return any_row
    ########################################3   Insert Item #######################################################

    def insert(self, user, customer, item, price):
        self.cursor.execute("INSERT INTO items_table VALUES (NULL, ?, ?, ?, ?)",(user, customer, item, price))
        #Null for sql protection ,? placeholder for each value mentioned later
        self.connection.commit()
    ######################################################### Updatae the item  ################################

    def update(self, id_number, user, customer, item, price):
        self.cursor.execute("UPDATE items_table SET user = ?, customer = ?, item = ?, price = ? WHERE id_number = ?",(user, customer, item, price, id_number))
        self.connection.commit()
    ###############################  Remove the value from data base ########################################
    def remove(self, id_number):
        self.cursor.execute("DELETE FROM items_table WHERE id_number=?", (id_number,))
        self.connection.commit()
    ##########################  Destructor ##########################################################
    def __del__(self):
        self.connection.close()

db = Database('store.db')
# db.insert("Apple", "John", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")