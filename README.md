## Admin UI for pianospushplay

## App overview
### superuser
 - CRUD administrator
 - CRUD pianos
    
### administrator
 - CRUD pianos

## Packages contributed to this app
- Flask
- jinja2: templates 
- sqlalchemy: ORM
- flask-migrate: db migration
- flask-login: user auth
- flask-Bcrypt: hash password
- wtform: form validation
- Bootstrap: page style 
- javascript: get geoLocation
- AJAX: send data to back end(or just use form)


## How to contribute:
```

git clone .... admin_ui

cd admin_ui

conda create -n yourenv

source activate yourenv

export DATABASE_URL='connect-to-your-db'
eg. :
export DATABASE_URL='mysql+pymysql://user:password@host:port/db_name'

python manage.py db migrate

python manage.py db upgrade

```

## Run server:
`python manage.py runserver`

