import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{'origins': '*'}})

@app.route('/', method=['GET'])
def index():
    return "<h1>Hello World</h1>"
   
def main():
    port = int(os.environ.get("PORT", 5000)) # Pegar PORT do host
    app.run(host="0.0.0.0", port = port)

if __name__ == "__main__":
    main()
© 2022 GitHub, Inc.
