import pymysql

host = 'advpy-finalproject-02.clihicjrcxdy.us-east-1.rds.amazonaws.com'
port = 3306
dbname = 'productdb'
user = 'admin'
password = 'admin.123'

conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname, connect_timeout=10)
cur = conn.cursor()
cur.execute("""SELECT now()""")
query_results = cur.fetchall()
print(query_results)

print('-----Complete-----')
