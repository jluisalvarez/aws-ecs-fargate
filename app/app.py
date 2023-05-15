
# file app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo from jluisalvarez in AWS ECS and Fargate!'
    

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)
