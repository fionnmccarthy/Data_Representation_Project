# Data Representation Project </n>

# Project for module Data Representation Winter 2022 </n>

## Author: Fionn McCarthy - G00301126 </n>
---
This is my repository for the project assessment in the module. This project will contain a Web application in Flask that has a RESTful API, the application
links to two database tables: one which holds members details and another for admin users login details. There are web pages that consume the web API contained in the templates folder of the reposiory. 

The web API which I designed is for the Atlantic Technical University's Manchester United Supporters Club. It is designed for admin of the club to create, update and delete members from the clubs database. In order to enter the mmebers areas, it is required to pass the login authentification, which details are stored in the database table login_details. 


![xplotoutput](templates/images/standard.png)

---
### In order to run this web API please read the following.
1. Download and install **[[Anaconda](https://www.anaconda.com/products/individual)]**  
2. If using windows download and run **[[Cmder](https://cmder.net/)]** 
3. Download and install mysql. 
3. Download this repository.
4. There is file in this repository called requirements.txt where it will detail the necessary requirements to run the notebook, to create this I ran this command in command line: 'conda list -e > requirements.txt' command.
5. Inititially you will need to run the database file by typing 'python membershipDAO.py' on the command line which will create the database, the database tables and populate the database tables. 
6. Once this has been done you can now run the server file memberships.py by typing 'python memberships.py' and opening your browser to local host http://127.0.0.1:5000/ 
7. From here you will be able to login with username: admin1234 password: pwd0000 or else username: drtest2022 password: abcd1234
8. Form the memebrs area you will tehn be able to perform CRUD operations to the database in order to manage members of the club. 
---

