// Один обработчик на весь документ (делегирование)
document.addEventListener('click', function(e) {
  const target = e.target.closest('.copy-address');
  if (!target) return; // клик не по адресу

  e.preventDefault();

  const textToCopy = target.getAttribute('data-clipboard');
  if (!textToCopy) return;

  navigator.clipboard.writeText(textToCopy)
    .then(() => {
      // Визуальная обратная связь
      target.classList.add('copied');
      setTimeout(() => target.classList.remove('copied'), 1500);
    })
    .catch(err => {
      console.error('Ошибка копирования:', err);
      // Можно добавить fallback для старых браузеров, но обычно не требуется
    });
});