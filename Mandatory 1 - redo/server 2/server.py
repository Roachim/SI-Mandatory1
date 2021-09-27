#Receieve Json, Send CSV

from bottle import route, run, get, post, requests

import requests

#################################
@route("/JSON")
def do():
    request = requests.post('http//:127.0.0.1:1111')
    return "Thank you"






run(host="127.0.0.1" , port=2222 , debug=True , reloader=True )