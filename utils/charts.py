import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

from database import get_connection


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CHART_DIR = os.path.join(
    os.path.dirname(BASE_DIR),
    "static",
    "charts"
)


def create_charts():

    os.makedirs(
        CHART_DIR,
        exist_ok=True
    )

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM logs",
        conn
    )

    conn.close()

    if df.empty:

        return

    # PIE CHART

    status_counts = df["status"].value_counts()

    plt.figure(figsize=(5, 5))

    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Success vs Failure")

    plt.savefig(
        os.path.join(
            CHART_DIR,
            "pie.png"
        )
    )

    plt.close()

    # BAR CHART

    api_counts = df["api_name"].value_counts()

    plt.figure(figsize=(7, 5))

    api_counts.plot(kind="bar")

    plt.title("API Usage Frequency")

    plt.savefig(
        os.path.join(
            CHART_DIR,
            "bar.png"
        )
    )

    plt.close()

    # LINE CHART

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["timestamp"],
        df["response_time"]
    )

    plt.title("Response Time Trend")

    plt.savefig(
        os.path.join(
            CHART_DIR,
            "line.png"
        )
    )

    plt.close()