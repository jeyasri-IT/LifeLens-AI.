import pandas as pd
import numpy as np

# Reproducible results
np.random.seed(42)

rows = 10000

# Generate data
age = np.random.randint(18, 60, rows)
gender = np.random.choice(["Male", "Female"], rows)
sleep = np.round(np.random.uniform(4, 9, rows), 1)
screen = np.round(np.random.uniform(1, 12, rows), 1)
exercise = np.random.randint(0, 121, rows)
water = np.round(np.random.uniform(1, 5, rows), 1)
study = np.round(np.random.uniform(2, 12, rows), 1)
stress = np.random.randint(1, 11, rows)
mood = np.random.choice(["Happy", "Neutral", "Sad", "Stressed"], rows)

# Productivity formula
productivity = (
    sleep * 10
    + exercise * 0.2
    + water * 5
    - screen * 2
    - stress * 4
    + study * 2
)

# Limit values between 0 and 100
productivity = np.clip(productivity, 0, 100)

# Burnout Risk
burnout = []

for p in productivity:
    if p >= 75:
        burnout.append("Low")
    elif p >= 50:
        burnout.append("Medium")
    else:
        burnout.append("High")

# Create DataFrame
df = pd.DataFrame({
    "Age": age,
    "Gender": gender,
    "Sleep_Hours": sleep,
    "Screen_Time": screen,
    "Exercise_Minutes": exercise,
    "Water_Intake": water,
    "Work_Study_Hours": study,
    "Stress_Level": stress,
    "Mood": mood,
    "Productivity_Score": productivity,
    "Burnout_Risk": burnout
})

# Save CSV
df.to_csv("life_data.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())
