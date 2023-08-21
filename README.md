# Horoscope API


## Project Description
This application was made using Python, Beautiful Soup, and Flask-RESTX. The horoscope data is scraped from https://www.horoscope.com using Beautiful Soup, and is returned in JSON format using Flask-RESTX when the specific API endpoint is accessed. The goal of this project was to create an API, and use the said API as the backend for a web application that will call the API and display to the user their horoscope. The web application that uses the API can be accessed via [https://horoscopeapp.justintruong.studio](https://horoscopeapp.justintruong.studio).


## How to use the API
1. The first option is to visit the deployed API at [https://horoscopeapi-v6vga.ondigitalocean.app](https://horoscopeapi-v6vga.ondigitalocean.app).
    - A Swagger UI is generated that lets the user test out the API
        - Select a daily, weekly, or monthly horoscope
        - Click the Try it out button and enter in the parameters asked (such as animal/day or both depending on the endpoint chosen)
        - Click the Execute button to view the response body and response header
    
2. Another option is to access the full URL endpoint that will return the JSON data, such as visiting [https://horoscopeapi-v6vga.ondigitalocean.app/api/get-chineseHoroscope/monthly?animal=dragon](https://horoscopeapi-v6vga.ondigitalocean.app/api/get-chineseHoroscope/monthly?animal=dragon) for example. 


## Technology used
- Python, Beautiful Soup, and Flask-RESTX
- DigitalOcean to host the app

