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
  .counter-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 16px;
    margin: 20px 0 30px;
  }
  .counter-item {
    background: rgba(20, 30, 40, 0.5);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 24px;
    padding: 16px 12px;
    text-align: center;
    font-family: 'Fira Code', monospace;
  }
  .counter-label {
    color: #b388ff;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
  }
  .counter-value {
    color: #4a9eff;
    font-size: 0.95rem;
    text-shadow: 0 0 5px #4a9eff;
    word-break: break-word;
  }
  .quote-block details {
    background: rgba(0,0,0,0.2);
    border-radius: 16px;
    padding: 8px 16px;
    margin-bottom: 16px;
  }
  .quote-block summary {
    cursor: pointer;
    color: #4a9eff;
    font-weight: 500;
    outline: none;
  }
  .quote-block .quote-text {
    margin-top: 12px;
    padding-left: 8px;
    border-left: 2px solid #4a9eff;
    font-size: 0.95rem;
    line-height: 1.5;
    color: #B0C0D0;
    font-style: italic;
  }
  .quote-block .quote-source {
    margin-top: 8px;
    font-size: 0.75rem;
    color: #b388ff;
    font-family: 'Fira Code', monospace;
  }
  .quote-block .quote-source a {
    color: #4a9eff;
    text-decoration: none;
  }
  .quote-block .quote-source a:hover {
    text-decoration: underline;
  }
</style>

# <span style="background: linear-gradient(135deg, #4a9eff, #8a2be2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 15px #4a9eff);">GFT Guru</span>

<div class="info-panel" style="padding: 16px 20px; margin: 0 0 20px 0; border-left: 4px solid #4a9eff;">
  <p style="margin: 0; font-size: 1rem; display: flex; align-items: center; gap: 8px;">
    <span style="font-size: 1.5rem;">⛔</span> 
    Справочная информация по подаркам, экосистеме TON и другому. Финансовых рекомендаций тут бесплатно не дождетесь.
  </p>
</div>

<!-- Блок автора (красивый, круглый, сразу под инфо) -->
<div class="info-panel" style="padding: 20px 24px; margin: 0 0 30px 0; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; background: rgba(20, 30, 40, 0.4); backdrop-filter: blur(8px); border-color: rgba(74,158,255,0.3); border-radius: 40px;">
  <div style="flex: 1; font-size: 1.1rem; color: #B0C0D0;">
    Автор <span class="glitch" style="font-weight: 600;">ZG</span>
  </div>
  <div>
    <a href="#" class="glass-button" style="padding: 10px 24px; display: inline-flex; align-items: center; gap: 8px; border-radius: 40px;">Telegram</a>
  </div>
</div>

<!-- Блок доната – новый заголовок -->
<h3 style="margin-bottom: 16px; font-weight: 400; letter-spacing: 1px;">Адреса потом сделаю, пока можете потыкать на заглушки и перейти в тг</h3>

<div style="display: flex; flex-direction: column; gap: 16px; margin: 20px 0;">
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #4a9eff20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #4a9eff; font-weight: 600; min-width: 70px;">TON</span>
    <code class="copy-address" data-clipboard="UQDYx...7Xe3" style="color: #4a9eff;">UQDYx...7Xe3</code>
  </div>
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #f7931a20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #f7931a; font-weight: 600; min-width: 70px;">BTC</span>
    <code class="copy-address" data-clipboard="bc1q...8z4k" style="color: #f7931a;">bc1q...8z4k</code>
  </div>
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #26a17b20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #26a17b; font-weight: 600; min-width: 70px;">TRC20</span>
    <code class="copy-address" data-clipboard="TR7...9fL" style="color: #26a17b;">TR7...9fL</code>
  </div>
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #f3ba2f20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #f3ba2f; font-weight: 600; min-width: 70px;">BEP20</span>
    <code class="copy-address" data-clipboard="0xBNB...3aF" style="color: #f3ba2f;">0xBNB...3aF</code>
  </div>
  <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
    <span style="background: #9945ff20; padding: 4px 12px; border-radius: 30px; font-size: 0.9rem; color: #9945ff; font-weight: 600; min-width: 70px;">SOL</span>
    <code class="copy-address" data-clipboard="SOL...9xQ" style="color: #9945ff;">SOL...9xQ</code>
  </div>
