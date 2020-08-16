from flask import Flask ,redirect,render_template, make_response,request,session,url_for
app =Flask(__name__)

app.secret_key="Surya"
@app.route('/index', methods=['GET'])
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
    app.run(host='localhost', port=9874,debug=True)


print('Running')