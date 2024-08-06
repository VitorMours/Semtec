from flask import Blueprint, redirect, render_template, request, url_for 






views = Blueprint("views", __name__, template_folder="templates", static_folder="static")


@views.route('/')
def index():
    return render_template("index.jinja")


@views.route('/register', methods=["GET","POST"])
def register():

    if request.method == "GET":
        return render_template("register.jinja")

    elif request.method == "POST":
        return "Registrando elementos"

    else:
        return redirect(url_for("views.error"))
        




@views.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@views.app_errorhandler(405)
def invalid_method(error):
    return render_template("405.html"), 405
