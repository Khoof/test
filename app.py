from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Innovative Web App</title>
        </head>
        <body style="font-family: Arial, sans-serif; background-color: #f0f0f0;">
            <h1 style="text-align: center; color: #333;">Welcome to Our <span style="color: yellow;">Innovative</span> Web App!</h1>
            <p style="text-align: center; font-size: 1.2em;">
                Crafted with passion by <span style="color: black;">Mubeen</span> and Fahad Aslam – where creativity meets technology.
            </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
