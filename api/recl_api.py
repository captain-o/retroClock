from flask import Flask
from flask import request
import json
app = Flask(__name__)

directory = 'E:/owncloud/Coden/raspiSpielerei/Wecker/api/time.json'


# set FLASK_APP=recl_api.py
# flask run

#Firefox RestClient
#Header: "Content-Type: application/json"
#Body: "{"time":"07:10"}"
#http://themayesfamily.com/blogs/b/2011/05/23/rest-client-for-firefox-sample-post-request/

@app.route('/')
def index():
    return 'Index Page'

@app.route('/getTime')
def getTime():
    with open(directory, 'r') as f:
      data = json.load(f)
    return data['time']

@app.route('/setTime', methods=['POST'])
def setTime():
    #print("is Json:", flush=True)
    #print (request.is_json, flush=True)
    content = request.get_json()
    #print (content['time'])
    newTime = content
    f = open(directory,"w", encoding='UTF-8' )
    f.write(str(newTime))
    f.close()

    return "Next alarm set"

#https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application


#https://www.predic8.de/post-put-patch-beispiel.htm
#https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/
