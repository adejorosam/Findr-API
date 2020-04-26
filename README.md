# Findr API


## Application Description
This is a simple API built for the sole purpose of finding a lasting solution to the myriads of a accomodation issues in O.O.U Ago-iwoye environs. Students don't find it easy in their search for apartment. It was for that purpose, that was why this API was built.

## Technologies used

Modern Python web technologies were adopted for this project

Django: Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit.
Visit [here](https://djangoproject.com/) for more information.



## Installation

```
git clone https://github.com/samson1998/Findr-API.git

cd Findr-API

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

python mange.py createsuperuser
```


## API Routes

<table>
<tr><th>HTTP VERB</th><th>ENDPOINT</th><th>FUNCTIONALITY</th></tr>
<tr><td>POST</td> <td>/api/v1/users</td>  <td>Creates a user</td></tr>
<tr><td>POST</td> <td>/api/v1/login</td>  <td>Login a user</td></tr>
<tr><td>POST</td> <td>/api/v1/users</td>  <td>Creates a user</td></tr>
<tr><td>PATCH</td> <td>/api/v1/users</td>  <td>Update a user</td></tr>
    
<tr><td>POST</td> <td>/api/v1/apartments</td>  <td>Creates a apartment</td></tr>
<tr><td>POST</td> <td>/api/v1/apartments</td>  <td>Get list of all apartments</td></tr>

<tr><td>GET</td> <td>/api/v1/users</td>  <td>View all users</td></tr>
<tr><td>GET</td> <td>/api/v1/users/{id}</td>  <td>View a particular user</td></tr>
<tr><td>GET</td> <td>/api/v1/apartments/{id}</td>  <td>View a particular apartment</td></tr>
<tr><td>PATCH</td> <td>/api/v1/users</td>  <td>Update a user</td></tr>
<tr><td>DELETE</td> <td>/api/v1/apartments/{id}</td>  <td>Delete a particular apartment</td></tr>




</table>
