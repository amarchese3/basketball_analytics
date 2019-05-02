import requests


zillow_id='X1-ZWz1h0gpdmzj0r_2vy2l'
address='233 Grand St APT 3L, Hoboken, NJ'
citystate='07030'

url = 'http://www.zillow.com/webservice/GetSearchResults.htm?' \
      'zws-id=%s&address=%s&citystatezip=%s' % ( zillow_id, address, citystate)

response = requests.get(url).content

print(response)