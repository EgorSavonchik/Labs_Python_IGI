const links = document.querySelectorAll('.custom-button');

links.forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault();

    const explosion = document.createElement('div');
    explosion.classList.add('explosion');
    this.appendChild(explosion);

    setTimeout(() => {
      window.location.href = link.href;
    }, 500);
  });
});