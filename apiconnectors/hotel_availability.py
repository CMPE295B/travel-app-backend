import requests
import simplejson as json

class AvailableHotel(object):

	def __init__(self):
		BASE_URL = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/'
		CID = 55505
		API_KEY ='tadfyuhku8jpq3zdh5mcc9sg'
		LOCALE='en_US'
		CURRENCY_CODE='USD'
		#CUSTOMER_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko)"
		#CUSTOMER_IP_ADDRESS = '127.0.0.1'
		ARRIVAL_DATE = '10/12/2014'
		DEPARTURE_DATE = '10/15/2014'
		
		self._base_url = BASE_URL
		self._expedia_api_info = {
			"cid" : CID,
			"apiKey" : API_KEY,
			"locale" : LOCALE,
			"currencyCode" : CURRENCY_CODE,
			}
	
	def _serialize_reponse(self, data):
		return json.loads(data)
	
	def getHotelList(self, hotelId, numberOfAdults, arrival, departure):
		
		url = '%savail' % self._base_url
		print url + 'xxxxxxx'
		payload = {}
		for key, value in self._expedia_api_info.iteritems():
			payload[key] = value
		payload['hotelId'] = hotelId
		payload['room1'] = numberOfAdults
		payload['arrivalDate'] = arrival
		payload['departureDate'] = departure
		print url
		try:
			resp = requests.get(url, params = payload)
			print (resp.url) +"======================================="
		except Exception , ex:
			print ex.message
			raise ex
			
		if 200 <= resp.status_code <= 299:
			return self._serialize_reponse(resp.text)
		else:
			raise Exception(" Request Error!")
	
	def getRateKey(self, hotelId, numberOfGuests, arvl, depart):
		hotels = self.getHotelList(hotelId, numberOfGuests, arvl, depart)
		data = hotels
		return data['HotelRoomAvailabilityResponse']['rateKey']
	