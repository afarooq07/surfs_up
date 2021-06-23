
# import Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Route
@app.route('/')

def hello_world():
    return 'Hello world'
