from flask import *
import sqlite3
import os
import base64
import secrets
import threading

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

command = """CREATE TABLE IF NOT EXISTS sensors(time TEXT, voltage TEXT, current TEXT, temp TEXT, humidity TEXT, Ac_voltage TEXT)"""
cursor.execute(command)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def GetData():
    while True:
        from database import Read_Data
        Read_Data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchone()

        if result:
            session['name'] = name
            cursor.execute("select * from sensors")
            result = cursor.fetchall()
            if result:
                return render_template('userlog.html', Data = result[-1][1:])
            else:
                return render_template('userlog.html', Data=[0,0,0,0,0])
        else:
            return render_template('signin.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('signin.html', msg='Successfully Registered')
    
    return render_template('signup.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        data = request.form
        values = []
        keys = []
        for key in data:
            keys.append(key)
            values.append(float(data[key]))

        print(keys, values)

        import pickle
        model=pickle.load(open("new_rf.pkl","rb"))
        out=model.predict([values])[0]
        charge_time=out[0]//60
        rull=out[1]
        print(out)
        cursor.execute("select * from sensors")
        result = cursor.fetchall()
        if result:
            return render_template('userlog.html', Data = result[-1][1:], result=out,ct=charge_time,rull=rull)
        else:
            return render_template('userlog.html', Data=[0,0,0,0,0,0,0], result=out,ct=charge_time,rull=rull)

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("select * from sensors")
    result = cursor.fetchall()
    if result:
        return render_template('userlog.html', Data = result[-1][1:])
    else:
        return render_template('userlog.html', Data=[0,0,0,0,0,0,0])

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')



@app.route('/enginetemp')
def enginetemp():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()

    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[1])))
        except:
            continue

    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/voltage')
def voltage():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()
    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[2])))
        except:
            continue
    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/current')
def current():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()

    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[3])))
        except:
            continue

    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/temp')
def temp():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()
    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[4])))
        except:
            continue
    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/smoke')
def smoke():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()

    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[5])))
        except:
            continue

    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/vibration')
def vibration():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()

    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[6])))
        except:
            continue

    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/oillevel')
def oillevel():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    labels1 = []
    data1 = []
    cursor.execute('select * from sensors')
    result = cursor.fetchall()

    for i in result:
        try:
            labels1.append(i[0])
            data1.append(int(float(i[7])))
        except:
            continue

    if len(data1) < 10:
        return jsonify([labels1, data1])
    else:
        return jsonify([labels1[-10:], data1[-10:]])

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    thread1 = threading.Thread(target=GetData)
    thread1.start()
    app.run(debug=True)
