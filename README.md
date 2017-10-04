## Admin UI for Pianospushplay

## App overview
### superuser
 - CRUD administrator
 - CRUD pianos
    
### administrator(admin)
 - CRUD pianos
 
 
## APP logic
 - superuser login:
    - redirect to admins/list(adminslist.html)
    - superuser can search any admins on adminslist.html
    - superuser create an admin by click 'create' on top of 
    adminslist.html and route to admins/create(admin_create.html)
    - superuser can click any admins on adminslist.html and route to
    admins/id(admin_detail.html)
    - superuser can edit or delete an admin on admin_detail.html
    
- admin login:
    - redirect to pianos/list(pianoslist.html)
    - admin can search any pianos on pianoslist.html
    - admin can add piano by click 'add' on top of 
    pianoslist.html and route to pianos/add(piano_add.html)
    - admin can click any pianos on pianoslist.html and route to
    pianos/id(piano_detail.html)
    - admin can edit or delete a piano on piano_detail.html
    - embed google map on piano_detail.html and show geolocation
    if geolocation is on
    
- navigation:
    - admins: adminslist.html(only display to superuser)
    - pianos: pianoslist.html(display to all authenticated users)
    
 
    
## Packages contributed to this app
- Flask: framework
- jinja2: templates 
- sqlalchemy: ORM
- flask-migrate: db migration
- flask-login: user auth
- flask-Bcrypt: hash password
- wtform: form validation
- Bootstrap: page style 
- javascript: get geoLocation
- AJAX: send data to back end(or just use form)


## How to contribute
```
git clone .... admin_ui

cd admin_ui

conda create -n yourenv

source activate yourenv

export DATABASE_URL='connection-to-your-db'
eg. :
export DATABASE_URL='mysql+pymysql://user:password@host:port/db_name'

python manage.py db migrate

python manage.py db upgrade

git checkout -b the_issue_you_want_to_work_on

```

## Run server
```
python manage.py runserver 
```
## Start coding

