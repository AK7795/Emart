import os
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from instamojo_wrapper import Instamojo
from flask_session import Session

import sqlite3

API_KEY = "test_4387b23fc264616d0291ee454a7"

AUTH_TOKEN = "test_00e09b762c2b5333325799cc455"

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


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
                    BOOKNAME TEXT,AUTHORNAME TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE TEXT); ''')


listOfTables3 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='ELECTRONICS' ").fetchall()

if listOfTables3!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE ELECTRONICS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PRODUCTNAME TEXT,COMPANY TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE TEXT); ''')


listOfTables4 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='GROCERY' ").fetchall()

if listOfTables4!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE GROCERY(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   ITEMNAME TEXT,DETAILS TEXT,PRICE TEXT,IMAGE TEXT); ''')


listOfTables5 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='HOMEDECOR' ").fetchall()

if listOfTables5!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE HOMEDECOR(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PRODUCTNAME TEXT,DETAILS TEXT,PRICE TEXT,IMAGE TEXT); ''')


listOfTables6 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='MOBILES' ").fetchall()

if listOfTables6!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE MOBILES(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,BRAND TEXT ,DETAILS TEXT,PRICE TEXT,IMAGE TEXT); ''')


listOfTables7 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='ORDERSS' ").fetchall()

if listOfTables7!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE ORDERSS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,EMAIL TEXT ,PHONE INTEGER, ADDRESS TEXT,PINCODE INTEGER, MODEOFPAYMENT TEXT,ITEMORDERED TEXT); ''')


listOfTables8 = con.execute("SELECT NAME FROM sqlite_master WHERE type='table' And name='USERS' ").fetchall()

if listOfTables8!=[]:
    print("Table Already Exists ! ")
else:
    con.execute('''CREATE TABLE USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FIRSTNAME TEXT,LASTNAME TEXT ,MOBILENUMBER TEXT,EMAILID TEXT,PASSWORD TEXT); ''')


app = Flask(__name__)

curo = con.cursor()
curo.execute("SELECT * FROM ORDERSS")
resul = curo.fetchall()
print(resul)

#con.execute("ALTER TABLE ORDERSS ADD COLUMN AMOUNT TEXT")
con.commit()


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

orname=""
con.execute("DELETE FROM ORDERSS WHERE NAME = '"+orname+"'  ")
con.commit()


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

            f2 = request.files['decorpic']
            pic2 = secure_filename(f2.filename)
            f2.save(os.path.join('static', pic2))
            f2.save(pic2)
            print(getName)
            print(getdetails)
            print(getPrice)
            try:
                con.execute(
                    "INSERT INTO HOMEDECOR(PRODUCTNAME,DETAILS,PRICE,IMAGE) VALUES('" + getName + "','" + getdetails + "','" + getPrice + "','"+pic2+"')")
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
            con.commit()
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

            f3 = request.files['mobpic']
            pic3 = secure_filename(f3.filename)
            f3.save(os.path.join('static', pic3))
            f3.save(pic3)

            print(getName)
            print(getBrand)
            print(getdetails)
            print(getPrice)
            try:
                con.execute(
                    "INSERT INTO MOBILES(NAME,BRAND,DETAILS,PRICE,IMAGE) VALUES('" + getName + "','" + getBrand + "','" + getdetails + "','" + getPrice + "','"+pic3+"')")
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
            con.commit()
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

            f4 = request.files['elepic']
            pic4 = secure_filename(f4.filename)
            f4.save(os.path.join('static', pic4))
            f4.save(pic4)

            print(getName)
            print(getComp)
            print(getdetails)
            print(getPrice)

            try:
                con.execute(
                    "INSERT INTO ELECTRONICS(PRODUCTNAME,COMPANY,DETAILS,PRICE,IMAGE) VALUES('" + getName + "','" + getComp + "','" + getdetails + "','" + getPrice + "','"+pic4+"')")
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
            con.commit()
            return redirect("/electronics")
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

            f5 = request.files['gropic']
            pic5 = secure_filename(f5.filename)
            f5.save(os.path.join('static', pic5))
            f5.save(pic5)

            print(getName)
            print(getdetails)
            print(getPrice)

            try:
                con.execute(
                    "INSERT INTO GROCERY(ITEMNAME,DETAILS,PRICE,IMAGE) VALUES('" + getName + "','" + getdetails + "','" + getPrice + "','"+pic5+"')")
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
            con.commit()
            return redirect("/grocery")
        return render_template("delgro.html")


