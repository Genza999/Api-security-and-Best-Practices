# Api-security-and-Best-Practices
A set of projects from the Udacity Api coaurses demonstrating how to create secure and developer-friendly Apis using python, SQLite and Flask

### Main Technologies Used

* Python
* Flask
* sqlite
* Virtual environment


### Use the following command to generate the requirements.txt file that includes all the external dependencies used in the development of the projects.
```
pip freeze >requirements.txt
```

### Use the command below to build a perfect replica of the virtual environment:

```
pip install -r requirements.txt
```

### The projects 

* #### Puppies
  This project shows the basic structure of Api endpoints in Flask.
  -Run endpoints_tester.py to test it out.

* #### MomandPopBagelShop project
  This project shows how to use the flask httpauth to implement basic user authentication on Api routes.
  -Run bagel_tester.py to test it out.

* #### RegalTreeFoods
  This project demonstrates using token-based authentication on login systems.
  -Run fruit_tester.py to test it out.

* #### BargainMart
  This project demonstrates usage of rate limit on an Api endpoint such that after 60 requests per minute, the hungryclient.py is denied service and is made to wait before sending any more requests.
  -Run hungryclient.py to send the requests.


### Author 

Kisekka David
