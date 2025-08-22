from flask import *
import pymysql


app.route("/api/READ",methods=["GET"])
def signin():
    if request.method=="GET":
        email=request.form["email"]
        password=request.form["password"]
        # print("The inserted email and password are:",(email,password))  

        #create a connection to the database
        connection=pymysql.connect(host="localhost",user="root",database="sokogarden",password="")

        #create cursor
        cursor=connection.cursor(pymysql.cursors.DictCursor)

        return jsonify({"mESSAGE":"eNTER YOUR CREDENTIALS"})

        # structure an sql for login in

        # sql="SELECT * FROM `users` WHERE email=%s and password=%s"

        # # create a tuple
        # data=(email,password)

        # #use cursor to execute to replace placeholders with actual data

        # cursor.execute(sql,data)

        # #check whether there is a user being returned based on the inserted email and password
        # # if there is a user are more than one
        # # if there is no ,user the number of rows are zero

        # if cursor.rowcount==0:
        #     return({"Message":'Login failed please try again...'})
        # else:
        #     #when detauils are correct,create a variable to mstore details of user in variable
        #     # then return a success message
        #     user=cursor.fetchone()

        #     return jsonify({"message":"Login succesful","user":user})

         



#run web app
app.run(debug=True)