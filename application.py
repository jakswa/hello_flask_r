from flask import Flask
# interface with R
import rpy2.robjects as robjects

application = Flask(__name__)

application.debug=True

@application.route("/")
def hello():
    # running some arbitrary R code to test
    str = robjects.r('paste("IM", "A STRING", "BUILT WITH RRRRR")')[0]
    return "Hello world! " + str

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
