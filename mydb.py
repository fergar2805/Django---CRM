import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

dataBase = mysql.connector.connect(
    host = os.getenv('DATABASE_HOST'),
    user = os.getenv('DATABASE_USER'),
    passwd = os.getenv('DATABASE_PASSWORD')
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE " + os.getenv('DATABASE_NAME'))
print("All Done!")
