class Config:
    DEBUG = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db' #:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
