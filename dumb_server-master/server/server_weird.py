import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/news')
def news():
    with open("news.json") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
