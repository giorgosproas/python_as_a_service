from flask import Flask
from flask import request
from flask import jsonify

import functions

app = Flask('python_as_a_service')


@app.route('/call/<function_name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def call_function(function_name: str):
    function_to_call = getattr(functions, function_name)
    try:
        number=request.args.get("number")
        return function_to_call(number)
    except:
        return function_to_call()
    
    
@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    d={"hello":"world"}
    return jsonify(d)


app.run()