@app.route("/sellerlogin", methods=['GET', 'POST'])
def sellerlogin():
    if request.method == 'POST':
        getemail = request.form['email']
        getpassword = request.form['pass']
        print(getemail)
        print(getpassword)

        cursor.execute("SELECT * FROM SELLER WHERE EMAILID = '" + getemail + "' AND PASSWORD = '" + getpassword + "'  ")
        res2 = cursor.fetchall()
        print(res2)
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
        return redirect("/")
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


@app.route("/searchpage", methods=['POST'])
def search():
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


@app.route("/buygrocery", methods=['GET', 'POST'])
def buygrocery():
    if not session.get("usemail") :
        return redirect("/userlogin")
    else:
        getId = request.args.get('id')
        cur = con.cursor()
        cur.execute("SELECT * FROM GROCERY WHERE ID=" + getId)
        res = cur.fetchall()

        c1 = con.cursor()
        c1.execute("SELECT ITEMNAME,PRICE FROM GROCERY  WHERE ID =" + getId)
        r1 = c1.fetchall()
        print(r1)
        if request.method == "POST":
            getName = request.form["bname"]
            getEmail = request.form["email"]
            getPhone = request.form["phone"]
            getAddress = request.form["add"]
            getPincode = request.form["pin"]
            getModeofpayment = request.form["payment"]

            print(getName)
            print(getEmail)
            print(getPhone)
            print(getAddress)
            print(getPincode)
            print(getModeofpayment)

            con.execute(
                "INSERT INTO ORDERSS(NAME,EMAIL,PHONE,ADDRESS,PINCODE,MODEOFPAYMENT,ITEMORDERED,AMOUNT) VALUES('" + getName + "','" + getEmail + "','" + getPhone + "','" + getAddress + "','" + getPincode + "','" + getModeofpayment + "','" +
                r1[0][0] + "','" + r1[0][1] + "')")
            print("successfully inserted !")
            con.commit()
            if getModeofpayment == "INSTAMOJO":
                return redirect("/payment")

            if getModeofpayment == "COD":
                return redirect("/success")

        return render_template("buygrocery.html", groc1=res)


@app.route("/buymobiles",methods=['GET', 'POST'])
def buymobiles():
    if not session.get("usemail") :
        return redirect("/userlogin")
    else:
        getId = request.args.get('id')
        cur = con.cursor()
        cur.execute("SELECT * FROM MOBILES WHERE ID=" + getId)
        res = cur.fetchall()

        c1 = con.cursor()
        c1.execute("SELECT NAME,PRICE FROM MOBILES  WHERE ID =" + getId)
        r1 = c1.fetchall()
        print(r1[0][0])
        if request.method == "POST":
            getName = request.form["bname"]
            getEmail = request.form["email"]
            getPhone = request.form["phone"]
            getAddress = request.form["add"]
            getPincode = request.form["pin"]
            getModeofpayment = request.form["payment"]

            print(getName)
            print(getEmail)
            print(getPhone)
            print(getAddress)
            print(getPincode)
            print(getModeofpayment)

            con.execute(
                "INSERT INTO ORDERSS(NAME,EMAIL,PHONE,ADDRESS,PINCODE,MODEOFPAYMENT,ITEMORDERED,AMOUNT) VALUES('" + getName + "','" + getEmail + "','" + getPhone + "','" + getAddress + "','" + getPincode + "','" + getModeofpayment + "','" +
                r1[0][0] + "','" + r1[0][1] + "')")
            print("successfully inserted !")
            con.commit()
            if getModeofpayment == "INSTAMOJO":
                return redirect("/payment")

            if getModeofpayment == "COD":
                return redirect("/success")

        return render_template("buymobiles.html", mob1=res)


@app.route("/buyelectronics",methods=['GET', 'POST'])
def buyelectronics():
    if not session.get("usemail") :
        return redirect("/userlogin")
    else:
        getId = request.args.get('id')
        cur = con.cursor()
        cur.execute("SELECT * FROM ELECTRONICS WHERE ID=" + getId)
        res = cur.fetchall()

        c1 = con.cursor()
        c1.execute("SELECT PRODUCTNAME,PRICE FROM ELECTRONICS  WHERE ID =" + getId)
        r1 = c1.fetchall()
        print(r1[0][0])
        if request.method == "POST":
            getName = request.form["bname"]
            getEmail = request.form["email"]
            getPhone = request.form["phone"]
            getAddress = request.form["add"]
            getPincode = request.form["pin"]
            getModeofpayment = request.form["payment"]

            print(getName)
            print(getEmail)
            print(getPhone)
            print(getAddress)
            print(getPincode)
            print(getModeofpayment)

            con.execute(
                "INSERT INTO ORDERSS(NAME,EMAIL,PHONE,ADDRESS,PINCODE,MODEOFPAYMENT,ITEMORDERED,AMOUNT) VALUES('" + getName + "','" + getEmail + "','" + getPhone + "','" + getAddress + "','" + getPincode + "','" + getModeofpayment + "','" +
                r1[0][0] + "'.'" + r1[0][1] + "')")
            print("successfully inserted !")
            con.commit()
            if getModeofpayment == "INSTAMOJO":
                return redirect("/payment")

            if getModeofpayment == "COD":
                return redirect("/success")

        return render_template("buyelectronics.html", elec1=res)


