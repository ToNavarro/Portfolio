from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from form import ContactForm
import smtplib
import os
from dotenv import load_dotenv, find_dotenv

# Template Page: https://startbootstrap.com/theme/creative

# Find .env file
dotenv_path = find_dotenv()
# Load .env file entries as environment variables
load_dotenv()

OWN_EMAIL = os.environ.get("G_MAIL")
OWN_PASSWORD = os.environ.get("GMAIL_PASSW")


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def portfolio():
    form = ContactForm()
    if form.validate_on_submit():
        message = (f"Subject:New Portfolio's Message\n\nName: {form.name.data}\nEmail: {form.email.data}\n"
                   f"Phone: {form.phone.data}\nMessage: {form.message.data}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, "tomasnavarro@upc.edu.ar", message)
        flash("Message Successfully Sent")
        return redirect(url_for("portfolio"))
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5002)


# TODO: Add My Projects