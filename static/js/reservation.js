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
const dateInput = document.querySelector('#start');
const reservationDateInput = document.querySelector('#reservation_date');
const timeInput = document.querySelector('#time');
const reservationTimeInput = document.querySelector('#reservation_time');

dateInput.addEventListener('change', () => {
  const selectedDate = dateInput.value;
  reservationDateInput.value = selectedDate;
});


dateInput.addEventListener('change', () => {
  const selectedTime = timeInput.value;
  reservationTimeInput.value = selectedTime;
});


reservationForm.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const user_id = user.id;
  const reservation_date = document.querySelector("#reservation_date").innerHTML;
  const reservation_time = document.querySelector("#reservation_time").innerHTML;
  const is_not_available = document.querySelector("#is_not_available").innerHTML;
  const time = document.querySelector("#time").innerHTML;
  const start = document.querySelector("#start").innerHTML;
  const convertedTime = convertTo24Hour(reservation_time);
  submitReservation(user_id, reservation_date, convertedTime, is_not_available, time, start);
});


function submitReservation(user_id, reservation_date, reservation_time, is_not_available, time, start) {
  const input = {
    user_id: user_id,
    reservation_date: reservation_date,
    reservation_time: reservation_time,
    is_not_available: is_not_available,
    time: time,
    start: start
  }
  fetch('/add-reservation', {
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