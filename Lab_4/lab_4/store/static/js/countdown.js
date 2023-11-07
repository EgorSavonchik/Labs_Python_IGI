// Функция для установки и запуска таймера
function startCountdown() {
    // Получаем текущее время в миллисекундах
    const now = new Date().getTime();

    // Проверяем, есть ли в локальном хранилище сохраненные данные
    const savedTime = localStorage.getItem('countdownTime');

    let endTime;

    if (savedTime) {
        // Если данные есть, используем их
        endTime = parseInt(savedTime, 10);
    } else {
        // Если данных нет, устанавливаем новое время окончания через час
        endTime = now + 3600000; // 1 час в миллисекундах
        localStorage.setItem('countdownTime', endTime);
    }

    // Обновляем отображение таймера каждую секунду
    const timerInterval = setInterval(() => {
        // Получаем текущее время
        const currentTime = new Date().getTime();

        // Вычисляем оставшееся время
        const distance = endTime - currentTime;

        // Проверяем, завершился ли отсчет
        if (distance <= 0) {
            clearInterval(timerInterval);
            localStorage.removeItem('countdownTime');
            document.getElementById('countdown').innerHTML = 'Отсчет завершен';
        } else {
            // Рассчитываем оставшиеся часы, минуты и секунды
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Обновляем отображение таймера
            document.getElementById('countdown').innerHTML = `${hours}ч ${minutes}м ${seconds}с`;
        }
    }, 1000);
}

// Вызываем функцию для запуска таймера
startCountdown();