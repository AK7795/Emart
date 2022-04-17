import os
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename

from flask_session import Session

import sqlite3

con = sqlite3.connect("Login.db", check_same_thread=False)
cursor = con.cursor()


listOfTables = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='SELLER' ").fetchall()

if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE SELLER(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    FIRSTNAME TEXT,LASTNAME TEXT ,MOBILENUMBER TEXT,EMAILID TEXT,PASSWORD TEXT); ''')


listOfTables2 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='BOOKS1' ").fetchall()

if listOfTables2!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE BOOKS1(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    BOOKNAME TEXT,AUTHORNAME TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE BLOB); ''')


listOfTables3 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='ELECTRONICS' ").fetchall()

if listOfTables3!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE ELECTRONICS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PRODUCTNAME TEXT,COMPANY TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE BLOB); ''')


listOfTables4 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='GROCERY' ").fetchall()

if listOfTables4!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE GROCERY(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   ITEMNAME TEXT,DETAILS TEXT,PRICE TEXT,IMAGE BLOB); ''')


listOfTables5 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='HOMEDECOR' ").fetchall()

if listOfTables5!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE HOMEDECOR(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PRODUCTNAME TEXT,DETAILS TEXT,PRICE TEXT,IMAGE BLOB); ''')


listOfTables6 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='MOBILES' ").fetchall()

if listOfTables6!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE MOBILES(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,BRAND TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE BLOB); ''')


app = Flask(__name__)

curo = con.cursor()
curo.execute("SELECT EMAILID,PASSWORD FROM SELLER")
resul = curo.fetchall()
print(resul)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def dash():
    return render_template("home.html")


@app.route("/sellerpage")
def seller():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        return render_template("sellerpage.html")


@app.route("/addbooks", methods=['GET', 'POST'])
def addbook():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getBookName = request.form["name"]
            getAuthor = request.form["author"]
            getdetails = request.form["cat"]
            getPrice = request.form["price"]

            f1 = request.files['bookpic']
            pic = secure_filename(f1.filename)
            f1.save(os.path.join('static', pic))
            f1.save(pic)

            print(getBookName)
            print(getAuthor)
            print(getdetails)
            print(getPrice)
            try:
                con.execute(
                    "INSERT INTO BOOKS1(BOOKNAME,AUTHORNAME,DETAILS,PRICE,IMAGE) VALUES('" + getBookName + "','" + getAuthor + "','" + getdetails + "','" + getPrice + "','"+pic+"')")
                print("successfully inserted !")
                con.commit()
                return redirect("/books")
            except Exception as e:
                print(e)
        return render_template("addbooks.html")


@app.route("/delbooks", methods=["GET", "POST"])
def delbooks():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getNAMEDEL = request.form["namedel"]
            cur3 = con.cursor()
            cur3.execute("DELETE FROM BOOKS1 WHERE BOOKNAME = '" + getNAMEDEL + "'   ")
            con.commit()
            return redirect("/books")
        return render_template("delbooks.html")


@app.route("/adddecor", methods=['GET', 'POST'])
def adddecor():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getName = request.form["name"]
            getdetails = request.form["det"]
            getPrice = request.form["price"]

            print(getName)
            print(getdetails)
            print(getPrice)
            try:
                con.execute(
                    "INSERT INTO HOMEDECOR(PRODUCTNAME,DETAILS,PRICE) VALUES('" + getName + "','" + getdetails + "','" + getPrice + "')")
                print("successfully inserted !")
                con.commit()
                return redirect("/decorate")
            except Exception as e:
                print(e)
        return render_template("adddecor.html")


@app.route("/deldecor", methods=["GET", "POST"])
def deldecor():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getNAMEDEL = request.form["namedel"]
            cur3 = con.cursor()
            cur3.execute("DELETE FROM HOMEDECOR WHERE PRODUCTNAME = '" + getNAMEDEL + "' ")
            return redirect("/decorate")
        return render_template("deldecor.html")


