here i am going to make a etl pipeline that is orchestrated with dagster

there are a few aspects to this project
- i have built a custom package that allows me to work with multiple apis and and my aws account
- this package needs to be installed in a virtual environment from the directory where it is
    - this means that wherever this datafin-etl project is you also need to install the datafin-package repo in a sibling directory
- once that is done adn a venv is activated and pip installed you need to install dagster and dagster0-webserver
- fruthermore you need to add the datafin package to the python path so dagster can use it
- you also need to create an .env file for you different environment variables 
