from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import pymysql
app = Flask(__name__)
app.secret_key='secret'

#主畫面
@app.route('/')
def index():
    return render_template('index.html')

#登入頁面
@app.route('/member')
def login() :
    name = session.get('username','unknown')
    if session['log'] == True :
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = f'''SELECT name,content FROM message JOIN member on message.member_id = member.id;'''
        with conn.cursor() as cur :
            cur.execute(sql)
            data = cur.fetchall()
        return render_template('success.html',member=name,messages=data)
    else :
        return redirect('/')
    
#失敗
@app.route('/error')
def error():
    error_message = request.args.get('messages','帳號、或密碼輸入錯誤')
    return render_template('fail.html',messages=error_message)

#確認登入
@app.route('/signin', methods=['POST'])
def signin() :
    account = request.form['account']
    password = request.form['passward']
    try :
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = '''SELECT name,id FROM member WHERE account= %s and password= %s;'''
        data = (account, password)
       
        with conn.cursor() as cur :
            cur.execute(sql,data)
            profile = cur.fetchall()[0]
            name =  profile['name']
            id = profile['id']
            session['log'] = True
            session['username'] = name
            session['member_id'] = id
            return redirect(f"/member")
    except Exception as e:
        session['log'] = False
        print(e)
        return redirect('/error?messages=Username or password is not correct')


#註冊
@app.route('/signup', methods=['POST'])
def signup() :
    name = request.form['name']
    account = request.form['account']
    password = request.form['passward']
    #確認帳號有無重複
    try :
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = '''SELECT COUNT(*) FROM member WHERE name = %s;'''
        data = (name,)
        with conn.cursor() as cur :
            cur.execute(sql,data)
            num = cur.fetchall()[0]["COUNT(*)"]
        if num > 1 :
            return redirect('/error?messages=帳號已被註冊')
    #新增帳號
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = '''INSERT INTO member(name,account,password) values(%s,%s,%s);'''
        data = (name,account,password)
        with conn.cursor() as cur :
            cur.execute(sql,data)
            conn.commit()  # 提交變更
            return redirect('/')
    except Exception as e:
        return redirect('/error?messages=帳號已被註冊')

#登出
@app.route('/signout')
def logout() :
    session['log'] = False
    return redirect('/')


#留言
@app.route('/createMessage')
def update() :
    content = request.args.get('content')
    try :
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        member_id = session.get('member_id', 'unknown')
        sql = '''INSERT INTO message(member_id,content) values(%s,%s);'''
        data = (member_id,content)
        with conn.cursor() as cur :
            cur.execute(sql,data)
            conn.commit()  # 提交變更
            return redirect(request.referrer)
    except Exception as e:
        print(e)
        return redirect('/error?messages=未知錯誤')
    
#刪除留言
@app.route('/deleteMessage')
def delete() :
    name = request.args.get('name')
    content = request.args.get('content')
    conn = pymysql.connect(
        user='root',
        password="Vincent1030",
        database='customer',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try :
        
        sql = '''DELETE FROM message WHERE content=%s AND member_id = (SELECT id FROM member where name = %s);'''
        data = (content,name)
        with conn.cursor() as cur :
            cur.execute(sql,data)
            conn.commit()  # 提交變更
            return redirect(request.referrer)
    except Exception as e:
        print(e)
        return redirect('/error?messages=未知錯誤')

app.run(port=3000,debug=True)
