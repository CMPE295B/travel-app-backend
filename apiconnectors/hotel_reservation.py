#! /usr/bin/python

import requests
import json

class HotelBookingAPI(object):

	def __init__(self):
		BASE_URL = 'https://book.api.ean.com/ean-services/rs/hotel/v3/'
		MINOR_REV = 99
		CID = 55505
		API_KEY ='tadfyuhku8jpq3zdh5mcc9sg'
		LOCALE='en_US'
		CURRENCY_CODE='USD'
		CUSTOMER_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko)"
		CUSTOMER_IP_ADDRESS = '127.0.0.1'
		USER_SESSION_ID = 'uniquesessionid'
		self._base_url = BASE_URL
		self._expedia_api_info = {
			"minorRev" : MINOR_REV,
			"cid" : CID,
			"customerUserAgent" : CUSTOMER_USER_AGENT,
			"customerIpAddress" : CUSTOMER_IP_ADDRESS,
			"customerSessionId" : USER_SESSION_ID,
			"apiKey" : API_KEY,
			"locale" : LOCALE,
			"currencyCode" : CURRENCY_CODE,
			}
	
	def _serialize_reponse(self, data):
		return json.loads(data)
	
	def bookHotel(self, hotelOrder):
		
		url = '%sres' % self._base_url
		payload = {}
		for key, value in self._expedia_api_info.iteritems():
			payload[key] = value
		print url

		payload['hotelId'] = hotelOrder['hotelId']
		payload['arrivalDate'] = hotelOrder['arrivalDate']
		payload['departureDate'] = hotelOrder['departureDate']
		payload['supplierType'] = hotelOrder['supplierType']
		payload['rateKey'] = hotelOrder['arrivalDate']
		payload['roomTypeCode'] = hotelOrder['roomTypeCode']
		payload['rateCode'] = hotelOrder['rateCode']
		payload['chargeableRate'] = hotelOrder['chargeableRate']
		payload['room1'] = hotelOrder['room1']
		payload['room1FirstName'] = hotelOrder['room1FirstName']
		payload['room1LastName'] = hotelOrder['room1LastName']
		payload['room1BedTypeId'] = hotelOrder['room1BedTypeId']
		payload['room1SmokingPreference'] = hotelOrder['room1SmokingPreference']
		payload['email'] = hotelOrder['email']
		payload['firstName'] = hotelOrder['firstName']
		payload['lastName'] = hotelOrder['lastName']
		payload['homePhone'] = "2145370159"
		payload['workPhone'] = "2145370159"
		payload['creditCardType'] = "CA"
		payload['creditCardNumber'] = "5401999999999999"
		payload['creditCardIdentifier'] = "123"
		payload['creditCardExpirationMonth'] = "11"
		payload['creditCardExpirationYear']= "2016"
		payload['address1'] = "travelnow"
		payload['city'] = hotelOrder['city']
		payload['stateProvinceCode'] = hotelOrder['stateProvinceCode']
		payload['countryCode'] = "US"
		payload['postalCode'] = hotelOrder['postalCode']
		
		headers = {'content-type': 'application/json'}
		print url
		try:
			resp = requests.post(url, params = payload, headers = headers)
			print (resp.url)
			print (resp.status_code)
		except Exception , ex:
			print ex.message
			raise ex
			
		if 200 <= resp.status_code <= 299:
			return self._serialize_reponse(resp.text)
		else:
			raise Exception(" Request Error!")