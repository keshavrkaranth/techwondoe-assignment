[TECHWONDOE ASSIGNMENT]
* Create a Django Rest Framework Application to expose a few API's and also design and implement supporting database tables.

# To run project:
* Make sure docker is installed in your pc
* run command docker-compose build
* then run docker-compose up 
* hurray your local server is running in `http://127.0.0.1:8000/api/`

The main routes are
* /api/login
* /api/register
* /api/companys
* /api/teams


Additional routes if you go to /api/teams/allteams you will find all the details of teams In a array WRT to Company ID

if are new user I suggest you to register your self
sample Payload for registering user
{
    "name":"Jhon",
    "email":"email@gmail.com",
    "phone":"1234567890",
    "password":"1234",
    "is_superadmin":true
}

you'll receive a jwt token to access further routes 

If you go to company and team routes from chrome the Django Rest Framework's UI is self-explanatory you can perform the actions that you have told

for better understanding of API I have added swagger ui to access this go to http://127.0.0.1:8000/swagger/ you can get details of all routes

Note I have Used postgres:13.0-alpine Image for Postgrese Database and Data is Consistent if you restart the server then also data won't be lost