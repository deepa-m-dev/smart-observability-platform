

async function loadAnalytics(){

    const res =
    await fetch("/analytics")

    const data =
    await res.json()

    document
    .getElementById("totalLogs")
    .innerText =
    data.total_logs

    document
    .getElementById("successRate")
    .innerText =
    data.success_rate + "%"

    document
    .getElementById("failureRate")
    .innerText =
    data.failure_rate + "%"

    document
    .getElementById("health")
    .innerText =
    data.system_health

    let insightsHTML = ""

data.insights.forEach(insight => {

    insightsHTML += `

    <div style="
        background:#334155;
        padding:12px;
        margin-top:10px;
        border-radius:8px;
    ">

        ⚠ ${insight}

    </div>
    `
})

document
.getElementById("insights")
.innerHTML = insightsHTML
}

async function loadLogs(){

    const res =
    await fetch("/logs")

    const logs =
    await res.json()

    let rows = ""

    logs.forEach(log => {

        rows += `

        <tr>

        <td>${log.api_name}</td>

        <td class="${
            log.status
        }">

        ${log.status}

        </td>

        <td>${log.severity}</td>

        <td>${log.response_time}</td>

        <td>${log.timestamp}</td>

        </tr>
        `
    })

    document
    .getElementById("logsTable")
    .innerHTML = rows
}

document
.getElementById("logForm")
.addEventListener("submit",

async(e)=>{

    e.preventDefault()

    const data = {

        api_name:
        document.getElementById(
        "api_name").value,

        status:
        document.getElementById(
        "status").value,

        severity:
        document.getElementById(
        "severity").value,

        response_time:
        document.getElementById(
        "response_time").value
    }

    await fetch("/log",{

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },

        body:JSON.stringify(data)
    })

    location.reload()
})

async function simulateTraffic(){

    await fetch("/simulate")

    location.reload()
}

loadAnalytics()

loadLogs()

async function startSim() {

    await fetch("/start-sim");

    alert("Simulation started");
}

async function stopSim() {

    await fetch("/stop-sim");

    alert("Simulation stopped");
}

    
async function refreshCharts(){

    await fetch("/charts")

    const timestamp =
    new Date().getTime()

    document
    .getElementById("pieChart")
    .src =
    "/static/charts/pie.png?t=" + timestamp

    document
    .getElementById("barChart")
    .src =
    "/static/charts/bar.png?t=" + timestamp

    document
    .getElementById("lineChart")
    .src =
    "/static/charts/line.png?t=" + timestamp
}


setInterval(()=>{

    loadAnalytics()

    loadLogs()

    refreshCharts()

},5000)

