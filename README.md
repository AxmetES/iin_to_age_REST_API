##IIN create and get defined age.
Project as test for a job.

##get start
install all requirements from ```requirements.txt```

##using
POST requests on ```/http://127.0.0.1:8000/api/people/```
with ```data = {'iin':'821119301118'}```

response ```{'iin':'821119301118','age':38}```

GET requests on ```/http://127.0.0.1:8000/api/people/```
with ```params = {'iin':'821119301118'}```

if exist :
response ```{'iin':'821119301118','age':38}```
