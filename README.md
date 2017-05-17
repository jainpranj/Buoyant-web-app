# Buoyant-web-app

###Application connects to Buoyant IO 
###Kept separate from Buoyant IO code for loose coupling and failure of linkerd-tcp should not effect this application.

###Steps to run the application
##As normal flask web application
``python app.py``

or 
###Using docker-compose

``docker-compose up``

##Once Application is up use web page to check endpoints
``http://localhost:5000``


###Endpoints example

``http://localhost:5000/health``


``http://localhost:5000/shift?N=30``

