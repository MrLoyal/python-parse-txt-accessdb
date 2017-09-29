import pyodbc

db_file = r'''./mydb.accdb'''
user = ''
password = ''

#odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
#                (db_file, user, password)
# Or, for newer versions of the Access drivers:
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %(db_file, user, password)
#print(odbc_conn_str)

conn = pyodbc.connect(odbc_conn_str)
cur = conn.cursor() 

with open("input.txt") as f:
	print(f)
	for line in f:
		print(line)
		vals = line.split(",")
		sql = "insert into Table1([FieldA], [Field2], [Field3]) values ('%s', '%s', '%s')" %(vals[0], vals[1], vals[2])
		print(sql)
		cur.execute(sql)
		conn.commit()


sql = "select * from %s" % "Table1"
cur.execute(sql)

# show the result
result = cur.fetchall()
for item in result:
    print item


print(conn)
conn.close()
