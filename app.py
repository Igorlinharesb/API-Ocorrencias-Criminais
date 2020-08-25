from flask import Flask

app = Flask(__name__)


@app.route('/api')
def documentacao():
    pass


@app.route('/api/municipio')
def municipio():
    pass


@app.route('api/estado')
def estado():
    pass


if __name__ == '__main__':
    app.run()
