# Api-security-and-Best-Practices
A set of projects from the Udacity Api coaurses demonstrating how to create secure and developer-friendly Apis using python, SQLite and Flask

### Technologies Used

* [Python](https://www.python.org)
* [Flask](http://flask.pocoo.org/)
* [sqlite](https://www.sqlite.org/)
* [itsdangerous](https://pythonhosted.org/itsdangerous/) - Cryptographically secure token generation and verification
* [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth) - Provide Basic and Digest HTTP authentication for Flask routes.
* [passlib](https://passlib.readthedocs.io/en/stable/) - password hashing library for Python 2 & 3


### First Use the command below to build a perfect replica of the virtual environment:

```
pip install -r requirements.txt
```

### The projects 

* #### Puppies
  This project shows the basic structure of Api endpoints in Flask.

  Within the Puppies directory, Run the following command to start the local server. 
  ```
  python endpoints.py
  ```
  Then in a new terminal, Run the following command to test the Api's.
  ```
  python endpoints_tester.py
  ```

* #### MomandPopBagelShop project
  This project shows how to use the flask httpauth to implement basic user authentication on Api routes.

  Within the MomandPopBagelShop directory, Run the following command to start the local server. 
  ```
  python views.py
  ```
  Then in a new terminal, Run the following command to test flask httpauth user authentication functionality imposed on the api routes.
  ```
  python bagel_tester.py
  ```

* #### RegalTreeFoods
  This project demonstrates using token-based authentication on login systems.

  Within the RegalTreeFoods directory, Run the following command to start the local server. 
  ```
  python views.py
  ```
  Then in a new terminal, Run the following command to test the token-based authentication functionality imposed on the api routes.
  ```
  python fruit_tester.py
  ```

* #### BargainMart
  This project demonstrates usage of rate limit on an Api endpoint such that after 60 requests per minute, the hungryclient.py is denied service and is made to wait before sending any more requests.
  
  Within the BargainMart directory, Run the following command to start the local server. 
  ```
  python views.py
  ```
  Then in a new terminal, Run the following command to test the Rate Limit imposed on the getcatalog route api.
  ```
  python hungryclient.py
  ```

  #### Enjoy
