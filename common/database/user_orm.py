from sqlalchemy import select
from common.database.db_client import DbClient
from common.models.user import User


class UserOrm:

    def __init__(self) -> None:
        self._session = DbClient.get_session()

    def get_all(self):
        stmt = select(User)
        return self._session.scalars(stmt)

    def add(self, user: User):
        id_ = None
        with self._session as session:
            user.cal_fullname()
            session.add(user)
            session.flush()
            id_ = user.id
            session.commit()
        return id_