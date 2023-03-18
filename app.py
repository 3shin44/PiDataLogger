# Import Flask
from flask import Flask

# Create an app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run()