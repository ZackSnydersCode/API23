from flask import Flask,request,jsonify
import json
import requests
import os
import google.generativeai as genai
app = Flask(__name__)
genai.configure(
    api_key = os.environ.get('API_KEY_GOOGLE_GEN')
)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
@app.route('/')
def raw_root():
    return "<h1>Hello</h1>"
@app.route('/GoogleGenAI',methods=['GET'])
def homepage():
    iterator = int(request.args.get('i'))
    query = readQueries()
    question = query[iterator]['q']
    response = chat.send_message(question)
    vision = getVision(query[iterator]['c'])
    return jsonify({'blog':response.text,'img':vision})
def readQueries():
    try:
        with open('queries.json','r') as q:
            e = q.read()
            jQ = json.loads(e)
            return jQ
    except Exception as e:
        print(e)
        return ""

def getVision(query):
    try:
        pexels_url = f'https://api.pexels.com/v1/search?query={query}&per_page={1}&media_type=video'
        headers = {'Authorization':os.environ.get('API_KEY_PEXELS_VISION')}
        response = requests.get(pexels_url,headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        return e

