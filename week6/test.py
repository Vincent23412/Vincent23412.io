import pymysql

# 建立資料庫連線
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Vincent1030',
    database='customer',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    # 執行插入操作
    with conn.cursor() as cur:
        sql_insert = '''INSERT INTO user_data(name, account, password) VALUES (%s, %s, %s);'''
        cur.execute(sql_insert, ("ff", "f", "f"))
        conn.commit()  # 提交變更

    # 執行查詢操作來檢查資料是否已經成功插入
    with conn.cursor() as cur:
        sql_query = '''SELECT * FROM user_data WHERE name = %s;'''
        cur.execute(sql_query, ("ff",))
        result = cur.fetchone()

        if result:
            print("資料已成功插入：", result)
        else:
            print("資料插入失敗或資料不存在。")

except Exception as e:
    print("操作失敗：", e)

finally:
    conn.close()  # 關閉資料庫連線
