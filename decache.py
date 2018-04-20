from flask import Flask
from flask import request
import hashlib
import os


app = Flask(__name__)
app.debug = True




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    key=request.headers['X-CACHEKEY']
    #key='httpGET10.110.5.145bneve/PY/'
    py=key.index("/PY")
    k2=key[0:py]+key[py+3:]

    m = hashlib.md5()
    m.update(k2.encode('utf-8'))
    file=m.hexdigest()
    
    # cache levels=1:2 
    path="/var/www/nginx-cache/"+file[-1]+"/"+file[-3:-1]+"/"+file

    deleted=0
    if os.path.exists(path):
        os.remove(path)
        deleted=1


    # some nice feedback output
    OUTPUT="<h1 style='color:blue'>Hello There! </h1><br> %s" % path
    OUTPUT += "<br><br>"
    OUTPUT += key
    OUTPUT += "<br><br>"
    OUTPUT += k2
    OUTPUT += "<br><br>"
    OUTPUT += path
    OUTPUT += "<br><br>"
    if deleted==0:
        OUTPUT+= "File not found"
    else:
        OUTPUT+= "File deleted!"
   
    return OUTPUT



if __name__ == "__main__":
    app.run(host='0.0.0.0')


