from flask import Flask
from routes.api import api_blueprint

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
