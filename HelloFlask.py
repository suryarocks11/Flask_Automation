from flask import Flask
app =Flask(__name__)

@app.route("/")
def home():
    return("Hello this is Flask")

if __name__ == "__main__":
    app.run(host='localhost', port=9874,debug=True)
print('Running')