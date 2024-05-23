from flask import Flask,request,jsonify
import json
import requests
import os
import datetime
import schedule
import time
import threading
import random
import google.generativeai as genai
app = Flask(__name__)
genai.configure(
    api_key = os.environ.get('API_KEY_GOOGLE_GEN')
)
@app.route('/')
def raw_root():
    return '<style>body{background:black;color:#03fc88;}</style>Status code 111 State ----> Done--> can proceed with all arguments (server running with configurations)'
content = "null"
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
@app.route('/GoogleGenAI',methods=['GET'])
def dusky():
    #return content variable
    return jsonify({'blog':"Soothes Nausea and Digestion: Ginger is a champion when it comes to calming nausea and indigestion. It can help ease stomach upset, vomiting, and even motion sickness. Studies suggest ginger may speed up the emptying of your stomach, further aiding digestion.",'img':'https://images.pexels.com/photos/984944/pexels-photo-984944.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'})
def zebronica():
    query = readQueries()
    iterator = random.randint(1,len(query))
    question = query[iterator]['q']
    response = chat.send_message(question)
    vision = getVision(query[iterator]['c'])
    content = jsonify({'blog':"Soothes Nausea and Digestion: Ginger is a champion when it comes to calming nausea and indigestion. It can help ease stomach upset, vomiting, and even motion sickness. Studies suggest ginger may speed up the emptying of your stomach, further aiding digestion.",'img':'https://images.pexels.com/photos/984944/pexels-photo-984944.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'})
    
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

def strange():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    if current_time == '00:00:00':
        zebronica()
    
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every(1).minutes.do(strange)
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()