@app.route("/buydecor",methods=['GET', 'POST'])
def buydecor():
    if not session.get("usemail") :
        return redirect("/userlogin")
    else:
        getId = request.args.get('id')
        cur = con.cursor()
        cur.execute("SELECT * FROM HOMEDECOR WHERE ID=" + getId)
        res = cur.fetchall()

        c1 = con.cursor()
        c1.execute("SELECT PRODUCTNAME,PRICE FROM HOMEDECOR  WHERE ID =" + getId)
        r1 = c1.fetchall()
        print(r1[0][0])
        if request.method == "POST":
            getName = request.form["bname"]
            getEmail = request.form["email"]
            getPhone = request.form["phone"]
            getAddress = request.form["add"]
            getPincode = request.form["pin"]
            getModeofpayment = request.form["payment"]

            print(getName)
            print(getEmail)
            print(getPhone)
            print(getAddress)
            print(getPincode)
            print(getModeofpayment)

            con.execute(
                "INSERT INTO ORDERSS(NAME,EMAIL,PHONE,ADDRESS,PINCODE,MODEOFPAYMENT,ITEMORDERED,AMOUNT) VALUES('" + getName + "','" + getEmail + "','" + getPhone + "','" + getAddress + "','" + getPincode + "','" + getModeofpayment + "','" +
                r1[0][0] + "','" + r1[0][1] + "')")
            print("successfully inserted !")
            con.commit()
            if getModeofpayment == "INSTAMOJO":
                return redirect("/payment")

            if getModeofpayment == "COD":
                return redirect("/success")

        return render_template("buydecor.html", decor1=res)


@app.route("/buybooks", methods=['GET', 'POST'])
def buybooks():
    if not session.get("usemail") :
        return redirect("/userlogin")
    else:
        getId = request.args.get('id')
        cur = con.cursor()
        cur.execute("SELECT * FROM BOOKS1 WHERE ID=" + getId)
        res = cur.fetchall()

        c1 = con.cursor()
        c1.execute("SELECT BOOKNAME,PRICE FROM BOOKS1  WHERE ID =" + getId)
        r1 = c1.fetchall()
        print(r1[0][0])
        if request.method == "POST":
            getName = request.form["bname"]
            getEmail = request.form["email"]
            getPhone = request.form["phone"]
            getAddress = request.form["add"]
            getPincode = request.form["pin"]
            getModeofpayment = request.form["payment"]

            print(getName)
            print(getEmail)
            print(getPhone)
            print(getAddress)
            print(getPincode)
            print(getModeofpayment)

            con.execute(
                "INSERT INTO ORDERSS(NAME,EMAIL,PHONE,ADDRESS,PINCODE,MODEOFPAYMENT,ITEMORDERED,AMOUNT) VALUES('" + getName + "','" + getEmail + "','" + getPhone + "','" + getAddress + "','" + getPincode + "','" + getModeofpayment + "','" +
                r1[0][0] + "','" + r1[0][1] + "')")
            print("successfully inserted !")
            con.commit()
            if getModeofpayment == "INSTAMOJO":
                return redirect("/payment")

            if getModeofpayment == "COD":
                return redirect("/success")

        return render_template("buybooks.html", books=res)


@app.route("/sellerorders", methods=["GET","POST"])
def userorder():

    cur = con.cursor()
    cur.execute("SELECT * FROM ORDERSS ")
    res = cur.fetchall()
    print(res)
    return render_template("myorders.html", detail=res)


@app.route("/userorders", methods=["GET","POST"])
def myorder():

    cur = con.cursor()
    cur.execute("SELECT * FROM ORDERSS ")
    res = cur.fetchall()
    print(res)
    return render_template("userorder.html", detail=res)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == "POST":
        getname = request.form["name"]
        getpass = request.form["pass"]
        if getname == "admin":
            if getpass == "1234":
                return redirect("/adminpage")
    return render_template("adminlogin.html")


