import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "dcrm",
    passwd = 'Abc@12345',
    auth_plugin='mysql_native_password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE temp")

print("All Done")