Feature:

Scenario:
  * url 'http://localhost:8000/'
  * path 'carts'
  * method get

Scenario:
  * url 'http://localhost:8000/'
  * path 'carts'
  * request { id: 10, products: [], created_at: "2023-06-22T16:16:13.009Z", updated_at: "2023-06-22T16:16:13.009Z" }
  * method post
  * status 200
  * match response.id == 10
  * def id = response.id

  * path 'carts', id 
  * method get
  * status 200 

Scenario:
  * url 'http://localhost:8000/'
  * def cart_id = 1
  * path 'carts', cart_id, 'products'
  * request { "title": "string", "price": 0, "description": "string", "category": "string", "image": "string", "rating": "string"}
  * method post
  * status 200

Scenario:
  * url 'http://localhost:8000/'
  * path 'products'
  * method get
  * match response[0].id == 1