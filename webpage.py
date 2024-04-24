from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def welcome():
    return "I found you " + request.remote_addr

app.run(host="0.0.0.0", port="3000")