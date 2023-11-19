from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired("Required Field.")],
                       render_kw={"placeholder": "Full name"})
    email = StringField(validators=[DataRequired("Required Field."), Email("Not a valid email.")],
                        render_kw={"placeholder": "Valid email address"})
    phone = StringField(validators=[DataRequired("Required Field.")],
                        render_kw={"placeholder": "Starting with country code"})
    message = TextAreaField(validators=[DataRequired("Required Field.")],
                            render_kw={"placeholder": "What do you want to tell me?"})
    submit = SubmitField("Send Message")
