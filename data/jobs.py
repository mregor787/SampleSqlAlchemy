import sqlalchemy as sa
import sqlalchemy.orm as orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime)
    modified_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean)
    team_leader = orm.relation('User')
