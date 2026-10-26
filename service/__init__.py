from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Configure security headers
talisman = Talisman(app)

# Enable Cross-Origin Resource Sharing
cors = CORS(app)
