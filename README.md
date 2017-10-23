# Admin UI for [Piano. Push. Play.](http://www.pianopushplay.com)

The live demo on: [python anywhere](http://adrianacmy.pythonanywhere.com)

## App overview

### volunteer
 - update pianos 
### administrator (admin)
 - CRUD pianos
 - CRUD users
 - CRUD other admins (stretch goal)


## APP logic
### Generics:
1. On pianos.html or volunteers.html, any authed parties can search with certain keywords
2. BASE_DIR: pianos.herokuapp.com (for example)
3. volunteers.html only visible to admins
4. pianos.html visible to all authenticated parties
5. unauthenticated parties login go to pianos_on_map.html which is a map with all displayable pianos' locations (route: BASE_DIR/) 
6. pianos API will be available at BASE_DIR/api/v1.0/pianos/

---
 - tasks for volunteers (vols):
    - login, goes to pianos.html with hyperlinked piano titles (route: admin/pianos)
    - click each piano on pianos.html and goes to piano_detail.html (route: admin/pianos/<int: piano_id>)
    - edit piano on piano_detail.html (route: admin/pianos/<int: piano_id>)
        - piano_detail.html loads with google map pined with current location
        - after done editing, redirect to piano_detail.html (route: admin/pianos/<int: pianos_id>) after done editing
---
- tasks for administrators (admins):
    - login, goes to volunteers.html (route: admin/volunteers)  
    - add vol: click 'add volunteer' on volunteers.html goes to volunteer_add.html (route:admin/volunteers/add)
        - after done adding, redirect to volunteer_detail.html (route: admin/volunteers/<int: vol_id>)
    - edit vol: click any vols on volunteers.html, goes to volunteer_detail.html (route: admin/volunteers/<int: vol_id>) 
        - after done editing, redirect to volunteer_detail.html (route: admin/volunteers/<int: vol_id>)
    - delete vol: click 'delete' on any volunteer_detail.html (route: admin/volunteers/<int: vol_id>) to deactive vols
        - after done delete, redirect to volunteers.html (route:admin/volunteers)

    - add piano: click 'add pianos' on pianos.html goes to pianos_add.html (route:admin/pianos/add)
        - after done adding, redirect to piano_detail.html (route: admin/pianos/<int: piano_id>)
    - edit piano: click any pianos on pianos.html, goes to pianos_detail.html (route: admin/pianos/<int: piano_id>) 
        - piano_detail.html load with google map pined with current location
        - after done editing, redirect to pianos_detail.html (route: admin/pianos/<int: piano_id>)
    - delete pianos: click 'delete' on any pianos_detail.html (route: admin/pianos/<int: piano_id>) to deactive pianos
        - after done delete, redirect to pianos.html(route:admin/pianos)

## To learn:

* JavaScript
* Geolocation 
* Uploading images
* Create JSON file
* (Stretch: auto-crop files for different screens, on a server)


## Technology used

- Flask framework
- Flask-Admin
- flask-security
- Flask-Migrate: db migration
- Flask-Bcrypt: hash password
- Bootstrap 4 Alpha
- JavaScript: get geoLocation
- AJAX: send data to back end (or just use form) ???


## How to contribute

1. Clone the repository:

```bash
git clone git@github.com:pianopushplay/admin_ui.git
cd admin_ui
```
2. Create virtual environment (pip is REQUIRED at the end)
```bash
conda create -n yourenvname pip
source activate yourenvname
```
3. Update packages from requirements file using pip (for now there is few too many of them)
```bash
pip install -r requirements.txt
```

3. Create MySQL database `db_name` and export it to local environment:
```bash
export DATABASE_URL='connection-to-your-db'
e.g.:
export DATABASE_URL='mysql+pymysql://user:password@host:port/db_name'
```
4. Run `manage.py`
```bash
python manage.py db upgrade
```
5. Create a superuser manually via phpMyAdmin
6. Run server:
```bash
python manage.py runserver 
```

## Sprint 2:

1. App runs locally
2. Superuser is create manually
3. Superuser can log in
4. Superuser can CRUD volunteers
5. Superuser can CRUD pianos
6. Geo-location fields can be updated manually. Pulling the data auto-magically does not work yet.