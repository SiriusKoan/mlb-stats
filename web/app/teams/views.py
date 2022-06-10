from flask import render_template
from . import teams_bp


@teams_bp.route("/teams", methods=["GET"])
def teams_page():
    return render_template("teams.html")
