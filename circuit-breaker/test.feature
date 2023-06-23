Feature:

Scenario:
  * url 'http://localhost:3000/'
  * path 'igv'
  * method get
  * status 200
  * match response.igv == 15