from flask import Flask, url_for, send_file

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
        return "<a href="+url_for('getTest')+">get_test</a"


#@app.route('/user', methods=['GET'])
#def getuser():
        #return "Hi there"

@app.route('/test.html', methods=['GET'])
def getTest():
        return send_file('/test.html')     



#@app.route('/user/<username>', methods=['GET'])
#def getuser(username):
        #return "Hi there"+username

@app.route('/user/<int:id>', methods=['GET'])
def getuserbyid(id):
        return "Getting by ID "+str(id)

@app.route('/user', methods=['POST'])
def postuser():
        print("in post!!!")
        return "in post!!!"

if __name__ == "__main__":
        app.run(debug=True)