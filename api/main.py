from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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

@app.post("/api/calculate")
async def calculate_gpa(data: Request):
    body = await data.json()
    courses = body.get("courses", [])
    
    total_credits = 0
    weighted_score = 0

    for course in courses:
        credit = float(course.get("credit", 0))
        grade = float(course.get("grade", 0))
        total_credits += credit
        weighted_score += credit * grade

    gpa = weighted_score / total_credits if total_credits > 0 else 0
    return JSONResponse({"gpa": round(gpa, 4)})
