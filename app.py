from Flask import flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    try:
        # Get the WOEID (Where On Earth ID) for the city
        woeid_response = requests.get(f"https://www.metaweather.com/api/location/search/?query={city}")
        
        if woeid_response.status_code != 200:
            return jsonify({'error': 'City not found or unable to fetch WOEID.'}), woeid_response.status_code
        
        woeid_data = woeid_response.json()
        
        if not woeid_data:
            return jsonify({'error': 'City not found.'}), 404
        
        woeid = woeid_data[0]['woeid']
        
        # Fetch the weather data using the WOEID
        weather_response = requests.get(f"https://www.metaweather.com/api/location/{woeid}/")
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            consolidated_weather = weather_data['consolidated_weather'][0]
            
            # Return additional details
            return jsonify({
                'city': weather_data['title'],
                'temperature': consolidated_weather['the_temp'],
                'weather': consolidated_weather['weather_state_name'],
                'humidity': consolidated_weather['humidity'],
                'wind_speed': consolidated_weather['wind_speed'],
                'icon': f"https://www.metaweather.com/static/img/weather/png/{consolidated_weather['weather_state_abbr']}.png"
            })
        else:
            return jsonify({'error': 'Failed to retrieve data from the weather API.'}), weather_response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching data: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)




