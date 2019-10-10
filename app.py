from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import time
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return '<h1>Welcome to API server</h1>'


@app.route("/send_link", methods=['GET', 'POST'])
def send_link():
    rf = request.json  # Receive link from client
    url = rf['link']
    r = requests.get(url)
    page = r.text  # HTML page
    soup = BeautifulSoup(page, 'html.parser')
    for h1 in soup.find_all('h1'):
        # Get list of <h1> tags and
        # select <h1> with most word count
        if len(h1.text) > 5:
            heading = h1.text.strip()
            break  # Get page header
    for p in soup.find_all('p'):
        # Get list of <p> tags and
        # select <p> with most word count
        if len(p.text) > 100:
            summary = p.text.strip()
            break
    # Send data to client
    return jsonify({'heading': heading, 'summary': summary})


if __name__ == '__main__':
    app.run()
