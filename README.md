# 🚀 Smart Observability & API Monitoring Platform

A real-time backend monitoring and analytics system built using Flask, SQLite, Pandas, and Matplotlib.

This project simulates a lightweight observability platform capable of:

- collecting API logs
- monitoring system health
- analyzing backend performance
- generating live analytics
- visualizing traffic trends

---

# 📌 Features

## ✅ Real-Time Log Collection

Insert API logs dynamically using:
- dashboard form
- REST API
- automated traffic simulator

---

## ✅ Live Monitoring Dashboard

Interactive dashboard displaying:

- total logs
- success rate
- failure rate
- system health
- recent logs
- AI-like insights

---

## ✅ Traffic Simulation Engine

Automatically generates:
- random API traffic
- failures
- latency spikes
- varying severities

to simulate real production systems.

---

## ✅ Analytics Engine

Built using Pandas for:

- API usage analysis
- average response time calculation
- failure tracking
- slowest API detection
- health scoring

---

## ✅ AI-like Insights

The system intelligently detects:

- high failure rates
- latency spikes
- unstable APIs
- high traffic conditions

Example:

```text
⚠ High failure rate detected
⚠ Payments API is unstable
⚠ System latency is critical
```

---

## ✅ Data Visualization

Generates real-time charts using Matplotlib:

- Pie Chart → Success vs Failure
- Bar Chart → API Usage Frequency
- Line Chart → Response Time Trends

---

## ✅ CSV Export

Download complete analytics reports as CSV files.

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend |
| Flask | REST API framework |
| SQLite | Database |
| Pandas | Data analysis |
| Matplotlib | Data visualization |

---

# 📂 Project Structure

```text
log-analytics-system/
│
├── app.py
├── database.py
├── models.py
├── traffic_simulator.py
├── requirements.txt
│
├── routes/
│   └── logs.py
│
├── services/
│   └── analytics.py
│
├── utils/
│   └── charts.py
│
├── templates/
│   └── dashboard.html
│
├── static/
│   └── charts/
│
└── logs.db
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-log-analytics-system.git
```

---

## 2️⃣ Open Project

```bash
cd smart-log-analytics-system
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Open Dashboard

```text
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/log` | Insert logs |
| GET | `/logs` | Fetch all logs |
| GET | `/analytics` | Generate analytics |
| GET | `/charts` | Generate charts |
| GET | `/simulate` | Generate fake traffic |
| GET | `/export/csv` | Download CSV report |

---

# 📊 Example Log Payload

```json
{
  "api_name": "/payments",
  "status": "failure",
  "severity": "CRITICAL",
  "response_time": 842
}
```

---

# 🧠 Analytics Generated

The system computes:

- total logs
- success percentage
- failure percentage
- average response time
- most used API
- slowest API
- most failing API
- health status

---

# 📈 Dashboard Features

## ✅ Auto Refresh

Dashboard updates automatically every few seconds.

---

## ✅ Live Charts

Charts dynamically regenerate based on incoming logs.

---

## ✅ Intelligent Monitoring

System generates human-readable insights based on analytics.

---

# 🔥 Sample Insights

```text
⚠ High failure rate detected
⚠ Payments API is unstable
⚠ System latency is critical
✓ System performance is stable
```

---

# 🎯 Purpose of This Project

This project was built to understand how real-world monitoring and observability platforms work internally.

It simulates concepts used in production systems such as:

- observability
- performance monitoring
- API analytics
- backend health tracking
- traffic analysis

---

# 🚀 Future Improvements

- Interactive charts using Chart.js
- Real-time WebSocket monitoring
- Alert notification system
- Machine learning anomaly detection
- PostgreSQL support
- Docker deployment
- User authentication

---

# ⭐ Final Outcome

This project evolved from a simple logging system into a mini real-time observability platform capable of:

✅ collecting logs  
✅ analyzing system performance  
✅ generating insights  
✅ visualizing backend health  
✅ simulating live production traffic  
✅ monitoring API behavior in real-time

---

# 👨‍💻 Author

Deepa M

AI/ML Developer Aspirant
Passionate about building intelligent real-world applications using Machine Learning and Full Stack Development.
