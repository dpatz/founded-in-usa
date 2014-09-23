# Founded In Romania

### Install PostgreSQL
```shell
sudo apt-get install postgresql postgresql-contrib pgadmin3
```
### Create a database user with full rights on it
```shell
sudo -u postgres createuser -D -A -P myuser
sudo -u postgres createdb -O myuser mydb
```
### Restart the PostgreSQL server
```shell
sudo /etc/init.d/postgresql restart
```

### Install the Python packages manager
```shell
sudo apt-get install python-pip
```
### Install virtualenv Python package
```shell
sudo pip install virtualenv
```
### Create virtualenv
```shell
cd founded-in-romania
virtualenv venv
```
### Activate virtualenv
```shell
source venv/bin/activate
```
### Install all necessary packages
```shell
pip install -r requirements.txt
```

### Tested
```shell
python run.py
```
Go to http://localhost:8080/ and to http://localhost:8080/data to populate the db