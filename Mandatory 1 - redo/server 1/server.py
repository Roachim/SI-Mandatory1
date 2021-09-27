#Receive XML, send Json - Receive and send CSV

from bottle import route, run, get, post, requests

import requests

##################################
@route("/XML")
def do():
    XML = 
    request = requests.post('http//:127.0.0.1:2222')
    return "Thank you"



run(host="127.0.0.1" , port=1111 , debug=True , reloader=True )