</div>

<!-- ЦИТАТЫ (проще некуда) -->
<div style="margin: 30px 0 20px;">
  <details style="background: #1a232f; border-radius: 24px; padding: 16px;">
    <summary style="color: #4a9eff; font-size: 0.95rem; font-weight: 500; cursor: pointer; border-radius: 24px;">
      2025 · Project Syndicate: Stablecoin Time Bomb
    </summary>
    <div style="margin-top: 16px; padding-left: 18px; border-left: 2px solid rgba(74,158,255,0.2);">
      <p style="margin: 0 0 8px 0; font-size: 0.95rem; line-height: 1.5; color: #B0C0D0; font-style: italic;">
        «Не покупайтесь на шумиху. Криптовалюта макроэкономически незначительна, но опасна. Стейблконы — это бомба замедленного действия под мировую финансовую систему. Их эмитенты имеют стимул выпускать больше токенов, чем у них есть долларовых резервов. Это рецепт следующего 2008 года. Банковская паника может вызвать "набег" на стейблконы, что приведёт к цепной реакции банкротств. Существует "петля зловещей судьбы" (doom loop), связывающая стейблконы с рынками акций и облигаций. Закон GENIUS Act, принятый в июне 2025, приведёт к миграции до 6,6 триллионов долларов банковских депозитов в стейблконы. Это закладывает гигантскую бомбу замедленного действия под фундамент нашей экономической системы. В текущем олигархическом, эксплуататорском, иррациональном и бесчеловечном мировом порядке рост крипто-приложений сделает наше общество ещё более олигархическим, более эксплуататорским, более иррациональным и более бесчеловечным.»
      </p>
      <div style="font-size: 0.7rem; color: #b388ff; font-family: 'Fira Code', monospace;">
        Yanis Varoufakis. A Trust Fund for Everyone to Defuse the Stablecoin Time Bomb // Project Syndicate. — 2025, 12 July.
      </div>
    </div>
  </details>
</div>

<!-- Сетка с историческими датами (только Биткоин и Эфириум) -->
<div class="counter-grid">
  <div class="counter-item">
    <div class="counter-label">2009.01.03</div>
    <div class="counter-value" id="bitcoin-genesis">—</div>
  </div>
  <div class="counter-item">
    <div class="counter-label">2015.07.30</div>
    <div class="counter-value" id="ethereum-genesis">—</div>
  </div>
</div>

<script>
  (function() {
    const dates = [
      { id: 'bitcoin-genesis', date: new Date('2009-01-03T18:15:05Z') },
      { id: 'ethereum-genesis', date: new Date('2015-07-30T00:00:00Z') }
    ];
    
    function formatDuration(ms) {
      if (ms < 0) return '—';
      let totalSeconds = Math.floor(ms / 1000);
      let days = Math.floor(totalSeconds / 86400);
      let hours = Math.floor((totalSeconds % 86400) / 3600);
      let minutes = Math.floor((totalSeconds % 3600) / 60);
      let seconds = totalSeconds % 60;
      let deciseconds = Math.floor((ms % 1000) / 100);
      let years = 0;
      while (days >= 365) {
        years++;
        days -= 365;
      }
      return `${years}y ${days}d ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${deciseconds}`;
    }

    function updateAllCounters() {
      const now = new Date();
      dates.forEach(item => {
        const diff = now - item.date;
        const el = document.getElementById(item.id);
        if (el) el.textContent = formatDuration(diff);
      });
    }

    updateAllCounters();
    setInterval(updateAllCounters, 100);
  })();
</script>