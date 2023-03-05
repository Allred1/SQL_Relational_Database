import sqlite3

class main():

    # Create connection to a database
    conn = sqlite3.connect("database.db")
    print("Opened database successfully")
  

    # Create a table function
    def create_table(conn):
        print("Let's create a table!")
        table_data = []
        table_name = input("Enter table name: ")
        table_data.append(table_name)

        def insert_column(table_data):
            # ask user to add columns
            addColumn = True
            while addColumn != False:
                column = input("Enter a column: ")
                table_data.append(column)
                another = input("Add another [y/n]? : ")
                if another == "y":
                    continue
                else:
                    addColumn = False
                
        # check existing tables before creating one
        def check_then_create(tbl_name, fst_column):
            # Create a cursor
            cur = conn.cursor()
            # check that the table exists before creating one
            cur.execute(f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{tbl_name}' ''')
            if cur.fetchone()[0]==1 :
                print("Table name already exists.")
            else:
                cur.execute(f"CREATE TABLE {tbl_name}({fst_column})")
                table_data.remove(table_data[1])
                table_data.remove(table_data[0])
                while len(table_data) > 0:
                    conn.execute(f"ALTER TABLE {tbl_name} ADD COLUMN {table_data[0]} TEXT")
                    table_data.remove(table_data[0])
                print("Table Created.")
            
        conn.commit()


        # table information as list; [0] = key, [1+] = values
        insert_column(table_data)

        # get name, first column
        tbl_name = table_data[0]
        fst_column = table_data[1]
        
        check_then_create(tbl_name, fst_column)
            

    # see all tables
    def fetch_tables(conn):
        cur = conn.cursor()
        cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
        # print(cur.fetchall())
        rows = cur.fetchall()
        for row in rows:
            for item in row:
                print(item)


    # delete a table
    def delete_table(conn, table):
        cur = conn.cursor()
        cur.execute(f"DROP TABLE {table}")
        print("Table Deleted.")


     # see all data in table
    def fetch_table_data(conn, tbl_name):
        cur = conn.cursor()
        print(f"{tbl_name} Table:")
        data = cur.execute(f"SELECT * FROM {tbl_name}")
        
        
        for column in data.description:
            print(f"{column[0]}:")
        for row in data:
            print(row)


    def values_menu(conn):
        # insert value
        # def insert_value(table_name):
        #     column = input("Select column: ")
        #     value = input("Input a value: ")
        #     conn.execute(f"UPDATE {table_name} SET {column}={value} WHERE {column}")
        #     pass
        # # delete
        # # change
        # # retrieve
        # def retrieve_value(table_name):
        #     conn.execute(f"SELECT * FROM {table_name}")
            
        index = 0
        while index < 5:
            print("\n1. Insert Value")
            print("2. Delete Value")
            print("3. Update Value")
            print("4. Retrieve Value")
            print("5. Go Back")
            index = int(input("Enter a selection: "))
            print()

            match index:
                case 1:
                    # insert
                    pass
                case 2:
                    # delete
                    pass
                case 3:
                    # update
                    pass
                case 4:
                    # retrieve
                    pass
                case 5:
                    # go back
                    break
                case _:
                    pass

    
    index = 0
    # database menu
    while index != 5:
        print("\n1. Create Table")
        print("2. Delete Table")
        print("3. Enter a Table")
        print("4. See All Tables")
        print("5. Quit")
        index = int(input("Enter a Selection: "))
        print()

        match index:
            case 1:
                create_table(conn)
            case 2:
                fetch_tables(conn)
                table = input("Select table to delete: ")
                delete_table(conn, table)
            case 3:
                fetch_tables(conn)
                print()
                table = input("Select table to enter: ")
                fetch_table_data(conn, table)
                values_menu(conn)
            case 4:
                fetch_tables(conn)
            case 5:
                quit()
            case _:
                pass

    
    # DATABASE MENU
        # create a database
            # create a table
                # (add columns)
            # delete a table
            # enter a table
                # value methods
            # see all tables
            # quit


            # (value methods)
                # insert to a table
                # modify in a table
                # delete from a table
                # retrieve from a table


    # Plans for VALUE METHODS
        # all columns are NULL (because of ALTER TABLE method)
        # So fix that (need TYPE and NOT NULL of each column)
        # INSERT something in a column
        # DELETE something in a column
        # UPDATE something in a column
        # RETRIEVE something in a column

        # INSERT INTO table_name [(column1,column2,column3,...columnN)] VALUES (value1, value2, value3,...valueN);
        # Display the table columns
        # allow user to enter value into each column like a menu
        # Use those variables to write the INSERT statement

        # (note: use "WHERE" to delete selected rows, or else it'll delete every row. Also, can combine N number of conditions using AND or OR operators)
        # DELETE FROM table_name WHERE column_name=value
        # delete specific rows by ids (for example)
        # or delete all records within

        # (update a value within a specified column)
        # UPDATE table_name SET column=value WHERE column=value
        # can update all values of a specified column

        # (fetch values from fields in a table)
        # SELECT column1, column2, columnN FROM table_name
        # SELECT * FROM table_table ---to fetch all fields available in the field
        # use .header on, .mode column to properly format the resulting display
        # can alter the display column width by: .width 10,20,10 etc.

    # Commit
    conn.commit()
    # Close the connection
    conn.close()

if __name__ ==  "__main__":
    main()