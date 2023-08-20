# What is this?

It is a specially developed pagination class to enable data to be paginated when we search with elasticsearch while using Django rest framework.


## Usage

- Locate the pagination.py file inside your project.
- Add the following code to your settings.py file.
```python
REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}
```
- Apply the example usage in the exp_views.py file to your own views.
- Sample requests;
```
    http://api.example.org/accounts/?page=4
    http://api.example.org/accounts/?page=4&page_size=100
```
- Sample response;
```json
   {
    "count": 130,
    "next": "http://api.example.org/accounts/?page=4&page_size=25",
    "previous": "http://api.example.org/accounts/?page=2&page_size=25",
    "results": [
      {},
      {}
    ]
}
```

