# flask_python_poc
Flask micro service with Peeweee


Steps to run POC:  
To start server, just execute the app.py:  
>> python app.py  

http://localhost:5000 -> default route  
http://localhost:5000/hello/ramit -> Route with paramater value  
http://localhost:5000/double/2 -> Flask takes care of converting num to the required data type  

## Learnings:

Flask is a micro-framework, its simple but extensible.  
It’s not just for small projects (Obama’s 2012 campaign used Flask).  
Flask doesn’t make decisions for you.  
By contrast, Ruby on Rails and Django make assumtions on how you want to interact with the databases.  

### Advantages:
Don’t have to worry about understndinf features you don’t get.  
Easy to add in extensions for things that you want.  
Templating gives dynamic html pages  

### Disadvantages:  
Less power out of the box  
Less standardised code (not enough help from net as compared to more commonly used frameworks)  

### Peewee: small ORM  
To install Peewee: >> sudo pip install peewee  
To use peewee module in code:  from peewee import *  

## Reources  
Flask:  http://flask.pocoo.org/docs/0.12/  
Peewee: http://docs.peewee-orm.com/en/latest/  

