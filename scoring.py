import numpy as np

def calculate_shooting_score(pose_landmarks):
    # Example: Check elbow angle during shot release
    elbow_angle = np.linalg.norm(pose_landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW])
    
    if 75 <= elbow_angle <= 90:
        return 100  # Perfect form
    elif 60 <= elbow_angle < 75 or 90 < elbow_angle <= 110:
        return 75  # Needs improvement
    else:
        return 50  # Poor form

# Example: Run AI scoring on sample pose data
sample_pose = np.array([80])  # Mocked pose data
score = calculate_shooting_score(sample_pose)
print(f"Shooting Form Score: {score}/100")

