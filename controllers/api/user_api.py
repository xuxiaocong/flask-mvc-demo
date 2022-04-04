from flask import Blueprint
from flask import request
from common.database.user_orm import UserOrm
from common.models.user import User

user_api = Blueprint("user_api", __name__)


@user_api.before_request
def befor():
    if request.method == 'POST':
        # return dict(message="要先登录")
        pass


@user_api.route("", methods=['GET', 'POST'])
def user_index():
    if request.method == 'GET':
        users = UserOrm().get_all()
        return {"users": [i.get_dict() for i in users]}
    elif request.method == 'POST':
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        age = request.json.get('age')
        user = User(first_name=first_name, last_name=last_name, age=age)
        id_ = UserOrm().add(user)
        return dict(id=id_)
