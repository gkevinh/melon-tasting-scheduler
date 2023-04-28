'use strict';

const addReservation = document.querySelector('.add-reservation');

addReservation.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const reservation_date = document.querySelector("#reservation_date").value;
  const reservation_time = document.querySelector("#reservation_time").value;
  const is_not_available = document.querySelector("#is_not_available").value;
  addReservation(reservation_date, reservation_time, is_not_available);
});

function submitReservation(reservation_date, reservation_time, is_not_available) {
  const input = {
    reservation_date: reservation_date,
    reservation_time: reservation_time,
    is_not_available: is_not_available
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
      alert(data.message);
    }
  });
}
