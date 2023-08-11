from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import pymysql
app = Flask(__name__)
app.secret_key='secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member')
def login() :
    name = request.args.get('member')
    if session['log'] == True :
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=密碼,
            database='customer',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = f'''SELECT name,content FROM message'''
        with conn.cursor() as cur :
            cur.execute(sql)
            data = cur.fetchall()
        print(data)
        return render_template('success.html',member=name,messages=data)
    else :
        return redirect('/')
    
@app.route('/error')
def error():
    error_message = request.args.get('messages','帳號、或密碼輸入錯誤')
    return render_template('fail.html',messages=error_message)


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
        sql = f'''SELECT name FROM user_data WHERE account="{account}" and password="{password}"'''
        with conn.cursor() as cur :
            cur.execute(sql)
            name =  cur.fetchall()[0]['name']
            session['log'] = True
            session['username'] = name
            return redirect(f"/member?member={name}")
    except :
        session['log'] = False
        return redirect('/error?messages=Username or password is not correct')



@app.route('/signup', methods=['POST'])
def signup() :
    name = request.form['name']
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
        sql = f'''INSERT INTO user_data(name,account,password) values("{name}","{account}","{password}");'''
        with conn.cursor() as cur :
            cur.execute(sql)
            conn.commit()  # 提交變更
            return redirect('/')
    except Exception as e:
        return redirect('/error?messages=帳號已被註冊')

@app.route('/signout')
def logout() :
    session['log'] = False
    return redirect('/')

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
        username = session.get('username', 'unknown')
        sql = f'''INSERT INTO message(name,content) values("{username}","{content}");'''
        with conn.cursor() as cur :
            cur.execute(sql)
            conn.commit()  # 提交變更
            return redirect(request.referrer)
    except Exception as e:
        return redirect('/error?messages=未知錯誤')

@app.route('/deleteMessage')
def delete() :
    name = request.args.get('name')
    content = request.args.get('content')
    conn = pymysql.connect(
        user='root',
        password='Vincent1030',
        database='customer',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try :
        sql = f'''DELETE FROM message WHERE name='{name}' AND content='{content}';'''
        print(sql)
        with conn.cursor() as cur :
            cur.execute(sql)
            conn.commit()  # 提交變更
            return redirect(request.referrer)
    except Exception as e:
        print(e)
        return redirect('/error?messages=未知錯誤')

app.run(port=3000,debug=True)






