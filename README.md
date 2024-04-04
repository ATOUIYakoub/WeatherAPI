# WeatherAPI
This repository contains a simple weather API built using Django Rest Framework. The API allows users to retrieve weather information based on location queries. It integrates with a weather service provider to fetch real-time weather data from an third API called Open Weather (https://openweathermap.org/api).



## Overview
This is an API built with Django Rest Framework, and allows to retrieve real time weather data for any location including over 200,000 cities from a third API called Open Weather (https://openweathermap.org/api).

The API support GET requests in the following endpoint: <strong>/weather?city=$City&country=$Country&</strong>.

where the variable "City" is a string. Example: Valledupar, and the variable "Country" is a country code of two characters in lowercase. Example: co



## Key Technologies

This project uses the following Python dependencies:
* asgiref==3.8.1
* certifi==2024.2.2
* charset-normalizer==3.3.2
* Django==5.0.4
* djangorestframework==3.15.1
* idna==3.6
* python-dotenv==1.0.1
* requests==2.31.0
* sqlparse==0.4.4
* tzdata==2024.1
* urllib3==2.2.1
* xmltodict==0.13.0


## Quick Start
To run locally

```python
# Within a local folder, Clone this repository

$ git clone https://github.com/ATOUIYakoub/WeatherAPI.git

```

```python
# Create and activate a virtual environment in order to install the requirements.txt
python -m venv .env
.\env\Scripts\activate
pip install -r requirements.txt

```
```python
#Create a .env file**:
Create a file named `.env` in the root directory of your project. Add the following line to it:
WEATHER_SECRET_APIKEY=your_secret_api_key_here

#Load environment variables**:
In the requestapi.py file, before accessing the environment variables, load them from the `.env` file:

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.environ.get('WEATHER_SECRET_APIKEY')

```

```python
# Run the database migrations, this creates automatically a db.sqlite3 file
$python manage.py migrate

```
```python
# in order to using the database cache, you must 
# create the cache table with this command:
$python manage.py createcachetable

```
For caching this API uses a low-level cache API who is used to store objects in the database cache table.
The data stored will be available for 2 minutes.

```python
# Run the local server
$python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 04, 2024 - 07:55:11
Django version 5.0.4, using settings 'weatherAPI.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```


## Usage

> Open the browser and go to the endpoint and enter the  requested city and country.
ex:
  > Go to  http://127.0.0.1:8000/weather?city=Bougaa&country=dz


<img src="https://github.com/ATOUIYakoub/WeatherAPI.git/weatherAPI/images/weatherapi.png" width="700">




Author: ATOUI Abderahman Yakoub | 2024
