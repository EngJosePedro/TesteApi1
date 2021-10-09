#from src.server.instance import server


# importar controles do App
#from src.controller.books import *
#from src.GurobiProjetc.proj1 import *



#server.run()



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World beachhh"
