from flask import Flask, render_template, request, session, flash
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from sqlalchemy.dialects import mysql

with open('config.json', 'r') as c:
    params = json.load(c) ["params"]

app = Flask(__name__)

app.secret_key = 'super-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost/codingbh'
db = SQLAlchemy(app)
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), nullable=True)

class Contacts(db.Model):
    contactID = db.Column(db.Integer, primary_key=True)
    contactName = db.Column(db.String(80), nullable=False)
    contactEmail = db.Column(db.String(80), nullable=False)
    contactPhoneNo = db.Column(db.String(80), nullable=False)
    contactMessage = db.Column(db.String(80), nullable=False)

class Posts(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),nullable= False)
    tagline= db.Column(db.String(120),nullable= False)
    slug = db.Column(db.String(25),nullable= False)
    content = db.Column(db.String(120),nullable= False)
    date = db.Column(db.String(12),nullable= True)
    img_file = db.Column(db.String(12), nullable=True)




app.config.update(
    MAIL_SERVER = 'contact2shivesh@gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)




@app.route('/')
def homepage():
    posts = Posts.query.filter_by().all()[0:50]
    return render_template('index.py',params=params,posts=posts)



@app.route('/about')
def aboutpage():
    userName11 = "Shivesh"
    return render_template('about.py', name = userName11,params=params)



@app.route('/contact',methods = ['GET', 'POST'])
def contactpage():
    if(request.method=='POST'):
        contactName = request.form.get('contactName')        
        contactEmail = request.form.get('contactEmail')        
        contactPhoneNo = request.form.get('contactPhoneNo')        
        contactMessage = request.form.get('contactMessage')        
        
        entry = Contacts(contactName=contactName,contactEmail=contactEmail,contactPhoneNo=contactPhoneNo,contactMessage=contactMessage)

        db.session.add(entry)
        db.session.commit()       
            
    return render_template('contact.py',params=params)


@app.route('/post/<string:post_slug>', methods=['GET'])
def post_slug_page(post_slug):
    post = Posts.query.filter_by(slug= post_slug).first()
    
    # Get the SQL statement
    #statement = post.statement
    
    # Print the compiled SQL query for MySQL
    #print(statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True}))

    # Execute the query
    #query = post.first()
    #print(post)

    return render_template('post.py',params=params, post=post) 
    


@app.route('/hello', methods = ['GET', 'POST'])
def hellopage():
    if(request.method=='POST'):
        userName = request.form.get('userName')
    return "Hello, World!"+userName



@app.route('/user', methods = ['GET', 'POST'])
def userpage():
    if(request.method=='POST'):
        userName = request.form.get('userName')        
        
        entry = User(userName=userName)

        db.session.add(entry)
        db.session.commit()
        

    return render_template('user.py',params=params)


@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user']== params['adminUname']):

        return render_template("dashboard.py",params=params) 

    if(request.method=='POST'):
       userName= request.form.get('uname')   
       userPass= request.form.get('pass') 

       if (userName== params['adminUname'] and userPass== params['adminPass'] ):
        session['user']= userName 
        flash('You have successfully logged yourself in.') 

        return render_template("dashboard.py",params=params) 
        

    return render_template('Login.py',params=params)

@app.route('/login')
def login():
    return render_template('Login.py',params=params)

@app.route('/logout')
def logout():
    if session.get('user'):
        # prevent flashing automatically logged out message
        #del session['user']
        session.pop('user', None)
        flash('You have successfully logged yourself out.')
    return render_template('Login.py',params=params)




if __name__ == "__main__":
    app.run(debug=True)
