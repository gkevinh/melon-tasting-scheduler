from flask import Flask, jsonify, render_template, request, redirect, session, flash
from model import connect_to_db, db, User, Reservation
import crud
import os
import requests
import json
from datetime import datetime, date


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "key"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('login.html')



@app.route("/make-view", methods=["GET", "POST"])
def enter_user():
    """Add a user or redirect to menu."""

    username = request.form.get("username")

    user = crud.get_user_by_username(username)

    if user:
        session['username'] = user.username
        flash(f"Welcome, {user.username}!")
        return render_template('menu.html')

    else:
        user = crud.create_user(username)
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username
        flash(f"Welcome, {user.username}!")
        return render_template('menu.html')



@app.route("/search", methods=['GET', 'POST'])
def search():

    username = session.get("username")
    user = crud.get_user_by_username(username)
    if not username:
        return render_template("/")
    
    flash(f"{user.username}'s account")
    today = date.today()
    return render_template('search.html', today=today)



@app.route('/add-reservation', methods=['POST'])
def add_reservation():
    """Add reservation to user's reservations table."""
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Please log in to add a reservation'})
    
    user = crud.get_user_by_username(session['username'])

    data = request.json
    reservation_date = data.get('reservation_date')
    reservation_time = data.get('reservation_time')

    existing_reservation = crud.user_reservation_same_day(user, reservation_date)
    if existing_reservation:
        return jsonify({'success': False, 'message': 'You already have a reservation for this date'})

    if crud.get_reservation_by_date_and_time(reservation_date, reservation_time):
        return jsonify({'success': False, 'message': 'Reservation taken. Try again.'})

    reservation = Reservation(user_id=user.id,
                               reservation_date=reservation_date,
                               reservation_time=reservation_time,
                               is_not_available=True)

    db.session.add(reservation)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Reservation added!'})



@app.route('/user-reservations')
def view_reservations():
    """View user's reservations."""
    
    username = session.get('username')
    if not username:
        flash('You must be logged in to view your profile.')
        return redirect('/')
    
    user = crud.get_user_by_username(username)
    reservations = user.reservations
    
    return render_template('view-user-reservations.html', user=user, reservations=reservations)



@app.route("/logout")
def logout():
    """User logout."""

    session.pop("username", None)

    return redirect("/")



if __name__ == "__main__":
    connect_to_db(app)
    print("http://localhost:5000/")
    app.run(host="0.0.0.0", debug=True)