@app.route("/addmob", methods=['GET', 'POST'])
def addmob():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getName = request.form["name"]
            getBrand = request.form["brand"]
            getdetails = request.form["det"]
            getPrice = request.form["price"]

            print(getName)
            print(getBrand)
            print(getdetails)
            print(getPrice)
            try:
                con.execute(
                    "INSERT INTO MOBILES(NAME,BRAND,DETAILS,PRICE) VALUES('" + getName + "','" + getBrand + "','" + getdetails + "','" + getPrice + "')")
                print("successfully inserted !")
                con.commit()
                return redirect("/mobiles")
            except Exception as e:
                print(e)
        return render_template("addmob.html")


@app.route("/delmob", methods=["GET", "POST"])
def delmob():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getNAMEDEL = request.form["namedel"]
            cur3 = con.cursor()
            cur3.execute("DELETE FROM MOBILES WHERE NAME = '" + getNAMEDEL + "' ")
            return redirect("/mobiles")
        return render_template("delmob.html")


@app.route("/addele", methods=['GET', 'POST'])
def addele():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getName = request.form["name"]
            getComp = request.form["comp"]
            getdetails = request.form["det"]
            getPrice = request.form["price"]

            print(getName)
            print(getComp)
            print(getdetails)
            print(getPrice)

            try:
                con.execute(
                    "INSERT INTO ELECTRONICS(PRODUCTNAME,COMPANY,DETAILS,PRICE) VALUES('" + getName + "','" + getComp + "','" + getdetails + "','" + getPrice + "')")
                print("successfully inserted !")
                con.commit()
                return redirect("/electronics")
            except Exception as e:
                print(e)
        return render_template("addele.html")


@app.route("/delele", methods=["GET", "POST"])
def delele():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getNAMEDEL = request.form["namedel"]
            cur3 = con.cursor()
            cur3.execute("DELETE FROM ELECTRONICS WHERE PRODUCTNAME = '" + getNAMEDEL + "' ")
            return redirect("/mobiles")
        return render_template("delele.html")


@app.route("/addgro", methods=['GET', 'POST'])
def addgro():
    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        if request.method == "POST":
            getName = request.form["name"]
            getdetails = request.form["det"]
            getPrice = request.form["price"]

            print(getName)
            print(getdetails)
            print(getPrice)

            try:
                con.execute(
                    "INSERT INTO GROCERY(ITEMNAME,DETAILS,PRICE) VALUES('" + getName + "','" + getdetails + "','" + getPrice + "')")
                print("successfully inserted !")
                con.commit()
                return redirect("/grocery")
            except Exception as e:
                print(e)
        return render_template("addgro.html")


@app.route("/delgro", methods=["GET", "POST"])
def delgro():
    if not session.get("name"):
        return redirect("/userlogin")
    else:
        if request.method == "POST":
            getNAMEDEL = request.form["namedel"]
            cur3 = con.cursor()
            cur3.execute("DELETE FROM GROCERY WHERE ITEMNAME = '" + getNAMEDEL + "' ")
            return redirect("/grocery")
        return render_template("delgro.html")


