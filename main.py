from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField
import smtplib
from datetime import datetime

EMAIL = "jeankalema058@gmail.com"
PASSWORD = "mntp szaa fbkf rthg"

app = Flask(__name__)

app.config['SECRET_KEY'] = "qwerty"

class FormContat(FlaskForm):
    nom = StringField(label="Nom", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    body = CKEditorField(label="Body", validators=[DataRequired()])
    submit = SubmitField(label="Envoi")

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = FormContat()
    date_nom = datetime.now().year
    if request.method == "POST":
        nom = form.nom.data
        email = form.email.data
        body = form.body.data
        
        with smtplib.SMTP("smtp.gmail.com") as connexion:
            connexion.starttls()
            connexion.login(user=EMAIL, password=PASSWORD)
            connexion.sendmail(from_addr=EMAIL,
                               to_addrs="bagayafazili@gmail.com",
                               msg=f"subject:Nouveau message \n\nEmail:{email}\nNom:{nom}\n{body}")
        return redirect(url_for("contact"))
            
    return render_template("contact.html", form=form, date=date_nom)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
