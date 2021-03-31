from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    db_session.global_init('db/space.sqlite')
    app.run(host='127.0.0.1', port=8080)
