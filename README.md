WeatherWatch24
WeatherWatch24 is a weather prediction and analysis project designed to predict weather for the next two weeks. By analyzing key weather features such as temperature and humidity, 
it determines whether weather phenomena like hurricanes, tornadoes, or floods are likely to occur. If such events are predicted, the project displays information on when and where they are likely to happen.

Features
Weather Prediction: Predicts the weather for the next two weeks based on real-time data.
Phenomenon Detection: Analyzes weather conditions to predict extreme weather events such as hurricanes, tornadoes, and floods.
Event Display: Provides detailed information on the predicted weather events, including the time and location.
Interactive Web Interface: Built using Flask for easy user interaction and weather updates.

Installation
Prerequisites
Make sure you have the following dependencies installed:

Python 3.x
Flask
Pandas
Requests
Scikit-learn
To install the necessary Python libraries, run the following command:

pip install pandas flask requests scikit-learn
Setup Instructions
Clone the repository:

Copy code
git clone https://github.com/yourusername/WeatherWatch24.git
Navigate into the project directory:

bash
Copy code
cd WeatherWatch24
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application: Start the Flask web server:

bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your browser.

Usage
After running the application, you can visit the local web server to interact with the project. The app will show predictions for the weather for the next two weeks, analyze the data, and display if any extreme weather events like hurricanes, tornadoes, or floods are likely to occur.

Example of using the prediction system:

python
Copy code
import requests

# Make a request to the weather API to get the next two weeks' weather data
response = requests.get('http://api.weatherapi.com/v1/forecast.json', params={
    'key': 'your_api_key',
    'q': 'location',
    'days': 14
})

weather_data = response.json()
# Use this data to predict extreme weather events
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License.


