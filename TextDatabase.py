import psycopg2


def bullk_insert_text_file(records):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "Yash@171",
                                      host = "localhost",
                                      port = "5432",
                                      database = "File Handling")

        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS metadata_of_text_file")
        cursor.execute("""CREATE TABLE metadata_of_text_file(id SERIAL PRIMARY KEY,
                       text_file_name VARCHAR(255),
                       date_of_creation VARCHAR(255),
                       hash_value VARCHAR(255),
                       parse_value TEXT, 
                       text_file_size VARCHAR(255))""")
        # cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

        sql_insert_query ="""INSERT INTO metadata_of_text_file (text_file_name,date_of_creation, hash_value, parse_value, text_file_size) 
                            VALUES(%s, %s, %s, %s, %s)"""
        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into metadata of text files table")

    except(Exception, psycopg2.Error) as error:
        print("Failed inserting record into metadata of text file table {}".format(error))

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)
    finally:
     # closing database connection.
     if connection:
         cursor.close()
         connection.close()
         print("PostgreSQL connection is closed")
