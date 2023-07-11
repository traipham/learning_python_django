# learning_python_django
First Step: Learn Python Django.

1. Follow this tutorial: https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh  [COMPLETE!]
2. Follow next tutorial for Django (7 hrs): https://www.youtube.com/watch?v=PtQiiknWUcI&ab_channel=TraversyMedia
3. Follow this tutorial for React (1 hr): https://www.youtube.com/watch?v=b9eMGE7QtTk&ab_channel=JavaScriptMastery [COMPLETE!]
4. Follow this tutorial for React + Django (3 hrs): https://www.youtube.com/watch?v=tYKRAXIio28&ab_channel=DennisIvy
5. Follow this tutorial for React + Django (3 hrs): https://www.youtube.com/watch?v=kfpY5BsIoFg&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60&index=7&ab_channel=TraversyMedia
6. Follow this tutorial for React (11 hrs) : https://www.youtube.com/watch?v=bMknfKXIFA8&ab_channel=freeCodeCamp.org 

# Notes:
- **What is Django**? 
  - Free and open source project that helps build web apps with python 
  - Have a lot of features
    - admin interface
    - object-relational mapper (ORM) Database manipulation ease
    - Authentication
    - Caching
  - Huge community

- **Basics of Django**
  - *Frontend(FE)/CLient*
    - Client sends request --> Web server --> Server sends back response
      - Best Practice: Have client generate Web Pages
    - Tools: React, Agular, Vue
  - *Backend(BE)/Server*
    - URL = uniform resource locator
    - HTTPS = Hyper Text Transfer Protocol: How clients and server communicates to one another
    - Functionality:
      - Sending back data
      - Sending back HTML document (or have client generate)
    - Tools: Django, ASP.NET Core, Express, JS
    - Build API from Django
  - **Start Django Project** with: `django-admin startproject <project_name>`
  - **Run Django server** with: `python3 manage.py runserver`
    - manage.py is the same as `django-admin`
  - **Views**:
    - file that stores request handlers, need to map request to url
    - Remember to set url configuration files and add it to main server's urls.py file
  - **Template**: 
    - Allows us to return HTML markup pages 
    - Don't usually use Template with Django
  - **Debug**: 
    - Use VsCode debugger, open server to see page, and add breakpoints
    - Use Django Debug toolbar ([Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/))
  - **Models**:
    - Used to store and retrieve data
    - Data modeling
      - Know the product's attributes: {title, description, price, inventory}
      - Relationships between data tables:
        - 1-to-1
        - 1-to-many
          - Ex: Cart table that takes many CartItem table
        - many-to-many
          - Ex: Multiple Product that can be in multiple collections table, and collection table can have multiple products
      - ID attribute is automatically created in Django
      - Ex: Data modeling for e-commerce 
      - Organizing Data Models in app:
        1. App that contains all data model collection
           1. BAD: Not good for big projects and for scaling
        2.  Break down project to smaller apps, each with differnet data models
            1.  BAD: Need to install one by one and updating each apps
            2.  Should bundle these smaller apps together
        3. Minimal Coupling and high focus on a specific functionality (including all pieces to run that functionality)