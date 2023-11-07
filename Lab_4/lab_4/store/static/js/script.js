document.getElementById('passengerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const lastName = document.getElementById('lastName').value;
    const firstName = document.getElementById('firstName').value;
    const patronymic = document.getElementById('patronymic').value;
    const flightNumber = document.getElementById('flightNumber').value;

    const passenger = {
        lastName: lastName,
        firstName: firstName,
        patronymic: patronymic,
        flightNumber: flightNumber
    };

    addPassenger(passenger);
    document.getElementById('passengerForm').reset();
});

const passengers = [];

function addPassenger(passenger) {
    passengers.push(passenger);
    checkSameLastNamePassengers();
}

function checkSameLastNamePassengers() {
    const lastNameCounts = {};

    for (const passenger of passengers) {
        const { lastName, flightNumber } = passenger;
        const key = `${lastName}-${flightNumber}`;

        if (!lastNameCounts[key]) {
            lastNameCounts[key] = [];
        }

        lastNameCounts[key].push(passenger);
    }

    const sameLastNamePassengers = Object.values(lastNameCounts)
        .filter(passengerGroup => passengerGroup.length > 1)
        .flat();

    displaySameLastNamePassengers(sameLastNamePassengers);
    displayAllPassengers(passengers);
}

function displaySameLastNamePassengers(passengers) {
    const sameLastNamePassengersList = document.getElementById('sameLastNamePassengers');
    sameLastNamePassengersList.innerHTML = '';

    if (passengers.length > 0) {
        for (const passenger of passengers) {
            const listItem = document.createElement('li');
            listItem.textContent = `${passenger.lastName} ${passenger.firstName} ${passenger.patronymic}`;
            sameLastNamePassengersList.appendChild(listItem);
        }
    } else {
        const listItem = document.createElement('li');
        listItem.textContent = 'На данном рейсе нет однофамильцев.';
        sameLastNamePassengersList.appendChild(listItem);
    }
}


function displayAllPassengers(passengers) {
    const sameLastNamePassengersList = document.getElementById('allPassengers');
    sameLastNamePassengersList.innerHTML = '';

    if (passengers.length > 0) {
        for (const passenger of passengers) {
            const listItem = document.createElement('li');
            listItem.textContent = `${passenger.lastName} ${passenger.firstName} ${passenger.patronymic}`;
            sameLastNamePassengersList.appendChild(listItem);
        }
    }
}