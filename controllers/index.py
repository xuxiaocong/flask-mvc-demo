from flask import Blueprint, render_template
from common.database.user_orm import UserOrm

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    users = UserOrm().get_all()
    return render_template("index.html", users=users)
