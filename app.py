from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DevOps demo - v2!, wassup Jatin rawal how u doin"

@app.route('/health')
def health():
    return "OK jatin"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
