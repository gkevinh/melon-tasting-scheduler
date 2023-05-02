from model import db, User, Reservation


def create_user(username):
    """Create a new user and return the user object"""

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_username(username):
    """Return a user object by username"""

    return User.query.filter_by(username=username).first()



def get_reservation_by_user_id(user_id):
    """Return a reservation by user ID."""
    return Reservation.query.filter_by(user_id=user_id).first()



def get_reservations_by_user(user):
    """Return a list of all reservations for a given user"""

    return Reservation.query.filter_by(user=user).all()



def user_reservation_same_day(user, reservation_date):
    """Check if user has a reservation scheduled for a specific date."""
    
    reservation = Reservation.query.filter_by(user=user, reservation_date=reservation_date).first()
    return reservation is not None



def create_reservation(username, res_date, res_time):
    """Create a new reservation and return the reservation object"""

    # check if the desired time slot is available
    existing_reservation = Reservation.query.filter_by(reservation_date=res_date, reservation_time=res_time).first()
    if existing_reservation:
        return None

    reservation = Reservation(user=username, reservation_date=res_date, reservation_time=res_time)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def is_reservation_taken(datetime_obj):
    """Check if a reservation already exists for the given datetime object"""
    
    reservation = Reservation.query.filter_by(reservation_date=datetime_obj.date(), reservation_time=datetime_obj.time()).first()
    if reservation:
        return True
    else:
        return False


def check_if_reservation_exists(reservation_date, reservation_time):
    """Return reservation given date and time."""
    return Reservation.query.filter_by(reservation_date=reservation_date, reservation_time=reservation_time).first()


def save_reservation(user):
    """Save and return reservation."""
    reservation = Reservation(user=user)
    return reservation


def save_reservation(user, reservation_date, reservation_time, is_not_available):
    """Save and return reservation."""
    reservation = Reservation(user=user,
                               reservation_date=reservation_date,
                               reservation_time=reservation_time,
                               is_not_available=is_not_available)
    db.session.add(reservation)
    db.session.commit()
    return reservation


def get_reservation_by_date_and_time(reservation_date, reservation_time):
    """Return a reservation object for a given date and time"""
    return Reservation.query.filter_by(reservation_date=reservation_date,
                                    reservation_time=reservation_time).first()