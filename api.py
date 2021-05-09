from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"Titre": 'Hello, World!'}

@app.route('/random-knowledge')
def rand():
    titre_activite = ""
    description = ""
    return {"Titre": titre_activite,
            "Description": description}