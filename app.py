from flask import Flask, render_template, request, redirect

import sqlite3




app = Flask(__name__)
conn = sqlite3.connect('database.sqlite', check_same_thread=False)  # database connection
cursor = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()


@app.route("/")
def main():
    return render_template("signup.html")


@app.route("/logup")
def logup():
    return render_template("login.html")


@app.route("/saveuser", methods=['POST'])
def saveuserdata():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('pass')
    re_password = request.form.get('repeat-pass')

    if password == re_password:
        cursor.execute(
            """INSERT INTO `user` (`fullname`,`email`,`username`,`password`) VALUES ('{}','{}','{}',
            '{}')""".format(fullname, email, username, password))
        conn.commit()
        return render_template("login.html")
    else:
        return "error"


@app.route("/login", methods=['POST'])
def signinvalidation():
    username = request.form.get('username')
    password = request.form.get('pass')

    cursor.execute(
        """SELECT * FROM user WHERE username LIKE '{}' AND password LIKE '{}'""".format(username, password))
    users = cursor.fetchall()
    msg = "Account doesn't exist"

    if len(users) > 0:
        return render_template("index.html")
    else:
        return render_template("login.html", msg=msg)


@app.route("/Rent")
def rentbook():
    cursor.execute(
        """SELECT `bookid`  FROM `books` """)
    data = cursor.fetchall()
    cursor1.execute(
        """SELECT `book_name`  FROM `books` """)
    data1 = cursor1.fetchall()
    cursor2.execute(
        """SELECT `author_name`  FROM `books` """)
    data2 = cursor2.fetchall()
    

    return render_template("rent.html",data=data,data1=data1,data2=data2)


@app.route("/success",methods=['POST'])
def success():
    return render_template("success.html")

@app.route("/return",methods=['POST'])
def ret():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
