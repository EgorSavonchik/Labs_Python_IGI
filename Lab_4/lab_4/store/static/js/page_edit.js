document.getElementById("styleForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Получаем значения из формы
    var fontSize = document.getElementById("fontSize").value + "px";
    var textColor = document.getElementById("textColor").value;
    var bgColor = document.getElementById("bgColor").value;
  
    // Применяем стили к нужным элементам
    document.body.style.fontSize = fontSize;
    document.body.style.color = textColor;
    document.body.style.backgroundColor = bgColor;
    document.querySelector('main').style.backgroundImage = 'none';
  });
  