from data import db_session
from data.jobs import Jobs
from data.users import User

db_session.global_init('space.sqlite')
session = db_session.create_session()

objects = [
    User(surname='Scott', name='Ridley'),
    User(surname='Weir', name='Andy'),
    User(surname='Sanders', name='Teddy'),
    Jobs(
        team_leader_id=1,
        job='Deployment of residential modules 1 and 2',
        work_size=15,
        collaborators='2, 3',
        is_finished=0
    ),
    Jobs(
        team_leader_id=2,
        job='Exploration of mineral resources',
        work_size=15,
        collaborators='3, 4',
        is_finished=0
    ),
    Jobs(
        team_leader_id=3,
        job='Development of a management system',
        work_size=25,
        collaborators='5',
        is_finished=0
    )
]

session.add_all(objects)
session.commit()
