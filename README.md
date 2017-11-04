# Admin UI for [Piano. Push. Play.](http://www.pianopushplay.com)

## App overview
- This admin UI tracks all pianos on piano.push.play, handles authentication and authrization of 
  all admins and volunteers. 

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
6. pianos API will be available at BASE_DIR/api/v1.0/pianos/

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
4. Run `manage.py` to create tables
```bash
python manage.py db upgrade
```
If you get an error similar to this: 

```bash
sqlalchemy.exc.InternalError: (pymysql.err.InternalError) (1130, "Host '127.0.0.1' is not allowed to connect to this MySQL server")
```

create database at 127.0.0.1 not the usual localhost.

5. Create a superuser manually via phpMyAdmin or mysql shell
   * create **superuser** and **volunteer** roles in `role` table
   * create a new **user** in `user` table
   * create a row in `roles_users` with the **user's id** and the **superuser id**
6. Run server:

```bash
python manage.py runserver 
```

### live demo : [pianoadmin](http://adrianacmy.pythonanywhere.com)