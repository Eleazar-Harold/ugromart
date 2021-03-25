# [UGROMART Project]
###### UgroMart is a platform connecting customers to local market vendors. Users can sign up, view market vendors and purchase local produce like food, fruits and vegetables. UgroMart is an end to end solution that handles payments, deliveries, product and order management.


### Technology Stack
* [FastAPI](https://fastapi.tiangolo.com/), 
* [Python](https://www.python.org/downloads/release/python-3710) Python 3.7.10,
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest) to manage all dependencies (and sub-dependencies)


### Project structure:
```
.
├── ugromart
    ├── delivery-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── deliveryconfirmation-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── deliveryitem-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── deliverystatus-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── order-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── orderassignment-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── orderitem-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── payment-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── product-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── productcategory-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── productitem-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── productvariation-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── unitofmeasure-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── user-service
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── app
    ├── .dockerignore
    ├── .env.example
    ├── .gitignore
    ├── Makefile
    ├── nginx_config.conf
    ├── docker-compose.yml

```

### Project setup
###### Assuming docker is pre-installed

###### Environment File
Example `.env.example` file:

```bash
PG_PSWD_DLVR=
PG_USER_DLVR=delivery

PG_PSWD_ORDE=
PG_USER_ORDE=order

PG_PSWD_PRDS=
PG_USER_PRDS=product

PG_PSWD_UOMS=
PG_USER_UOMS=uom

# Delivery Services Url
DELIVERY_SERVICE_URL = "http://.../api/v1/deliveries/"
DELIVERYSTATUS_SERVICE_URL="http://.../api/v1/deliverystatus/"

# Order Services Url
ORDER_SERVICE_URL="http://.../api/v1/orders/"

# Payment Services Url
PAYMENT_SERVICE_URL="http://.../api/v1/payments/"

# Product Services Url
PRODUCT_SERVICE_URL="http://.../api/v1/products/"
CATEGORY_SERVICE_URL="http://.../api/v1/categories/"
PRODUCTITEM_SERVICE_URL="http://.../api/v1/productitems/"
VARIATION_SERVICE_URL = "http://.../api/v1/variations/"

# UnitOfMeasure Services Url
UOM_SERVICE_URL= "http://.../api/v1/unitofmeasures/"

```

##### Api Access path for all the services
```
default http path: http://127.0.0.1/api/v1/{service}/docs
```
###### Service names
* deliveries :       ```from delivery-service```
* confirmations :    ```from deliveryconfirmation-service```
* deliveryitems :    ```from deliveryitem-service```
* orders :           ```from order-service```
* orderassignments : ```from orderassignment-service```
* orderitems :       ```from orderitem-service```
* products :         ```from product-service```
* categories :       ```from productcategory-service```
* productitems :     ```from productitem-service```
* variations :       ```from productvariation-service```
* unitofmeasures :   ```from unitofmeasure-service```
* auth :            ```from user-service```

###### WIP services
* payments :         ```from payment-service```
* deliverystatus :   ```from deliverystatus-service```

##### Development/Production environment propagation
```
make stack
```

##### Development/Production environment destroy
```
make tearstack
```

### Contribution guidelines

* Code review
* Other guidelines
* Contact [repo owner](mailto:haroldyewa@gmail.com) for more details.