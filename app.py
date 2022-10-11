from flask import Flask, request, make_response
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
import json

app = Flask(__name__)

@app.post('/api/hero')
def add_hero():
    invalid = check_endpoint_info(request.json, ['name', 'description', 'image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400) 

    results = run_statement('CALL insert_hero(?,?,?)', [request.json.get('name'), request.json.get('description'), request.json.get('image_url')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 400)


app.run(debug=True)