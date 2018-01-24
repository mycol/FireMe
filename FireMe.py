import requests
import json
import jsonp2json

jsonp_response = requests.get('http://sonomatech-production.s3.amazonaws.com/sacramento/airquality_org/cbyb-widget/burncheckForecast.txt')
json_result = jsonp2json.convert(jsonp_response.text)

forecast = json.loads(json_result)

aqi_today = forecast['burn_forecast']['today']['aqi']
aqi_tomorrow = forecast['burn_forecast']['tomorrow']['aqi']
cat_today = forecast['burn_forecast']['today']['category']
cat_tomorrow = forecast['burn_forecast']['tomorrow']['category']

if cat_today == 6:
    print("All Burning is Allowed Today. The Air Quality Index (AQI) High Today is {}.".format(aqi_today))
elif cat_today == 7:
    print("Burning is Discouraged Today. The Air Quality Index (AQI) High Today is {}.".format(aqi_today))
elif cat_today == 8:
    print("Stage 1 No Burn Unless Exempt. The Air Quality Index (AQI) High Today is {}.".format(aqi_today))
else:
    print("Stage 2 No Burn, All Burning Prohibited. The Air Quality Index (AQI) High Today is {}.".format(aqi_today))
