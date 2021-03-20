import json
import os
import math
import requests
import time
import threading


app = Flask(__name__)

@app.route("/ids",methods=['POST', 'GET'])
def ids():
	print ("123")

if __name__ == "__main__":
	
	app.run(host="0.0.0.0", port=int("5050"))