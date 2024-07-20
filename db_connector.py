import mysql.connector.pooling

# 연결 풀 설정
db_pool = mysql.connector.pooling.MySQLConnectionPool(
  pool_name = "my_pool",
  pool_size = 5,
  host="localhost",
  user="root",
  password="1004",
  database="todolist_db"
)

def get_connection():
  db = db_pool.get_connection()
  return db