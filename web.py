from bottle import route, run, template
import subprocess
subprocess.popen(["python3","cat_line.py"])

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=10000)
