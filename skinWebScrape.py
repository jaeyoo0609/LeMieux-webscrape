#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#importing modules
import requests
import json
import csv

with open('OrangeCounty25MileRadius.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['Name', 'Location', 'Rating', 'Contact'])

    #define business id
    business_id ='HuaI3akdTuzM1MJXLV3Qbg'

    #define the API key, define the endpoint, and define the header
    API_KEY = 'Bfj52f3IPqzUJS1bjWTb5aHfTRgFSGDbpZ4a7DuatM9Y0KFGxm4ifUbvHdhzRuhklbZcIx1ZtSWEWaaLuwN3nU2IuhrjIEnhT1I3i2bVQo7_kpF9-VhI-hzjjw_pXnYx'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    #Authenticating oneself to the Yelp API
    HEADERS = {'Authorization' : 'bearer %s' % API_KEY}
    OFFSET = 0
    while OFFSET < 1000:
        #Define the parameters
        PARAMETERS = {
            'term' : 'skin care',
            'limit' : 50,
            'radius' : 40000,
            'offset' : OFFSET,
            'location' : 'Orange County'
        }

        #Making request to Yelp API
        response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

        #convert json string to dict
        business_data = response.json()

        #print(business_data.keys())

        for biz in business_data['businesses']:
            location = biz['location']
            if location is None:
                location = ''
            
            city = location['city']
            if city is None:
                city = ''
            
            address = location['address1']
            if address is None:
                address = ''
            state = location['state']
            if state is None:
                state = ''
            zipcode = location["zip_code"]
            if zipcode is None:
                zipcode = ''

            thewriter.writerow([biz['name'], address + ', ' + city + ', ' + state + ', ' + zipcode, str(biz['rating']), biz['phone']])
        OFFSET += 50

