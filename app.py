from flask import (
    Flask,
    render_template
)

from database import init_db
from traffic_simulator import start_simulator
from routes.logs import logs_bp

from utils.charts import create_charts

app = Flask(__name__)

init_db()

app.register_blueprint(logs_bp)

start_simulator()

@app.route("/")
def dashboard():

    try:
        create_charts()
    except Exception as e:
        print("Chart error:", e)


    return render_template(
        "dashboard.html"
    )


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
