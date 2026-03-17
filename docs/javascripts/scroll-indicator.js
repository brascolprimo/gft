// Глобальный индикатор прокрутки
document.addEventListener('DOMContentLoaded', function() {
    // Создаём элементы индикатора, если их ещё нет
    if (!document.querySelector('.global-scroll-indicator')) {
        const indicator = document.createElement('div');
        indicator.className = 'global-scroll-indicator';
        
        const fill = document.createElement('div');
        fill.className = 'global-scroll-indicator-fill';
        
        indicator.appendChild(fill);
        document.body.appendChild(indicator);
    }

    const fillElement = document.querySelector('.global-scroll-indicator-fill');
    
    function updateScrollIndicator() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight;
        const winHeight = window.innerHeight;
        const scrollPercent = (scrollTop / (docHeight - winHeight)) * 100 || 0;
        
        // Ограничиваем от 0 до 100
        const percent = Math.min(100, Math.max(0, scrollPercent));
        fillElement.style.height = percent + '%';
    }
    
    window.addEventListener('scroll', updateScrollIndicator);
    window.addEventListener('resize', updateScrollIndicator);
    updateScrollIndicator(); // вызываем сразу для начального состояния
});