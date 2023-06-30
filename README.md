# learning_python_django
First Step: Learn Python Django. 

Follow this tutorial: https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh

Left off at: 32:07/1:02:35

Notes:
- What is Django? 
  - Free and open source project that helps build web apps with python 
  - Have a lot of features
    - admin interface
    - object-relational mapper (ORM) Database manipulation ease
    - Authentication
    - Caching
  - Huge community

- Basics of Django
  - Frontend(FE)/CLient
    - Client sends request --> Web server --> Server sends back response
      - Best Practice: Have client generate Web Pages
    - Tools: React, Agular, Vue
  - Backend(BE)/Server
    - URL = uniform resource locator
    - HTTPS = Hyper Text Transfer Protocol: How clients and server communicates to one another
    - Functionality:
      - Sending back data
      - Sending back HTML document (or have client generate)
    - Tools: Django, ASP.NET Core, Express, JS
    - Build API from Django
  - Start Django Project with: `django-admin startproject <project_name>`
  - Run Django server with: `python3 manage.py runserver`
    - manage.py is the same as `django-admin`
  - Views:
    - file that stores request handlers, mapping request to url
    - Remember to set url configuration files and add it to main server's urls.py file