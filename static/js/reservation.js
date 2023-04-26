// 'use strict';

// const reservationForm = document.querySelector('#reservation-form');

// reservationForm.addEventListener('submit', (evt) => {
//   evt.preventDefault();
//   const reservation_date = document.querySelector("#reservation_date").value;
//   const reservation_time = document.querySelector("#reservation_time").value;
//   const is_not_available = document.querySelector("#is_not_available").value;
//   submitReservation(reservation_date, reservation_time, is_not_available);
// });

// function submitReservation(reservation_date, reservation_time, is_not_available) {
//   const input = {
//     reservation_date: reservation_date,
//     reservation_time: reservation_time,
//     is_not_available: is_not_available
//   }
//   fetch('/add-reservation', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(input)
//   })
//   .then((response) => response.json())
//   .then((data) => {
//     if (data.success) {
//       alert('Reservation added!');  
//     } else {
//       alert(data.message);
//     }
//   });
// }


'use strict';

const reservationForm = document.querySelector('#reservation-form');
const reservationDate = document.querySelector('#reservation_date');
const reservationTime = document.querySelector('#reservation_time');

reservationForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const date = document.querySelector('#start').value;
  const time = document.querySelector('#time').value;
  reservationDate.value = date;
  reservationTime.value = time;
  fetch('/add-reservation', {
    method: 'POST',
    body: new FormData(reservationForm)
  })
  .then(response => response.json())
  .then(data => {
    const addReservationContainer = document.querySelector('.add-reservation');
    if (data.message) {
      addReservationContainer.innerHTML = `<p>${data.message}</p>`;
    } else {
      addReservationContainer.innerHTML = `<p>Reservation added successfully!</p>`;
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
