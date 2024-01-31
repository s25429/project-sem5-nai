from flask import Flask, render_template
from models.raw.bert import get_example


app = Flask(__name__)


@app.route('/')
def index():
    print(get_example())
    return render_template('index.html', test='PYTHON')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8123, debug=True)
