# backend/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/calculate")
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
    return JSONResponse({"gpa": round(gpa, 2)})
