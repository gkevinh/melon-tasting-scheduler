import os
import json
from datetime import datetime, time

import crud
import model
import server

os.system("dropdb reservations_db")
os.system("createdb reservations_db")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/users.json") as f:
    user_data = json.loads(f.read())

with open("data/reservations.json") as g:
    reservation_data = json.loads(g.read())

users_in_db = []
for user in user_data:
    username = user.get("username")
    if username:
        db_user = crud.create_user(username=username)
        users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

reservations_in_db = []
for res in reservation_data:
    username, res_date, res_time = (
        res["username"],
        datetime.strptime(res["reservation_date"], "%Y-%m-%d"),
        datetime.strptime(res["reservation_time"], "%I:%M:%S %p").time(),
    )

    db_user = crud.get_user_by_username(username)
    db_res = crud.create_reservation(db_user, res_date, res_time)
    reservations_in_db.append(db_res)

model.db.session.add_all(reservations_in_db)
model.db.session.commit()

print("Seed script completed!")
