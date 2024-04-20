import scratchattach as scratch3,time,random,requests
from bottle import run,route,Bottle
import os
PASSWORD = os.environ.get('PASSWORD')
print(PASSWORD)
session = scratch3.login("kannbo", str(PASSWORD)) # 自分のパスワード
conn = session.connect_cloud("980998475") # project_id
NAME={}
ii=0
debug=True #デバッグ以外False!!

for i in """-
_
1
2
3
4
5
6
7
8
9
0
a
b
c
d
e
f
g
h
i
j
k
l
n
m
o
p
q
r
s
t
u
v
w
x
y
z
Z
Y
X
W
V
U
T
S
R
Q
P
O
N
M
L
K
J
I
H
G
F
E
D
C
B
A""".split("\n"):
    ii+=1
    if ii%10==0:
        ii+=1
    NAME[str(ii)]=i
print(NAME)
name=""
while True:
    name=""
    time.sleep(random.randint(1,4))
    variables = scratch3.get_cloud("980998475")
    #print(scratch3.get_cloud("980998475"))
    #print(variables["UserName"],end=" ")
    for i in str(variables["UserName"]).split("0"):
        
        if i=="":
            pass
        else:
            name=name+NAME[i]
    if debug:
        print(name)
    try:
        getdata2=scratch3.get_user(name).follower_count()
        conn.set_var("follower",str(getdata2))
        getdata3=scratch3.get_user(name).following_count()
        conn.set_var("follow",str(getdata3))
        conn.set_var("error","0")
        getdata1=requests.get(f"https://api.scratch.mit.edu/users/{name}/messages/count/").json()
        conn.set_var("message",str(getdata1["count"]))
        time.sleep(1)
        UNAME=variables["UserName"]
        conn.set_var("UserName",UNAME)
    except Exception as e:
        try:
            conn.set_var("error","1")
            print("error")
            conn.set_var("follow","0")
            conn.set_var("follower","0")
            conn.set_var("message","0")
            UNAME=variables["UserName"]
            conn.set_var("UserName",UNAME)
            print(e)
        except:
            try:
                session = scratch3.login("kannbo", str(PASSWORD)) # 自分のパスワード
                conn = session.connect_cloud("980998475")
            except:
                pass
app = Bottle()
"""
@app.route("/")
def aaaa():
    return ""
    <style>
    p{
      color:red;
      }
    </style><p>これが見えてたら公開済み</p>""

run(app, host='localhost',)"""
