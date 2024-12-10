from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend's URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("static/index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.post("/calculate")
async function calculateGPA() {
    const rows = document.querySelectorAll("#courses-table tbody tr");
    const courses = [];

    rows.forEach(row => {
        const credit = row.querySelector("td:nth-child(1) input").value;
        const grade = row.querySelector("td:nth-child(2) select").value;

        if (credit && grade) {
            courses.push({ credit: parseFloat(credit), grade: parseFloat(grade) });
        }
    });

    try {
        const response = await fetch("https://gpa-calculator-seven-sigma.vercel.app/api/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ courses })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById("gpa-result").textContent = `Your GPA is: ${result.gpa}`;
    } catch (error) {
        console.error("Error fetching data:", error);
        document.getElementById("gpa-result").textContent = "An error occurred while calculating GPA.";
    }
}
