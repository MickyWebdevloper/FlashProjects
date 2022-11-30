import os
# from PythonProject import app


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    EMAIL_USER = os.environ.get('EMAIL_USER')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')
    # set the location for the whoosh index
    WHOOSH_BASE = 'whoose'


    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # app.config['SECRET_KEY'] = '7a64d063534bd17828556d68e5ca4df01292f2482c8f76c5f60b08'
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/pythonncs"
    # app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
