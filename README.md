# Mokeskin API

This is a service that provides an API to store objects/items. It's main purpose is to serve as a cache for temporary items.

**Python 3.7 >= (Recommended)**
**It uses Redis as main database to store the items**

## API Reference

**IMPORTANT: All the requests should add two extra queries in the url**

**tag_name: it's a prefix to be added to the item's key. ie: cm-spiders-**

**api_key: authorization**



**GET /exists/{key:.+}**

Check if `key` exists. It will return 404 status code if it doesn't. 200 if it does.


**GET /items/{key:.+}**

Returns an item (object) if it exists.

### Response example

```javascript

{'message': 'All OK',
 'data': {...item data...},
 'status': 'success'}

```


**POST /items**

Creates a new item or overwrite an existing one.

### Parameters

Content-Type: application/json

- *key* (required)
- *data* (a JSON object)
- *exp* (expiration time. Optional, in seconds.)

### Response example

```javascript

{'message': 'All OK',
 'data': {'key': <db key>},
 'status': 'success'}

```


**PUT /items**

Update an item data. It doesn't need all the fields included, only those to update.

### Parameters

Content-Type: application/json

- *key* (required)
- *data* (a JSON object)
- *exp* (expiration time. Optional, in seconds.)

### Response example

```javascript

{'message': 'All OK',
 'data': {...item data...},
 'status': 'success'}

```


**DELETE /items/{key:.+}**

Remove an item from the DB.

### Response example

```javascript

{'message': 'All OK',
 'data': {},
 'status': 'success'}

```


**GET /ttl/{key:.+}**

Get the current expiration time (in seconds) for an item.

### Response example

```javascript

{'message': 'All OK',
 'data': {'ttl': <seconds>},
 'status': 'success'}

```


## Develop

**You should have Python 3.7 >= installed (recommended, you could try with Python 3.5 >= but it's not recommended).**
**You should install the latest stable version of Redis too (https://redis.io/download)**

- Create a virtualenv for the project using the desired python binary: **virtualenv -p python3 --no-site-packages ~/Development/_env/mokeskin-api
**
- Clone this repo: **git clone git@bitbucket.org:competitormonitor/mokeskin-api.git**
- Install the dependencies: **pip install -r requirements.txt** (please remember to activate the proper vitualenv before...)


## Tests

To run the test you should have the project installed before.

- Run redis for testing using the redis_test.conf file in the repo: **redis-server redis_test.conf**
- Run the test server: **./run_test.sh**
- Now you can run the tests using *nose*: **nosetests -s tests/item.py** (the option **-s** is optional, it will show the print messages)
