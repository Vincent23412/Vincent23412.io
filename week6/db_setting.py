import pymysql

# 資料庫連線設定
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Vincent1030',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cur:
        sql = '''CREATE DATABASE TEST'''  # 資料庫名稱要大寫
        cur.execute(sql)

    print('成功')

except Exception as e:
    print('失敗:', e)

finally:
    conn.close()
