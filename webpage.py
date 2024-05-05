from flask import Flask, request, render_template, jsonify
from screenCapture import screenVar
import time
import threading

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def welcome():
    # time.sleep(1)
    return render_template("screen.html")

@app.route('/getScreen')
def get_screen():
    return jsonify(ssBase64=screenVar.base64)

if __name__=="__main__":
    try:
        app.debug = True
        threading.Thread(target=screenVar.capture).start()
        app.run(host="0.0.0.0", port="3000")
        screenVar.stop_event.set()
    except KeyboardInterrupt:
        print("Exiting the program...")
        screenVar.stop_event.set()