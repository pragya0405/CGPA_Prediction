import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r"C:\Users\Pragya\Desktop\CGPA\student_data.csv")

# Split data into features (X) and target (y)
X = df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours', 'Extracurricular']]
y = df['CGPA']

# Split into training & testing sets (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Model Performance
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:\nMAE: {mae}\nMSE: {mse}\nR² Score: {r2}")

# Save the trained model
print("Saving model...")  # Debug print
try:
    joblib.dump(model, r"C:\Users\Pragya\Desktop\CGPA\cgpa_prediction_model.pkl")
    print("Model saved successfully!")
except Exception as e:
    print(f"Error saving model: {e}")
