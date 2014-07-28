import requests
try: import simplejson as json
except ImportError: import json

class HotelAPI(object):

	def __init__(self):
		BASE_URL = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/'
		MINOR_REV = 99
		CID = 55505
		API_KEY ='tadfyuhku8jpq3zdh5mcc9sg'
		LOCALE='en_US'
		TYPE = 'json&'
		CURRENCY_CODE='USD'
		COUNTRY_CODE = 'US'
		NUMBER_OF_RESULTS = 5
		SUPPLIER_CACHE_TOLERANCE = 'MED_ENHANCED'
		
		self._base_url = BASE_URL
		self._expedia_api_info = {
			"minorRev" : MINOR_REV,
			"cid" : CID,
			"apiKey" : API_KEY,
			"locale" : LOCALE,
			"_type" : TYPE,
			"currencyCode" : CURRENCY_CODE,
			"supplierCacheTolerance" : SUPPLIER_CACHE_TOLERANCE,
			"numberOfResults" : NUMBER_OF_RESULTS
			}
	
	def _serialize_reponse(self, data):
		return json.loads(data)
	
	def getHotelList(self, cityName, state, arrival, departure):
		
		url = '%slist' % self._base_url
		payload = {}
		for key, value in self._expedia_api_info.iteritems():
			payload[key] = value
		payload['city'] = cityName
		payload['stateProvinceCode'] = state
		payload['arrivalDate'] = arrival
		payload['departureDate'] = departure
		try:
			resp = requests.get(url, params = payload)
			print (resp.url)
		except Exception , ex:
			print ex.message
			raise ex
			
		if 200 <= resp.status_code <= 299:
			return self._serialize_reponse(resp.text)
		else:
			raise Exception(" Request Error!")