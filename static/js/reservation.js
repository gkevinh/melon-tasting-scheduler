'use strict';

function convertTo24Hour(time) {
  const [hour, minute, period] = time.split(/:|\s/);
  let hourInt = parseInt(hour, 10);
  if (period === 'PM' && hourInt !== 12) {
    hourInt += 12;
  } else if (period === 'AM' && hourInt === 12) {
    hourInt = 0;
  }
  return `${hourInt.toString().padStart(2, '0')}:${minute}`;
}

const reservationForm = document.querySelector('.add-reservation');

reservationForm.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const user_id = user.id;
  const reservation_date = document.querySelector("#reservation_date").value;
  const reservation_time = document.querySelector("#reservation_time").value;
  const is_not_available = document.querySelector("#is_not_available").value;
  const selectedDate = document.querySelector("#start").value;
  const convertedTime = convertTo24Hour(reservation_time);
  submitReservation(user_id, reservation_date, convertedTime, is_not_available, selectedDate);
});

window.addEventListener('load', (evt) => {
  const today = new Date().toISOString().split('T')[0];
  const maxDate = new Date(new Date().setFullYear(new Date().getFullYear() + 1)).toISOString().split('T')[0];
  document.getElementById("reservation_date").setAttribute("min", today);
  document.getElementById("reservation_date").setAttribute("max", maxDate);
});

function submitReservation(user_id, reservation_date, reservation_time, is_not_available) {
  const input = {
    user_id: user_id,
    reservation_date: reservation_date,
    reservation_time: reservation_time,
    is_not_available: is_not_available
  }
  fetch('/add-favorite', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(input)
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      alert('Reservation added!');  
    } else {
      alert('Reservation already taken. Try again.');
    }
  })
  .catch(function(error) {
    console.error('Error adding:', error);
    alert('Error');
  });
}