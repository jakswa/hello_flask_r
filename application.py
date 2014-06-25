from flask import Flask
import rpy2.robjects as robjects
application = Flask(__name__)

application.debug=True

@application.route("/")
def hello():
    str = robjects.r('paste("IM", "A STRING", "BUILT WITH RRRRR")')[0]
    return "Hello world! " + str

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
