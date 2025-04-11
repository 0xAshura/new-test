from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return "Hello from Mihir Limbad - 100938484!! This is Flask running on ECS Fargate!"

if _name_ == "_main_":
    app.run()
