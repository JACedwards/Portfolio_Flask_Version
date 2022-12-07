from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "hello world"

@application.route('/recommendations')
def recs():
    return "Recommendations will be on this page"

if __name__ == '__main__':
    application.run(debug=True)