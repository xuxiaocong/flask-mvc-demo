from sqlalchemy import Column, Integer, String

from common.database.db_client import DbClient

Base = DbClient.get_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    age = Column(Integer)
    fullname = Column(String(60))

    def cal_fullname(self):
        self.fullname = f"{self.first_name}{self.last_name}"

    def __repr__(self):
        return f"User(id={self.id},age={self.age},fullname={self.fullname}"

    def get_dict(self):
        return {'id': self.id, 'age': self.age, 'fullname': self.fullname}
