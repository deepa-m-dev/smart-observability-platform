from flask import (
    Blueprint,
    request,
    jsonify,
    send_file
)
from traffic_simulator import start_simulator, stop_simulator

import random
import pandas as pd

from models import (
    insert_log,
    fetch_logs
)

from services.analytics import (
    generate_analytics,
    load_dataframe
)

from utils.charts import (
    create_charts
)

logs_bp = Blueprint(
    "logs",
    __name__
)


# ----------------------------------------
# INSERT LOG
# ----------------------------------------

@logs_bp.route("/log", methods=["POST"])
def add_log():

    data = request.get_json()

    api_name = data.get("api_name")

    status = data.get("status")

    severity = data.get("severity")

    response_time = data.get("response_time")

    if not api_name:

        return jsonify({
            "error": "API name required"
        }), 400

    insert_log(
        api_name,
        status,
        severity,
        response_time
    )

    return jsonify({
        "message": "Log inserted"
    })


# ----------------------------------------
# FETCH LOGS
# ----------------------------------------

@logs_bp.route("/logs")
def logs():

    return jsonify(
        fetch_logs()
    )


# ----------------------------------------
# ANALYTICS
# ----------------------------------------

@logs_bp.route("/analytics")
def analytics():

    return jsonify(
        generate_analytics()
    )


# ----------------------------------------
# CHARTS
# ----------------------------------------

@logs_bp.route("/charts")
def charts():

    create_charts()

    return jsonify({

        "pie_chart":
        "/static/charts/pie.png",

        "bar_chart":
        "/static/charts/bar.png",

        "line_chart":
        "/static/charts/line.png"
    })


# ----------------------------------------
# SIMULATE TRAFFIC
# ----------------------------------------

@logs_bp.route("/simulate")
def simulate():

    apis = [
        "/login",
        "/products",
        "/orders",
        "/payments",
        "/profile"
    ]

    statuses = [
        "success",
        "failure"
    ]

    severities = [
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
    ]

    for _ in range(50):

        insert_log(

            random.choice(apis),

            random.choice(statuses),

            random.choice(severities),

            random.randint(50, 1000)

        )

    return jsonify({
        "message": "Fake traffic inserted"
    })


# ----------------------------------------
# EXPORT CSV
# ----------------------------------------

@logs_bp.route("/export/csv")
def export_csv():

    df = load_dataframe()

    file_name = "logs_report.csv"

    df.to_csv(
        file_name,
        index=False
    )

    return send_file(
        file_name,
        as_attachment=True
    )

# ----------------------------------------
# SIMULATION START AND STOP
# ----------------------------------------

@logs_bp.route("/start-sim")
def start_sim():
    start_simulator()
    return {"message": "Simulation started"}


@logs_bp.route("/stop-sim")
def stop_sim():
    stop_simulator()
    return {"message": "Simulation stopped"}
