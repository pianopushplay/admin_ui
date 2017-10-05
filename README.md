# Admin UI for [Piano. Push. Play.](http://www.pianopushplay.com)

## App overview
### user / volunteer

 - CRUD pianos (TODO: clarify with Al, if volunteer can CRUD or just \_RU\_ )
### administrator / admin
 - CRUD pianos
 - CRUD users
 - CRUD other admins (stretch goal)


## APP logic
 - user:
    - upon login, redirect to pianos (pianos.html)

    - user can ~~search~~ choose any piano on pianos.html and get redirected to pianos/<piano-name>.html

    - user can edit piano details and save changes (the data is pre-filled with geolocation but gives the possibility to change them manually)

    - user sees piano details with a location map after saving changes

      ​

    - user can click any admins on adminslist.html and route to

      admins/id(admin_detail.html)

    - superuser can edit or delete an admin on admin_detail.html

- admin:
    - redirect to homepage home.html with options to 
      - CRUD users
      - CRUD pianos (flow just like users see)
      - CRUD admins (stretch)
    - admin can do all the tasks that user can do for pianos (TODO: plus create and delete, depends what Al says from TODO 1)
    - admin can add piano by clicking 'add piano' on a homepage or navigation menu 
    - admin can add users by clicking 'add user' on a homepage or navigation menu 
    - admin can edit or delete a piano on pianos/<piano-name>.html
    - embed google map on pianos/<piano-name>.html if the piano has geolocation data in the database
    - admin can create an admin by click 'add admin' on a homepage or navigation menu

- navigation:

    - List:	
        - admins: admins.html (only display to admins)
        - users: users.html (TODO: ask Al if users can see it)
        - pianos: pianos.html (display to all authenticated users)
    - Add:
        - add admin: admins/add.html (only display to admins)
        - add user: users/add.html (TODO: ask Al if users can see it)
        - add piano: pianos/add.html (display to all authenticated users)

- JSON data

    - generate JSON file that can be pulled by AL to be used in mobile apps (/pianos/json)

## To learn:

* JavaScript
* Geolocation (JS or HTML5)
* Uploading files
* Create JSON file
* (Stretch: auto-crop files for different screens, on a server)



## Technology used

- Flask framework
- Jinja2 templates 
- SQLAlchemy
- Flask-Migrate: db migration
- Flask-Login: user auth
- Flask-Bcrypt: hash password
- WTForms: form validation
- Bootstrap 4 
- JavaScript: get geoLocation (HTML5 Geolocation API might be a better choice, TODO: check mobile browsers support )
- AJAX: send data to back end (or just use form) ???


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