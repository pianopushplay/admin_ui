# Admin UI for [Piano. Push. Play.](http://www.pianopushplay.com)

## App overview
### volunteer
 - update pianos 
### administrator(admin)
 - CRUD pianos
 - CRUD users
 - CRUD other admins (stretch goal)


## APP logic
### Generics:
1. On pianos.html or volunteers.html, any authed parties can search with certain keywords
2. BASE_DIR : piaons.herokuapp.com(for example)
3. volunteers.html only show to admins
4. pianos.html shows to all authenticated parties
5. unauthed parties login go to pianos_on_map.html which is a map with all displayable pianos' location(route: BASE_DIR/) 
5. pianos API will be available at BASE_DIR/api/v1.0/pianos/

---
 - tasks for volunteers(vols):
    - login, goes to pianos.html with hyperlinked piano titles (route: admin/pianos)
    - click each piano on pianos.html and goes to piano_detail.html(route: admin/pianos/<int: piano_id>)
    - edit piano on piano_detail.html(route: admin/pianos/<int: piano_id>)
        - piano_detail.html loads with google map pined with current location
        - after done editing, redirect to piano_detail.html(route: admin/pianos/<int: pianos_id>) after done editing
---
- tasks for administrators(admins):
    - login, goes to volunteers.html(route: admin/volunteers)  
    - add vol: click 'add volunteer' on volunteers.html goes to volunteer_add.html (route:admin/volunteers/add)
        - after done adding, redirect to volunteer_detail.html(route: admin/volunteers/<int: vol_id>)
    - edit vol: click any vols on volunteers.html, goes to volunteer_detail.html(route: admin/volunteers/<int: vol_id>) 
        - after done editing, redirect to volunteer_detail.html(route: admin/volunteers/<int: vol_id>)
    - delete vol: click 'delete' on any volunteer_detail.html(route: admin/volunteers/<int: vol_id>) to deactive vols
        - after done delete, redirect to volunteers.html(route:admin/volunteers)
        
    - add piano: click 'add pianos' on pianos.html goes to pianos_add.html (route:admin/pianos/add)
        - after done adding, redirect to piano_detail.html(route: admin/pianos/<int: piano_id>)
    - edit piano: click any pianos on pianos.html, goes to pianos_detail.html(route: admin/pianos/<int: piano_id>) 
        - piano_detail.html load with google map pined with current location
        - after done editing, redirect to pianos_detail.html(route: admin/pianos/<int: piano_id>)
    - delete pianos: click 'delete' on any pianos_detail.html(route: admin/pianos/<int: piano_id>) to deactive pianos
        - after done delete, redirect to pianos.html(route:admin/pianos)
 
## To learn:

* JavaScript
* Geolocation (JS or HTML5)
* Uploading images
* Create JSON file
* (Stretch: auto-crop files for different screens, on a server)
* Update Github via python script (for JSON file) [https://developer.github.com/v3/repos/contents/#update-a-file](https://developer.github.com/v3/repos/contents/#update-a-file) 


## Technology used

- Flask framework
- Flask-Admin
- flask-security
- Flask-Migrate: db migration
- Flask-Bcrypt: hash password
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

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

git checkout -b the_issue_you_want_to_work_on
```

## Run server
```
python manage.py runserver 
```
