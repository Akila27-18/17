from flask import Flask, render_template, flash, redirect, url_for
from forms import PasswordResetForm

app = Flask(__name__)
app.secret_key = "resetsecret"

@app.route("/", methods=["GET", "POST"])
def reset():
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Password reset successfully!", "success")
        return redirect(url_for("reset"))
    return render_template("reset.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
