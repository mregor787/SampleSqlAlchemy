from data import db_session
from data.jobs import Jobs
from data.users import User
from data.departments import Department

db_session.global_init('space.sqlite')
session = db_session.create_session()

objects = [
    User(
        surname='Scott', name='Ridley', age=21,
        position='captain', speciality='research engineer',
        address='module_1', email='scott_chief@mars.org'
    ),
    User(
        surname='Weir', name='Andy', age=24,
        position='chief', speciality='scientist',
        address='module_2', email='andy_787@mars.org'
    ),
    User(
        surname='Sanders', name='Teddy', age=23,
        position='middle', speciality='scientist',
        address='module_2', email='tedsan@mars.org'
    ),
    User(
        surname='Bean', name='Sean', age=26,
        position='chief', speciality='builder',
        address='module_3', email='beans4all@mars.org'
    ),
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
    ),
    Department(
        title='Department of geological exploration',
        chief_id=2,
        members='3, 4, 5',
        email='geo@mars.org'
    ),
    Department(
        title='Department of construction',
        chief_id=4,
        members='16, 17, 28',
        email='build@mars.org'
    ),
    Department(
        title='Department of terraforming',
        chief_id=1,
        members='4, 5, 6',
        email='terra@mars.org'
    )
]

session.add_all(objects)
session.commit()
