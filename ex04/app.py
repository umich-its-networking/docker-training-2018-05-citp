from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def root():
    return 'Hello %s' % os.getenv('NAME')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
