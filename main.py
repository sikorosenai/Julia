from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
    return 'Wassup Earth'

if __name__ == '__main__':
  app.run()