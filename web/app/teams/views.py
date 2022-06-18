from flask import render_template, request, jsonify
from . import teams_bp
from .helper import get_all_teams, get_standings_with_date_range


@teams_bp.route("/teams", methods=["GET"])
def teams_page():
    teams = get_all_teams()
    return render_template("teams.html", teams=teams)


@teams_bp.route("/api", methods=["POST"])
def teams_api():
    data = request.get_json(force=True)
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    teams = data.get("teams")
    attrs = data.get("attrs")
    for i, attr in enumerate(attrs):
        if attr.endswith("pct"):
            attrs[i] = attr.replace("pct", "win")
            attrs.append(attr.replace("pct", "loss"))
    return jsonify(get_standings_with_date_range(start_date, end_date, teams, attrs))
