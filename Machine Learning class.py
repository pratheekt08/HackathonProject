import Pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Replace these with your Twilio credentials
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
TO_PHONE_NUMBER = 'recipient_phone_number'

# Function to send notification
def send_notification(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER
    )

# Load historical weather data
# Ensure your CSV file has appropriate columns: 'temperature', 'humidity', 'wind_speed', 'pressure', 'severe_storm'
data = pd.read_csv('historical_weather_data.csv')

# Preprocessing
# Assuming 'severe_storm' is the target variable (1 for storm, 0 for no storm)
X = data[['temperature', 'humidity', 'wind_speed', 'pressure']]
y = data['severe_storm']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 3: Predict for New Data
def predict_severe_storm(new_weather_data):
    # new_weather_data should be a DataFrame or array with same feature structure as training data
    prediction = model.predict(new_weather_data)
    return prediction

# Step 4: Example Prediction (Replace with your actual new weather data)
new_data = pd.DataFrame({
    'temperature': [30],  # Example temperature
    'humidity': [80],     # Example humidity
    'wind_speed': [20],   # Example wind speed
    'pressure': [1010]    # Example pressure
})

# Predict
storm_prediction = predict_severe_storm(new_data)
if storm_prediction[0] == 1:
    send_notification("Alert: A severe storm is predicted based on the latest weather data!")
else:
    send_notification("No severe storm predicted based on the latest weather data.")
