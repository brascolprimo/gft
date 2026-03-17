<!-- ---
title: Главная
--- -->

<style>
  /* Техно-панк примочки */
  .glitch {
    position: relative;
    display: inline-block;
    color: #4a9eff;
    text-shadow: 0.05em 0 0 #ff00ff, -0.05em -0.025em 0 #00ffff;
    animation: glitch-shake 0.3s infinite alternate;
  }
  @keyframes glitch-shake {
    0% { transform: translate(0); }
    20% { transform: translate(-1px, 1px); }
    40% { transform: translate(1px, -1px); }
    60% { transform: translate(-1px, 0); }
    80% { transform: translate(1px, 0); }
    100% { transform: translate(0); }
  }
  .status-bar {
    font-family: monospace;
    border-top: 1px dashed #4a9eff;
    border-bottom: 1px dashed #4a9eff;
    padding: 8px 0;
    margin: 24px 0;
    color: #4a9eff;
    text-transform: uppercase;
    letter-spacing: 2px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
  }
  .glass-button {
    transition: all 0.2s;
  }
  .glass-button:hover {
    box-shadow: 0 0 0 1px #3B82F6, 0 0 20px rgba(59,130,246,0.5);
    transform: translateY(-2px);
  }
  .copy-address {
    display: inline-block;
    background: rgba(30, 36, 51, 0.5);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 40px;
    padding: 6px 18px;
    font-size: 0.95rem;
    font-family: 'Fira Code', monospace;
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
    text-decoration: none;
  }
  .copy-address:hover {
    background: rgba(59, 130, 246, 0.4);
    border-color: #4a9eff;
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.6);
  }
  #genesis-counter {
    font-family: 'Fira Code', monospace;
    color: #b388ff;
    text-shadow: 0 0 5px #b388ff;
    background: rgba(0,0,0,0.2);
    padding: 2px 8px;
    border-radius: 20px;
  }
</style>

# <span style="background: linear-gradient(135deg, #4a9eff, #8a2be2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 15px #4a9eff);">GFT Guru</span>

<div class="info-panel" style="padding: 16px 20px; margin: 0 0 20px 0; border-left: 4px solid #4a9eff;">
  <p style="margin: 0; font-size: 1rem; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.5rem;">⚠️</span> 
    Финансовых рекомендаций тут бесплатно не дождетесь.
  </p>
</div>

<!-- Строка состояния с посекундным отсчетом от genesis блока -->
<div class="status-bar">
  <span>> SIGMA CREATOR // ONLINE</span>
  <span id="genesis-counter">⏳ загрузка...</span>
  <span>CLASSIFIED //</span>
</div>

<script>
  (function() {
    // Дата первого блока Bitcoin (2009-01-03 18:15:05 UTC) — точное время блока genesis
    const genesis = new Date('2009-01-03T18:15:05Z'); 
    
    function formatDuration(ms) {
      let totalSeconds = Math.floor(ms / 1000);
      let days = Math.floor(totalSeconds / 86400);
      let hours = Math.floor((totalSeconds % 86400) / 3600);
      let minutes = Math.floor((totalSeconds % 3600) / 60);
      let seconds = totalSeconds % 60;
      let deciseconds = Math.floor((ms % 1000) / 100); // десятые доли секунды

      let years = 0;
      while (days >= 365) {
        years++;
        days -= 365;
      }
      
      return `${years}y ${days}d ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${deciseconds}`;
    }

    function updateCounter() {
      const now = new Date();
      const diff = now - genesis;
      const el = document.getElementById('genesis-counter');
      if (el) {
        el.textContent = formatDuration(diff);
      }
    }

    updateCounter();
    setInterval(updateCounter, 100); // обновление каждые 100 мс (децисекунды)
  })();
</script>

<!-- Блок доната – цветные метки и адреса с обводкой -->
<h3 style="margin-bottom: 16px; font-weight: 400; letter-spacing: 1px;">💎 <span style="color: #4a9eff;">десятину</span> можете закинуть сюда</h3>

<div style="display: flex; flex-direction: column; gap: 16px; margin: 20px 0;">
  <!-- TON -->
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #4a9eff20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #4a9eff; font-weight: 600; min-width: 70px;">TON</span>
    <code class="copy-address" data-clipboard="UQDYx...7Xe3" style="color: #4a9eff;">UQDYx...7Xe3</code>
  </div>
  <!-- BTC -->
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #f7931a20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #f7931a; font-weight: 600; min-width: 70px;">BTC</span>
    <code class="copy-address" data-clipboard="bc1q...8z4k" style="color: #f7931a;">bc1q...8z4k</code>
  </div>
  <!-- TRC20 -->
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #26a17b20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #26a17b; font-weight: 600; min-width: 70px;">TRC20</span>
    <code class="copy-address" data-clipboard="TR7...9fL" style="color: #26a17b;">TR7...9fL</code>
  </div>
  <!-- BEP20 -->
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #f3ba2f20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #f3ba2f; font-weight: 600; min-width: 70px;">BEP20</span>
    <code class="copy-address" data-clipboard="0xBNB...3aF" style="color: #f3ba2f;">0xBNB...3aF</code>
  </div>
  <!-- SOL -->
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #9945ff20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #9945ff; font-weight: 600; min-width: 70px;">SOL</span>
    <code class="copy-address" data-clipboard="SOL...9xQ" style="color: #9945ff;">SOL...9xQ</code>
  </div>
</div>

<!-- Блок автора – только текст и ссылка -->
<div class="info-panel" style="padding: 16px 20px; margin: 30px 0 0; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; background: rgba(0,0,0,0.3); border-color: #4a9eff;">
  <div style="flex: 1; font-size: 1rem; color: #B0C0D0;">
    Автор проекта <span class="glitch">реальный сигма</span>.
  </div>
  <div>
    <a href="#" class="glass-button" style="padding: 8px 20px; display: inline-flex; align-items: center; gap: 8px;">✈️ Telegram</a>
  </div>
</div>