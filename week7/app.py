from flask import Flask,jsonify
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import pymysql
import json
app = Flask(__name__)
app.secret_key='secret'


def load_config(file_path) :
    with open(file_path,"r") as file :
        config = json.load(file)
    return config
db_config = load_config('config.json')['config']

print(db_config['host'],db_config['user'],db_config['password'])

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
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
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
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
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
            session['account'] = account
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
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
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
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
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
        print(e)
        return redirect('/error?messages=未知錯誤')

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
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
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
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
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
    
####查詢和更新用帳號
#查詢會員
@app.route('/api/member')
def search() :
    account = request.args.get('account')
    conn = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database='customer',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )
    try :
        sql = '''SELECT id,name FROM member WHERE account = %s'''
        data = (account)
        with conn.cursor() as cur :
            cur.execute(sql, data)
            result = cur.fetchone()
            print(result)
            return jsonify({"data":result})

    except Exception as e:
        print(e)
        return redirect('/error?messages=未知錯誤')
    
@app.route('/api/member',methods=['PATCH'])
def update_member():
    try:
        # 解析 JSON 格式的 Request Body
        request_data = request.json
        new_name = request_data.get('name')
        account = session.get('account','unknown')
        conn = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database='customer',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
        sql = '''UPDATE member SET name = %s WHERE account = %s'''
        with conn.cursor() as cur:
            cur.execute(sql, (new_name, account))  
            conn.commit()  # 提交變更
        
        # 成功更新時回傳成功的 JSON 回應
        response_data = {"ok": True}
        return jsonify(response_data)

    except Exception as e:
        # 更新失敗時回傳錯誤的 JSON 回應
        response_data = {"error": True}
        return jsonify(response_data)


# http://127.0.0.1:3000//api/member?username=a

app.run(port=3000,debug=True)




