from flask import Blueprint

user_login_blueprint = Blueprint('user_login_blueprint',__name__,url_prefix='/user')

@user_login_blueprint.route('/login')
def login():
    return 'Please login into the website'

@user_login_blueprint.route('/register')
def register():
    return "Please create your own website"

@user_login_blueprint.route('/log_out')
def logout():
    return "Please log out from the website"

