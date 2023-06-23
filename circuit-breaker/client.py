from flask import Flask
from flask import request, jsonify
import urllib.request, json
from werkzeug.exceptions import HTTPException
import os
app = Flask(__name__)

variable = os.environ.get('Ambiente')

# Do not remove this method.
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

@app.route('/igv')
def igv():
    status = request.args.get("status")
    tax = get_tax_from_api(status)

    return jsonify(igv=tax), 200

def get_tax_from_api(status):
    print(variable)
    if(variable=="Prod"):
        url = "http://127.0.0.1:5000/tax"
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return int(dict["Tax"])
    
    if(variable=="Test"):
        url = "http://127.0.0.1:3001/tax"
        if(status=="200"):
            response = urllib.request.Request(url,headers={"Scenario":status})
            response = urllib.request.urlopen(response)
            data = response.read()
            dict = json.loads(data)
            return int(dict["Tax"])
        if(status=="500" or status=="403"):
            response = urllib.request.Request(url,headers={"Scenario":status})
            response = urllib.request.urlopen(response)
            data = response.read()
            dict = json.loads(data)
            return int(dict["Message"])
if __name__ == "__main__":
    app.run(debug=True, port=3000)