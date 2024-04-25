from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def welcome():
    return render_template("screen.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port="3000")