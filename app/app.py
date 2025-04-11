from flask import Flask
import socket

app = Flask(_name_)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  return 'Hello from Mihir Limbad - 100938484!! This is Flask running on ECS Fargate!'
  
@app.route('/host')
def host_name():
  return hostname

@app.route('/ip')
def host_ip():
  return ip_address

app.run(host='0.0.0.0')
