from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is Mubeen with Fahad Aslam and this is our app!"

if __name__ == '__main__':
    app.run(debug=True)
