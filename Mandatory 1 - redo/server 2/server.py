#Receieve Json, Send CSV

from bottle import run, get, post, requests

import requests

#################################
@post("/post")
def do():
    request = requests.post('http//:127.0.0.1:1111')






run(host="127.0.0.1" , port=2222 , debug=True , reloader=True )