## IIN create and get defined age.
Project as test for a job.

## Get start
install all requirements from ```requirements.txt```

create DataBase ```python manage.py migrate```

start server ```python manage.py runserver```

## Using
### POST request
requests on [/http://127.0.0.1:8000/api/people/](/http://127.0.0.1:8000/api/people/)

with ```data = {'iin':'821119301118'}```

response ```{'iin':'821119301118','age':38}```

### GET request
requests on [127.0.0.1:8000/api/people/?iin=821119301118](127.0.0.1:8000/api/people/?iin=821119301118)

or 

GET requests on ```127.0.0.1:8000/api/people/```
with ```params = {'iin':'821119301118'}```

if exist :
response ```{'iin':'821119301118','age':38}```
