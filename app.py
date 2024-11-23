from flask import Flask
from routes import setup_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)