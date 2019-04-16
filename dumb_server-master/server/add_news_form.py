from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок поста', validators=[DataRequired()])
    content = TextAreaField('Текст поста', validators=[DataRequired()])
    author = StringField('Автор поста', validators=[DataRequired()])
    submit = SubmitField('Добавить')