from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            Hello, my name is <span style="color: red;">Mubeen</span> with Fahad Aslam and this is our app!
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
