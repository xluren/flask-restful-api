class Config(object):
    DEBUG=False
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SECRER_KEY="hello secret  key"

class MysqlConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql://hello:hello@10.210.71.145:3306/sqlalchemy'
    DEBUG=True

class TestConfig(Config):
    DEBUG=True
