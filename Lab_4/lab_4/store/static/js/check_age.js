document.addEventListener('DOMContentLoaded', function() {
  const overlay = document.getElementById('overlay');
  const ageVerificationPopup = document.getElementById('age-verification-popup');

  const submitAge = document.getElementById('age-confirm');
  const birthdateInput = document.getElementById('birth-date');

  // Функция для проверки возраста
  function checkAge() {
      const birthdate = new Date(birthdateInput.value);
      const now = new Date();
      const age = now.getFullYear() - birthdate.getFullYear();
      if (now.getMonth() < birthdate.getMonth() || (now.getMonth() === birthdate.getMonth() && now.getDate() < birthdate.getDate())) {
          age--;
      }

      return age >= 18;
  }

  // При каждом входе на страницу
  overlay.classList.remove('hidden');
  ageVerificationPopup.classList.remove('hidden');

  // При нажатии на кнопку "Подтвердить"
  submitAge.addEventListener('click', function() {
      if (checkAge()) {
          overlay.style.display = 'none';
          ageVerificationPopup.style.display = 'none';

        const birthdate = new Date(birthdateInput.value);
        const inputDate = new Date(birthdate);
        const today = new Date(); // Get the current date
        const ageDate = new Date(today - inputDate);
        // 1970 is subtracted to calculate the number of years since the Unix epoch (January 1, 1970) to the user's birth year
        const years = Math.abs(ageDate.getUTCFullYear() - 1970);
        const dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        alert(`You are ${years} years old. The day of the week of your birthdate is ${dayOfWeek[inputDate.getDay()]}`);

      } else {
          alert('Вы несовершеннолетний! Доступ запрещен!');
          window.location.href = 'http://127.0.0.1:8000/';
      }
  });
});


