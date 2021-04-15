import mysql.connector

try:
    conn=mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="tejas1004", 
            auth_plugin="mysql_native_password",
            database="PasswordManager")

    if conn.is_connected():
        cursor=conn.cursor()

        cursor.execute('''CREATE TABLE Details (
                DESCRIPTION_ VARCHAR(256), 
                USERNAME_ VARCHAR(64),
                PASSWORD_ VARCHAR(64),
                SECURITY_ANSWER VARCHAR(128));''')
        conn.commit()

except:
    print("DataBase Already Exists or MySQL Connection Failed.")
    exit()
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL Connection Terminated.")