@app.route("/adminpage")
def adminpage():
    return render_template("adminpage.html")


@app.route("/adminorder")
def vieworders():
    cur = con.cursor()
    cur.execute("SELECT * FROM ORDERSS")
    res2 = cur.fetchall()
    print(res2)
    return render_template("adminorder.html", orders=res2)


@app.route("/sellers")
def sellers():
    cur = con.cursor()
    cur.execute("SELECT * FROM SELLER")
    res2 = cur.fetchall()
    print(res2)
    return render_template("sellers.html", seller=res2)


@app.route("/users")
def adminviewusers():
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    res = cur.fetchall()
    return render_template("allusers.html", us=res)


@app.route("/delsel", methods=["GET","POST"])
def delseller():
    if request.method == "POST":
        getemailid = request.form["email"]
        cur3 = con.cursor()
        cur3.execute("DELETE FROM SELLER WHERE EMAILID = '" + getemailid + "' ")
        con.commit()
        return redirect("/sellers")
    return render_template("delsel.html")


@app.route("/deluser", methods=["GET","POST"])
def deluser():
    if request.method == "POST":
        getemailid = request.form["email"]
        cur3 = con.cursor()
        cur3.execute("DELETE FROM USERS WHERE EMAILID = '" + getemailid + "' ")
        con.commit()
        return redirect("/users")
    return render_template("deluser.html")


@app.route("/userlogin", methods=['GET', 'POST'])
def uslogin():
    if request.method == 'POST':
        getemail = request.form['email']
        getpassword = request.form['pass']
        print(getemail)
        print(getpassword)

        cursor.execute("SELECT * FROM USERS WHERE EMAILID = '" + getemail + "' AND PASSWORD = '" + getpassword + "'  ")
        res2 = cursor.fetchall()
        print(res2)
        if len(res2) > 0:
            for i in res2:
                getusid = i[0]
                getusName = i[1]
                getusnum = i[3]
                getusemail = i[4]

            print(getemail)
            session["usname"] = getusName
            session["usid"] = getusid
            session["usnum"] = getusnum
            session["usemail"] = getusemail

            return redirect("/userpage")

    return render_template("userlogin.html")


@app.route("/userlogout")
def uslogout():

    if not session.get("usemail"):
        return redirect("/")
    else:
        session["usname"] = None
        session["usemail"] = None
        session["usnum"] = None
        return redirect("/")


@app.route("/userpage")
def userpage():
    if not session.get("usemail"):
        return redirect("/userlogin")
    else:
        return render_template("user.html")


@app.route("/editprofile", methods=['GET', 'POST'])
def editprofile():
    if not session.get("usemail"):
        return redirect("/userlogin")
    else:
        if request.method == 'POST':
            getfirstname = request.form['firstname']
            getlastname = request.form['lastname']
            getemail = request.form['email']
            getmobile = request.form['mobile']
            getpassword = request.form['password']

            print(getfirstname)
            print(getlastname)
            print(getmobile)
            print(getemail)
            print(getpassword)

            cursor.execute(
                "UPDATE  USERS SET FIRSTNAME = '" + getfirstname + "',LASTNAME = '" + getlastname + "', MOBILENUMBER = '" + getmobile + "', EMAILID = '" + getemail + "',PASSWORD = '" + getpassword + "'      WHERE FIRSTNAME = '"+session["usname"]+"'  ")
            con.commit()
            return redirect("/")

        return render_template("editprofile.html")


@app.route("/userrregistration", methods=['GET', 'POST'])
def userreg():
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

        cursor.execute("INSERT INTO USERS(FIRSTNAME,LASTNAME,MOBILENUMBER,EMAILID,PASSWORD)VALUES('"+getfirstname+"','"+getlastname+"','"+getmobile+"','"+getemail+"','"+getpassword+"')")
        con.commit()
        return redirect("/userlogin")

    return render_template("userreg.html")


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if not session.get("usemail"):
        return redirect("/userlogin")
    else:
        cur = con.cursor()
        cur.execute("SELECT * FROM ORDERSS WHERE EMAIL = '" + session["usemail"] + "' ")
        res = cur.fetchall()
        print(res)
        return render_template("payment.html", detail=res)


        return render_template("payment.html")


@app.route('/pay', methods=["GET", "POST"])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        product = request.form.get('product')
        email = request.form.get('email')
        amount = request.form.get('amount')

        response = api.payment_request_create(
            amount=amount,
            purpose=product,
            buyer_name=name,
            send_email=True,
            email=email,
            redirect_url="http://localhost:5000/success")
        return redirect(response['payment_request']['longurl'])


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
