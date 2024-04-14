from bottle import route, run, template
import subprocess
subprocess.Popen(["python3","cat_line.py"])

@route('/')
def index(name):
    return "<title>こんちゃ</title><h1>OKです"

run(host='0.0.0.0', port="10000")
