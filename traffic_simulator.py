import threading
import random
import time

from models import insert_log

apis = [
    "/login",
    "/products",
    "/orders",
    "/payments",
    "/profile",
    "/checkout",
    "/analytics"
]

statuses = ["success", "failure"]

severities = ["INFO", "WARNING", "ERROR", "CRITICAL"]

# Control flag
running = False


def generate_logs():
    global running

    while running:
        api = random.choice(apis)

        status = random.choices(
            statuses,
            weights=[80, 20]
        )[0]

        response_time = random.randint(50, 1200)

        # severity logic
        if response_time > 800:
            severity = "CRITICAL"
        elif response_time > 500:
            severity = "ERROR"
        elif response_time > 300:
            severity = "WARNING"
        else:
            severity = "INFO"

        insert_log(api, status, severity, response_time)

        print(f"Inserted: {api} | {status} | {response_time}ms")

        time.sleep(2)


def start_simulator():
    global running

    if not running:
        running = True

        thread = threading.Thread(target=generate_logs)
        thread.daemon = True
        thread.start()


def stop_simulator():
    global running
    running = False
