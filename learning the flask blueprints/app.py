# importing Flask class from flask module
from flask import Flask
from order_management import order_manager_blueprint
from user_login import user_login_blueprint

# creating an object of Flask class
app = Flask(__name__)

app.register_blueprint(order_manager_blueprint)
app.register_blueprint(user_login_blueprint)

#Decorating our function with app.route method
@app.route('/')
def hello_world():
    return "Hello, This is home page."

#Running our Flask application using app.run method
if __name__ == '__main__':
   app.run()