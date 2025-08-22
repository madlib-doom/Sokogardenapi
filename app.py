from flask import *
import os
#import pymysql library that will enable you to create a connection between vscode and db
import pymysql
import pymysql.cursors

#create a web app
app=Flask(__name__)
# configure upload folder where images will be stored
app.config['UPLOAD_FOLDER']='static/images'

#Below is the sign up route(Registration)
@app.route("/api/signup",methods=["POST"])
def signup():
    if request.method=="POST":
            #extarct the different details entered on the form
            username=request.form["username"]
            password=request.form["password"]
            email=request.form["email"]
            phone=request.form["phone"]
            # print("The inserted details are",(username,password,email,phone))
            # create/establish a connection to the database 

            connection= pymysql.connect(host="localhost",user="root",password="",database="sokogarden")

            #create aa cursor
            cursor=connection.cursor()

            #structure an sql query to insert data into the table

            sql="INSERT INTO `users`( `user_name`, `password`, `email`, `phone`) VALUES (%s,%s,%s,%s)"
            #Put data into a tuple
            data=(username,password,email,phone)

            #use cursor to execute sql as you replace placeholders with actual data
            cursor.execute(sql,data)

            #commit changes into database
            connection.commit()

            return jsonify({"message":"Users registered succcesfully"})


@app.route("/api/signin",methods=["POST"])
def signin():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        # print("The inserted email and password are:",(email,password))  

        #create a connection to the database
        connection=pymysql.connect(host="localhost",user="root",database="sokogarden",password="")

        #create cursor
        cursor=connection.cursor(pymysql.cursors.DictCursor)

        # structure an sql for login in

        sql="SELECT * FROM `users` WHERE email=%s and password=%s"

        # create a tuple
        data=(email,password)

        #use cursor to execute to replace placeholders with actual data

        cursor.execute(sql,data)

        #check whether there is a user being returned based on the inserted email and password
        # if there is a user are more than one
        # if there is no ,user the number of rows are zero

        if cursor.rowcount==0:
            return({"Message":'Login failed please try again...'})
        else:
            #when detauils are correct,create a variable to mstore details of user in variable
            # then return a success message
            user=cursor.fetchone()

            return jsonify({"message":"Login succesful","user":user})

         
@app.route("/api/addproduct",methods=["POST"])
def addproduct():
     if request.method=="POST":
          #extract details from keys on form and store into variables
          product_name=request.form["product_name"]
          product_description=request.form["product_description"]
          product_cost=request.form["product_cost"]

        #   the product photo shall be requested from the file system

          product_photo=request.files["product_photo"]

        #   extract filename for photo

          filename=product_photo.filename
        #   by use of os(operating system library) take path of photo
          photo_path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
# Save your photo on that particular path
          product_photo.save(photo_path)
        #   print("The details are:",(product_name,product_description,product_cost,photo_path))
        
          connection= pymysql.connect(host="localhost",user="root",password="",database="sokogarden")

            #create aa cursor
          cursor=connection.cursor()

            #structure an sql query to insert data into the table

          sql="INSERT INTO `product_details`( `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES (%s,%s,%s,%s)"
            #Put data into a tuple
          data=(product_name,product_description,product_cost,filename)

            #use cursor to execute sql as you replace placeholders with actual data
          cursor.execute(sql,data)

            #commit changes into database
          connection.commit()

          return jsonify({'message':"product added succesfully"})


@app.route("/api/getproducts",methods=["GET"])
def getProducts():
     product_name=request.form

  #establish a connection to the db
  connection=pymysql.connect(host="localhost",password="",database="sokogarden",user="root")
  #create a cursor
  cursor=connection.cursor(pymysql.cursors.D)
  #structure the sql to fetch all products
  sql="SELECT * FROM `product_details` "
  #use cursor to execute sql
  cursor.execute(sql)
  #create a variable that will hold the products fetched from the db
  products=cursor.fetchall()
  #return the response
  return jsonify({"products":products})
  return jsonify({"message":"Get products accessed sucessfully"})

#run web app
app.run(debug=True)