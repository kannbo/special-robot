from bottle import route, run, template
import subprocess
subprocess.Popen(["python3","cat_line.py"])

@route('/')
def index(name):
    return template('<b>Hello {{name}}</b>!', name="world")

run(host='0.0.0.0', port="10000")
