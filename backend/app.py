from fastapi import FastAPI
from scoring import calculate_shooting_score

app = FastAPI()

@app.post("/analyze")
def analyze_shot(pose_data: list):
    score = calculate_shooting_score(pose_data)
    return {"score": score, "feedback": "Improve follow-through"}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

