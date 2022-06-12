from flask import render_template
from . import main_bp


@main_bp.route("/", methods=["GET"])
def index_page():
    return render_template("index.html")
