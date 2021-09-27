#Receive XML, send Json - Receive and send CSV

from bottle import run, get, post, requests

import requests

##################################
@post("/post")
def do():
    request = requests.post('http//:127.0.0.1:2222')



run(host="127.0.0.1" , port=1111 , debug=True , reloader=True )