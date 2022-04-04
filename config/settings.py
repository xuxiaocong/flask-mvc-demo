import os

# 数据库类型（任选其一）
SQL_TYPE = os.environ.get('SQL_TYPE', default='POSTGRES')
# sqlite数据库
SQLITE_URL = os.environ.get('SQLITE_URL', default='temp/test.sqlite')
# postgres数据库参数
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', default=5432)
POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', default='postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='123456')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE',
                                   default='flask_db_demo')
