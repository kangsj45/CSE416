from flask import Flask, render_template, request, redirect, url_for, session
from dictionaries import mwlDict, mwcDict, oxfordDict, etymonlineDict, googleImageDict, googleNewsDict, synonymDict, thefreedictionaryDict, urbanDict, wikiDict, wiktionaryDict, wordnetDict, youtubeDict
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import asyncio
import json


app = Flask(__name__ ,template_folder='../static')
app._static_folder = '../static'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0000'
app.config['MYSQL_DB'] = 'cse416'

mysql = MySQL(app)


@app.route('/')
def search():
    if session.get('loginAccount'):
        loginAccount=session['loginAccount']
    else:
        loginAccount=None
    return render_template("html/search.html", loginAccount=loginAccount)

@app.route('/searchResult/')
def noresult():
    if session.get('loginAccount'):
        loginAccount=session['loginAccount']
    else:
        loginAccount=None
    return render_template("html/searchResult.html", loginAccount=loginAccount)

@app.route('/searchResult/<string:word>')
def searchResult(word):
    if session.get('loginAccount'):
        loginAccount=session['loginAccount']
    else:
        loginAccount=None

    mwl = mwlDict(word)
    mwc = mwcDict(word)
    oxford = oxfordDict(word)
    #etymonline = etymonlineDict(word)
    googleImage = googleImageDict(word)
    googleNews = googleNewsDict(word)
    #synonym = synonymDict(word)
    #thefreedictionary = thefreedictionaryDict(word)
    urban = urbanDict(word)
    wiki = wikiDict(word)
    #wiktionary = wiktionaryDict(word)
    #wordnet = wordnetDict(word)
    youtube = youtubeDict(word)

    return render_template("html/searchResult.html", loginAccount=loginAccount, word = word, mwl = mwl, mwc = mwc, oxford = oxford, googleImage = googleImage, googleNews =googleNews, urban = urban, wiki = wiki, youtube = youtube)

@app.route('/signin', methods =['GET', 'POST'])
def signin():
    return render_template('./html/signin.html')
  

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    return render_template('./html/signup.html')


@app.route('/addUser', methods =['GET', 'POST'])
def addUser():
    email = request.form['email']
    password = request.form['pw']
    name = request.form['name']

    #DB 연결
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM account WHERE email = % s', (email, ))
    account = cursor.fetchone()
    if account:
        msg='already'
    else:     
        isAdmin=False
        delete = "n"
        profilePictureURL=None
        cursor.execute('INSERT INTO account VALUES (%s, %s, %s)', (email, isAdmin, delete))
        cursor.execute('INSERT INTO useraccount VALUES (%s, %s, %s, %s)', (email, password, name, profilePictureURL))
        mysql.connection.commit()
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account WHERE email = % s', (email, ))
        loginAccount = cursor.fetchone()
        session['loginAccount']= loginAccount
        
        msg='ok'
    return msg


@app.route('/getUserByEmailAndPW', methods =['GET', 'POST'])
def getUserByEmailAndPW():
    email = request.form['email']
    password = request.form['pw']
    
    #DB 연결
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
        SELECT * FROM userAccount AS ua
        JOIN account AS a
        ON ua.email = a.email
        WHERE ua.email=%s AND ua.password=%s AND a.del='n'
        ''', (email,password))
    account = cursor.fetchone()

    if account:
        session['loginAccount']=account
        return 'ok'
    else:
        return 'fail'     
   

@app.route('/signout', methods =['GET', 'POST'])
def signout():
    session.pop('loginAccount', None)
    msg = 'ok'
    return msg


@app.route('/dictOrder')
def dictOrder():
    return render_template('./html/changeDictionaryOrder.html')


@app.route('/addDicOrder', methods =['POST'])
def addDicOrder():
    number = request.form['number']
    source = request.form['source']
    email = session['loginAccount']['email']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO HasSourceOrder VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE source = VALUES(source)', (email, number, source))
    mysql.connection.commit()

    return 'ok'


@app.route('/getAllDic', methods =['GET'])
def getAllDic():
    if session.get('loginAccount'):
        email = session['loginAccount']['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM HasSourceOrder WHERE email=%s', (email))
        dic_list = cursor.fetchall()

        return json.dumps(dic_list)
    else:    
        return 'fail'
 

@app.route('/mypage')
def mypage():
    email = session['loginAccount']['email']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM userAccount WHERE email=%s', (email))
    account = cursor.fetchone()

    return render_template('./html/mypage.html', account=account)



@app.route('/addScHis', methods =['POST'])
def addScHis():
    if session.get('loginAccount'):
        email = session['loginAccount']['email']
        word = request.form['word']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO  HasSearchHistory (email,word,regDate) VALUES (%s,%s,SYSDATE())', (email,word))
        mysql.connection.commit()

        return 'ok'
    else:    
        return 'fail'


@app.route('/addImgUrlToUser', methods =['POST'])
def addImgUrlToUser():
    email = session['loginAccount']['email']
    img_url = request.form['img_url']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('UPDATE userAccount SET profilePictureURL=%s WHERE email=%s', (img_url,email))
    mysql.connection.commit()

    return 'ok'


@app.route('/delUser', methods =['POST'])
def delUser():
    email = session['loginAccount']['email']
    session.pop('loginAccount', None)

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("UPDATE account SET del='y' WHERE email=%s", (email))
    mysql.connection.commit()

    return 'ok'    


@app.route('/changePw', methods =['POST'])
def changePw():
    email = session['loginAccount']['email']
    pw = request.form['pw']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("UPDATE userAccount SET password=%s WHERE email=%s", (pw,email))
    mysql.connection.commit()

    return 'ok'


@app.route('/changeName', methods =['POST'])
def changeName():
    email = session['loginAccount']['email']
    name = request.form['name']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("UPDATE userAccount SET name=%s WHERE email=%s", (name,email))
    mysql.connection.commit()

    return 'ok'    


if __name__ == '__main__':
    app.secret_key = '0000'
    app.run(debug=True) 