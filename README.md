# Kevin's Melon Experience (Take Home Challenge)

Make a reservation to attend a fancy melon tasting!

## Setup

Before you begin the setup and installation process below, you'll need to have
the following installed:

- Python 3.0 or above
- PostgreSQL 11


CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT:

   $ pip3 install virtualenv  
   $ virtualenv env  
   $ source env/bin/activate  


INSTALL DEPENDENCIES:

(env) $ pip3 install -r requirements.txt


CREATES DATABASE CALLED reservations_db WITH A FEW SAMPLE USER INFO:

(env) $ python3 seed.py


RUN FLASK SERVER:

(env) $ python3 server.py


Simple login (no password needed)
Select date and time
    -Reservation will be added to user account if available
    -If booking on same day as previous reservation, message will display - #tooMuchMelon
    -If reservation is already taken, message will display to choose another time
    -logout

Would like to add delete capability so user can delete a reservation
