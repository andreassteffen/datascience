from flask import Flask
from flask import request
import uuid


app = Flask(__name__)

@app.route("/get_foto", methods=['GET', 'POST'])
def get_foto():
    if request.method == 'POST':
        data = request.get_json()
        print data['x'], data['y'],data['height'],data['width']
        print data['img']
        # In Python 2.7
        filename = str(uuid.uuid4())
        fh = open("{}.png".format(filename), "wb")
        fh.write(data['img'].replace('data:image/png;base64,','').decode('base64'))
        fh.close()

    return "Hello World!"