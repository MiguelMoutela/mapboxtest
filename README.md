# Simple geocoding app in Flask


Adding markers to Mapbox map: https://www.mapbox.com/help/markers-js/



Sample Census Reporter geocode call:

https://github.com/censusreporter/census-api/blob/master/API.md


https://api.censusreporter.org/1.0/geo/search?lat=34.154551&lon=-117.302247


```py
import requests
BASE_ENDPOINT = 'https://api.censusreporter.org/1.0/geo/search'
myparams = {'lat': 34.154551, 'lon': -117.302247}

resp = requests.get(BASE_ENDPOINT, params=myparams)
```


# Sample census decennial

https://www.census.gov/data/developers/data-sets/decennial-census.html

https://api.census.gov/data/2000/sf3?get=P087001,P052017,NAME&for=state:06



# Sample census api call ACS


http://www.census.gov/data/developers/data-sets/acs-survey-5-year-data.html



Santa Clara County, median per capita income, median household, total pop, total households, for 2009:

http://api.census.gov/data/2009/acs5?for=county:085&in=state:06&get=B06011_001E,B19013_001E,B01003_001E,B11011_001E


For tracts within a state (California)

http://api.census.gov/data/2009/acs5?for=tract:*&in=state:06&get=B01003_001E,B11011_001E,B11011_002E,B11011_004E
