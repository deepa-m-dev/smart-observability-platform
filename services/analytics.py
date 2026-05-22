import pandas as pd

from database import get_connection


def load_dataframe():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM logs",
        conn
    )

    conn.close()

    return df


def generate_analytics():

    df = load_dataframe()

    if df.empty:

        return {
            "message": "No logs available"
        }

    total_logs = len(df)

    success_rate = round(
        (
            len(df[df["status"] == "success"])
            / total_logs
        ) * 100,
        2
    )

    failure_rate = round(
        (
            len(df[df["status"] == "failure"])
            / total_logs
        ) * 100,
        2
    )

    avg_response_time = round(
        df["response_time"].mean(),
        2
    )

    most_used_api = (
        df["api_name"]
        .value_counts()
        .idxmax()
    )

    slowest_api = (
        df.groupby("api_name")["response_time"]
        .mean()
        .idxmax()
    )

    most_failing_api = (
        df[df["status"] == "failure"]["api_name"]
        .value_counts()
    )

    if not most_failing_api.empty:
        most_failing_api = most_failing_api.idxmax()
    else:
        most_failing_api = "None"

    health = "Healthy"

    if failure_rate > 40:
        health = "Critical"

    elif failure_rate > 20:
        health = "Warning"

    # ------------------------------------
# AI-like Insights
# ------------------------------------

    insights = []

    if failure_rate > 30:

        insights.append(
            "High failure rate detected"
        )

    if avg_response_time > 700:

        insights.append(
            "System latency is critical"
        )

    if slowest_api == "/payments":

        insights.append(
            "Payments API is unstable"
        )

    if success_rate > 90:

        insights.append(
            "System performance is stable"
        )

    if total_logs > 100:

        insights.append(
            "High traffic volume detected"
        )

    return {

        "total_logs": total_logs,

        "success_rate": success_rate,

        "failure_rate": failure_rate,

        "average_response_time": avg_response_time,

        "most_used_api": most_used_api,

        "slowest_api": slowest_api,

        "most_failing_api": most_failing_api,

        "system_health": health,

        "insights": insights
    }