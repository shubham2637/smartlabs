
Getting Started
---------------
To get up and running, simply do the following:

    $ git clone git@github.com:shubham2637/smartlabs.git
    $ cd smartlabs

    # Install the requirements
    $ pip install -r requirements.txt



    # Perform database migrations if required
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Start the server
    $ python manage.py runserver
    
    Open bowser at http://127.0.0.1:8000
    Admin Login : http://127.0.0.1:8000/admin
                username : admin 
                password : admin
    

    #for Rest APIs
    method                      URL                                   Discription

**NOTE**: I highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).



<b>Assignment Problem Statement:</b><br>

## Task 1:

Create a View which will use https://free.currencyconverterapi.com/ API, to build a currency converter.

API documentation: https://www.currencyconverterapi.com/docs (You need to create a free account there)

**Input:**

The user will select the Base Currency, Currency to convert to from a dropdown and enter the amount of money to the form. for example: 

```python
input = {
    "base": "USD",
    "convert_to": "INR",
    "amount": "100"
}
```

**Output:**

Conversion Rate and converted amount.

## Task 2:

Given this model:

```python
class Order(models.Model):
    user = models.ForeignKey(
        'User',
        realted_name='orders',
        on_delete=models.CASCADE
    )
    discount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )


class Item(models.Model):
    name = models.Chafield(max_length=100)
    order = models.ForeignKey(
        'Order',
        realted_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )
```

**A. Develop a REST API (Django Rest Framework) which will list the orders by a specific user.**
 

The API response should look like:

```json
{
  "user": {
    "username": "new user",
    "email": "user@gmail.com"
  },
  "items": [
    {
      "name": "product 1",
      "price": "100.00",
      "quantity": 2,
      "total": "200.00"
    },
    {
      "name": "product 2",
      "price": "100.00",
      "quantity": 2,
      "total": "200.00"
    }
  ],
  "sub_total": "400.00",
  "total": "380.00",
  "discount": "20"
}
```

**B. Write the required database queries to get these analytics data:**
    
- Get total number of orders per users.
  
  `[{'user_id: 1, 'count': 100}, {'user_id: 2, 'count': 100}, ...]`
- Total orders per month. (for last 12 month's)
  
  `[{'month: 'January', 'count': 100}, {'month: 'February', 'count': 100}, ...]`
- Total revenue from orders per month. (for last 12 month's)
  
  `[{'month: 'January', 'revenue': 100.00}, {'month: 'February', 'revenue': 100.00}, ...]`


