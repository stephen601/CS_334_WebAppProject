# CS 334 Team Pages Repository
## 1. Web Addresses:
  * https://stephen601.github.io/CS_334_WebAppProject/
  * https://revisionary-cockpit.000webhostapp.com/

## 2. Links: 
  * [Home Page](https://stephen601.github.io/CS_334_WebAppProject/)
  * [Manager Page](https://stephen601.github.io/CS_334_WebAppProject/manager)
  * [Login Page](https://stephen601.github.io/CS_334_WebAppProject/login)
## 3. Notes:
  * None at the moment.
## 4. API Instructions 
  ### https://teamcs334.pythonanywhere.com/ice_cream
  * GET will show all ice cream
  * POST will add a new flavor
    * POST required variables: name, image, and price
  ### https://teamcs334.pythonanywhere.com/ice_cream/<ice_cream_id>
  * Ex:https://teamcs334.pythonanywhere.com/ice_cream/1
  * GET will show the ice cream with the provided ice_cream_id
  * PUT will modify that ice cream's data based of ice_cream_id
    * PUT required variables: name, image, and price
  * DELETE will delete that ice cream's data based of ice_cream_id
  ### https://teamcs334.pythonanywhere.com/user
  * GET will show all users
  * POST will add a new user
    * POST required variables: username, password, and is_admin(boolean)
  ### https://teamcs334.pythonanywhere.com/user/<user_id>
  * Ex:https://teamcs334.pythonanywhere.com/user/1
  * GET will show the user with the provided user id.
  * PUT will update the user info with the provided user id.
    * PUT required variables: username, password, and is_admin(boolean)
  * DELETE will delete the user of the provided user id.
  ### https://teamcs334.pythonanywhere.com/orders
  * GET will show all orders
  * POST will add a new order
    * POST required variables: user_id, quantity, total_price, order_date, and ice_cream_id
  ### https://teamcs334.pythonanywhere.com/orders/<order_id>
  * Ex:https://teamcs334.pythonanywhere.com/orders/8
  * GET will show the order of the order id provided
  * PUT will update the order of the order if provided
    * PUT required variables: user_id, quantity, total_price, order_date, and ice_cream_id
  * DELETE will delete the order of the order id provided.
  ### http://teamcs334.pythonanywhere.com/send_email
  * POST will send an email with order information.
