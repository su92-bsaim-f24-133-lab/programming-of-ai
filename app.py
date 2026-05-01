from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke_data = response.json()
    
    return render_template('index.html', joke=joke_data)

if __name__ == '__main__':
    app.run(debug=True)