import joblib
import pandas as pd

# Load the trained model
model = joblib.load(r"C:\Users\Pragya\Desktop\CGPA\cgpa_prediction_model.pkl")

# Load the dataset
df = pd.read_csv(r"C:\Users\Pragya\Desktop\CGPA\student_data.csv")

# Select only the feature columns (excluding CGPA)
X_new = df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours', 'Extracurricular']]

# Predict CGPA for all students
predicted_cgpa = model.predict(X_new)

# Add predictions to the dataset
df['Predicted_CGPA'] = predicted_cgpa

# Display results
print(df[['SGPA_Sem1', 'SGPA_Sem2', 'SGPA_Sem3', 'SGPA_Sem4', 'Attendance', 'Study_Hours', 'Extracurricular', 'Predicted_CGPA']])

# Save the results to a new CSV file
df.to_csv(r"C:\Users\Pragya\Desktop\CGPA\predicted_results.csv", index=False)

print("\nPredictions saved to 'predicted_results.csv'")
