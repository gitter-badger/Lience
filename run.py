
from flask import Flask

app = Flask(__name__)

app.run(host='0.0.0.0', debug=True, use_reloader=True)