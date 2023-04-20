from flask import Flask

app = Flask("My Hello World Application")

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run(debug=True)
