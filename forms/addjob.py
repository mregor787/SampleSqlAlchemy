from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    team_leader_id = IntegerField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')
