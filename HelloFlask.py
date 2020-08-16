#pip install mysqlclient
from flask import Flask ,redirect,render_template, make_response,request,session,url_for
from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dq_database'
app.secret_key="Surya"
db=SQLAlchemy(app)
class user_1(db.Model):
    _id =db.Column("ID",db.Integer,primary_key =True)
    name =db.Column(db.String(100))
    email =db.Column(db.String(100))
    password =db.Column(db.String(100))

    def __init__(self,name,email,password):
        self.name =name
        self.email = email
        self.password = password

#Db 



#@app.route('/index', methods=['GET'])
#home page
@app.route("/")

def home():
    return render_template ('index.html')
    #headers = {'Content-Type': 'text/html'}
    #return make_response(render_template('index.html'),200,headers)
    #return make_response(render_template('index.html'))
#login Page

@app.route('/login',methods=["POST","GET"])
def login ():
    email=''
    if request.method == 'POST':
        email = request.form["InputEmail"]
        session["email"]=email
        admin = user(email, email,email)

        db.create_all() # In case user table doesn't exists already. Else remove it.    

        db.session.add(admin)

        db.session.commit()





        return redirect(url_for("admin",data=email))
    else:
        if "email" in session :
            return redirect(url_for("admin",data=session["email"]))

        else:
            return render_template('login.html')
    #login logic here

    #login logic here

#signup page

@app.route('/register')
def register():
    return render_template ('register.html')
    #register logic here

@app.route('/admin')
def admin():
    if 'email' in session :
        email=session['email']
        return render_template ("index_admin.html",data=email) 
        
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect(url_for("login"))
@app.route("/<name>")
def name(name):
    return (f'Helow {name}!')

if __name__ == "__main__":
    db.create_all()
    app.run(host='localhost', port=9874,debug=True)


print('Running')