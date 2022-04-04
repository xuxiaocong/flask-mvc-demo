from application import app

from common.database.db_client import DbClient


@app.before_first_request
def before_first():
    from common.models.user import User
    DbClient.init_table()


@app.before_request
def before_request():
    print('all.befor_request')


@app.after_request
def after_request(response):
    app.logger.info("----------------before_request----------------")
    return response