@app.route("/sellerlogin", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        getemail = request.form['email']
        getpassword = request.form['pass']
        print(getemail)
        print(getpassword)

        cursor.execute("SELECT * FROM SELLER WHERE EMAILID = '" + getemail + "' AND PASSWORD = '" + getpassword + "'  ")
        res2 = cursor.fetchall()
        if len(res2) > 0:
            for i in res2:
                getName = i[1]
                getid = i[0]

            session["name"] = getName
            session["id"] = getid
            return redirect("/sellerpage")
    return render_template("login.html")


@app.route("/sellerregistration", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        getfirstname = request.form['firstname']
        getlastname = request.form['lastname']
        getemail = request.form['email']
        getmobile= request.form['mobile']
        getpassword = request.form['password']

        print(getfirstname)
        print(getlastname)
        print(getmobile)
        print(getemail)
        print(getpassword)

        cursor.execute("INSERT INTO SELLER(FIRSTNAME,LASTNAME,MOBILENUMBER,EMAILID,PASSWORD)VALUES('"+getfirstname+"','"+getlastname+"','"+getmobile+"','"+getemail+"','"+getpassword+"')")
        con.commit()
        return redirect("/sellerlogin")

    return render_template("registration.html")


@app.route("/logout")
def logout():

    if not session.get("name"):
        return redirect("/sellerlogin")
    else:
        session["name"] = None
        return redirect("/")


@app.route("/grocery")
def grocery():
    cur = con.cursor()
    cur.execute("SELECT * FROM GROCERY")
    res = cur.fetchall()
    return render_template("grocery.html", groc1=res)


@app.route("/mobiles")
def mob():
    cur = con.cursor()
    cur.execute("SELECT * FROM MOBILES")
    res = cur.fetchall()
    return render_template("mobiles.html", mob1=res)


@app.route("/electronics")
def elect():
    cur = con.cursor()
    cur.execute("SELECT * FROM ELECTRONICS")
    res = cur.fetchall()
    return render_template("electronics.html", elec1=res)


@app.route("/decorate")
def decor():
    cur = con.cursor()
    cur.execute("SELECT * FROM HOMEDECOR")
    res = cur.fetchall()
    return render_template("decorate.html", decor1=res)


@app.route("/books")
def books():
    cur = con.cursor()
    cur.execute("SELECT * FROM BOOKS1")
    res = cur.fetchall()
    return render_template("books.html", books=res)


@app.route("/singleproductgro")
def singleproductgro():
    getId = request.args.get('id')
    cur = con.cursor()
    cur.execute("SELECT * FROM GROCERY WHERE ID ="+getId)
    res = cur.fetchall()
    return render_template("viewsingleproductgro.html", groc1=res)


@app.route("/singleproductmob")
def singleproductmob():
    getID = request.args.get('id')
    cur = con.cursor()
    cur.execute("SELECT * FROM MOBILES WHERE ID="+getID)
    res = cur.fetchall()
    return render_template("viewsingleproductmob.html", mob1=res)


@app.route("/singleproductele")
def singleproductele():
    getID = request.args.get('id')
    cur = con.cursor()
    cur.execute("SELECT * FROM ELECTRONICS WHERE ID="+getID)
    res = cur.fetchall()
    return render_template("viewsingleproductele.html", elec1=res)


@app.route("/singleproductdecor")
def singleproductdecor():
    getID = request.args.get('id')
    cur = con.cursor()
    cur.execute("SELECT * FROM HOMEDECOR WHERE ID=" +getID)
    res = cur.fetchall()
    return render_template("viewsingleproductdecor.html", decor1=res)


@app.route("/singleproductbooks")
def singleproductbooks():
    getID = request.args.get('id')
    cur = con.cursor()
    cur.execute("SELECT * FROM BOOKS1 WHERE ID="+getID)
    res = cur.fetchall()
    return render_template("viewsingleproductbooks.html", books=res)


@app.route("/searchpage", methods=['POST'])
def searchbook():
    if request.method == 'POST':
        sear = request.form['searchproduct']

        cur = con.cursor()
        cur.execute("SELECT * FROM BOOKS1 WHERE BOOKNAME LIKE  '%"+sear+"%'  ")
        res1 = cur.fetchall()

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM GROCERY WHERE ITEMNAME LIKE  '%" + sear + "%'  ")
        res2 = cur2.fetchall()

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM HOMEDECOR WHERE PRODUCTNAME LIKE  '%" + sear + "%'  ")
        res3 = cur3.fetchall()

        cur4 = con.cursor()
        cur4.execute("SELECT * FROM ELECTRONICS WHERE PRODUCTNAME LIKE  '%" + sear + "%'  ")
        res4 = cur4.fetchall()

        cur5 = con.cursor()
        cur5.execute("SELECT * FROM MOBILES WHERE NAME LIKE  '%" + sear + "%'  ")
        res5 = cur5.fetchall()

        print(res1)
        print(res2)
        if len(res1) > 0:
            return render_template("searchbook.html", searchbook=res1)

        if len(res2) > 0:
            return render_template("searchgro.html", searchgro=res2)

        if len(res5) > 0:
            return render_template("searchmob.html", searchmob=res5)

        if len(res4) > 0:
            return render_template("searchele.html", searchele=res4)

        if len(res3) > 0:
            return render_template("searchdecor.html", searchdecor=res3)


if __name__ == "__main__":
    app.run(debug=True)