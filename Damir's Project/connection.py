import cx_Oracle

connection = cx_Oracle.connect("damir/password@localhost:1522/orcl")

cursor = connection.cursor()

print("Succesfully connected to ORCL db: ")