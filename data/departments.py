import sqlalchemy as sa
import sqlalchemy.orm as orm
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    members = sa.Column(sa.String)
    email = sa.Column(sa.String)
    chief = orm.relation('User')
