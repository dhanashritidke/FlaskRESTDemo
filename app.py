import csv
import json
from flask import Flask
from flask import request

data={}
with open('ra_data_classifier.csv', 'r', encoding='mac_roman') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header=None
    for index,row in enumerate(fileReader):
        if index == 0:
            header=row
            continue
        r={}
        for _,head in enumerate(row):
            r[header[_]]=head
        data[row[0]]=r

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def getJSON():
    content = request.get_json(silent=True)
    if hid in data.keys():
        return json.dumps(data[content["hid"]])
    else:
        return json.dumps({})

@app.route("/hid/<hid>",methods=['GET','POST'])
def getJSONwithHid(hid):
    if hid in data.keys():
        return json.dumps(data[hid])
    else:
        return json.dumps({})
