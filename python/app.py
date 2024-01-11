from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def hello():

    return "Hello Flask,Let's Learn Docker by doing"

if __name__ == '__main__':
    app.run(debug=True)
