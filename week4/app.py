from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key='secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member')
def login() :
    if session['log'] == True :
        return render_template('success.html')
    else :
        return redirect('/')
    
@app.route('/error')
def error():
    error_message = request.args.get('messages','帳號、或密碼輸入錯誤')
    return render_template('fail.html',messages=error_message)


@app.route('/signin', methods=['POST'])
def signin() :
    account = request.form['account']
    passward = request.form['passward']
    if account == 'test' and passward == 'test' :
        session['log'] = True
        return redirect('/member')
    elif account == '' or passward == '' :
        session['log'] = False
        return redirect('/error?messages=Please enter username and password')
    else :
        session['log'] = False
        return redirect('/error?messages=Username or password is not correct')

@app.route('/logout')
def logout() :
    session['log'] = False
    return redirect('/')



app.run(port=3000)