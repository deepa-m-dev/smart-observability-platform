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

start_simulator()

app.register_blueprint(logs_bp)


@app.route("/")
def dashboard():

    create_charts()

    return render_template(
        "dashboard.html"
    )


if __name__ == "__main__":
    
    app.run(debug=True)