from app import db
from models import User, Role

# insert data
db.session.add(User(first_name="admin", last_name="admin",
                    email="admin@gmail.com", password="pianoadmin",
                    roles=[Role(name="superuser", description="can update location")])
               )
db.session.add(User(first_name="volu", last_name="vol",
                    email="vol@gmail.com", password="pianovol",
                    roles=[Role(name="volunteer", description="can update location")])
               )


# commit the changes
db.session.commit()
