# Findr API


## Application Description
This is a simple API built for the sole purpose of finding a lasting solution to the myriads of a accomodation issues in O.O.U Ago-iwoye environs. Students don't find it easy in their search for apartment. It was for that purpose, that was why this API was built.

## Features
Below are the features of my WEconnect app

Organizers(user) can create event<br/>
Organizers(user) can delete event<br/>
Users can register to attend an event<br/>
Users can unregister from attedning an event<br/>



## Technologies used

Modern Python web technologies were adopted for this project

Django: Laravel is a web application framework with expressive, elegant syntax. We’ve already laid the foundation — freeing you to create without sweating the small things.
Visit [here](https://laravel.com/) for more information.



## Installation

```
git clone https://github.com/samson1998/Findr-API.git

cd file

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
    
<tr><td>POST</td> <td>/api/v1/meeting</td>  <td>Creates a meeting</td></tr>
<tr><td>POST</td> <td>/api/v1/registration</td>  <td>Register for a meeting</td></tr>

<tr><td>GET</td> <td>/api/v1/users</td>  <td>View all users</td></tr>
<tr><td>GET</td> <td>/api/v1/users/{id}</td>  <td>View a particular user</td></tr>
<tr><td>GET</td> <td>/api/v1/meeting/{id}</td>  <td>View a particular meeting</td></tr>
<tr><td>PATCH</td> <td>/api/v1/users</td>  <td>Update a user</td></tr>
<tr><td>DELETE</td> <td>/api/v1/meeting/{id}</td>  <td>Delete a particular meeting</td></tr>
<tr><td>DELETE</td> <td>/api/v1/registration/{id}</td>  <td>Unregister from a particular meeting</td></tr>



</table>
