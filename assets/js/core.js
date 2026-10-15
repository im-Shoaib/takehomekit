/* Takehome core: theme, nav, formatting, exchange rates, payout slip. No dependencies. */
(function () {
  'use strict';
  var root = document.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      if (val === null) localStorage.removeItem(key); else localStorage.setItem(key, val);
    } catch (e) { return null; }
    return null;
  }

  /* ---------- Theme ---------- */
  function currentTheme() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('.theme-toggle');
    if (t) {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      store('th-theme', next);
      t.setAttribute('aria-label', next === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
    var m = e.target.closest('.menu-btn');
    if (m) {
      var nav = document.getElementById('site-nav');
      var open = nav.classList.toggle('open');
      m.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      var nav = document.getElementById('site-nav');
      if (nav && nav.classList.contains('open')) {
        nav.classList.remove('open');
        var b = document.querySelector('.menu-btn');
        if (b) { b.setAttribute('aria-expanded', 'false'); b.focus(); }
      }
    }
  });

  /* ---------- Numbers ---------- */
  var CURRENCIES = {
    USD: { name: 'US Dollar', sym: '$' }, EUR: { name: 'Euro', sym: '€' }, GBP: { name: 'British Pound', sym: '£' },
    PKR: { name: 'Pakistani Rupee', sym: 'Rs' }, INR: { name: 'Indian Rupee', sym: '₹' }, PHP: { name: 'Philippine Peso', sym: '₱' },
    BDT: { name: 'Bangladeshi Taka', sym: '৳' }, NGN: { name: 'Nigerian Naira', sym: '₦' }, AED: { name: 'UAE Dirham', sym: 'AED' },
    SAR: { name: 'Saudi Riyal', sym: 'SAR' }, CAD: { name: 'Canadian Dollar', sym: 'C$' }, AUD: { name: 'Australian Dollar', sym: 'A$' },
    EGP: { name: 'Egyptian Pound', sym: 'E£' }, KES: { name: 'Kenyan Shilling', sym: 'KSh' }, LKR: { name: 'Sri Lankan Rupee', sym: 'Rs' },
    NPR: { name: 'Nepalese Rupee', sym: 'Rs' }, IDR: { name: 'Indonesian Rupiah', sym: 'Rp' }, VND: { name: 'Vietnamese Dong', sym: '₫' },
    BRL: { name: 'Brazilian Real', sym: 'R$' }, MXN: { name: 'Mexican Peso', sym: 'MX$' }, TRY: { name: 'Turkish Lira', sym: '₺' },
    MYR: { name: 'Malaysian Ringgit', sym: 'RM' }, ZAR: { name: 'South African Rand', sym: 'R' }, UAH: { name: 'Ukrainian Hryvnia', sym: '₴' }
  };
  // Approximate fallback rates (per 1 USD). Used only if the live feed can't be reached.
  var FALLBACK = {
    date: '2026-10-01',
    rates: { USD: 1, EUR: 0.86, GBP: 0.75, PKR: 277, INR: 88.5, PHP: 58, BDT: 122, NGN: 1480, AED: 3.6725, SAR: 3.75, CAD: 1.38,
      AUD: 1.52, EGP: 48, KES: 129, LKR: 302, NPR: 141.5, IDR: 16500, VND: 26300, BRL: 5.4, MXN: 18.4, TRY: 41.5, MYR: 4.2, ZAR: 17.5, UAH: 41.5 }
  };

  function num(v) {
    if (typeof v === 'number') return isFinite(v) ? v : 0;
    if (v == null) return 0;
    var n = parseFloat(String(v).replace(/[^0-9.\-]/g, ''));
    return isFinite(n) ? n : 0;
  }
  function money(v, cur, opts) {
    cur = cur || 'USD';
    opts = opts || {};
    var big = Math.abs(v) >= 1000 && ['PKR', 'INR', 'NGN', 'IDR', 'VND', 'LKR', 'NPR', 'BDT', 'KES'].indexOf(cur) > -1;
    var digits = opts.digits != null ? opts.digits : (big ? 0 : 2);
    try {
      return new Intl.NumberFormat(cur === 'PKR' || cur === 'INR' ? 'en-IN' : 'en-US', {
        style: 'currency', currency: cur, minimumFractionDigits: digits, maximumFractionDigits: digits, currencyDisplay: 'narrowSymbol'
      }).format(v || 0);
    } catch (e) {
      return (CURRENCIES[cur] ? CURRENCIES[cur].sym + ' ' : '') + (v || 0).toFixed(digits);
    }
  }
  function pct(v, d) { return (v || 0).toFixed(d == null ? 1 : d).replace(/\.0$/, '') + '%'; }
  function round2(v) { return Math.round((v + Number.EPSILON) * 100) / 100; }

  /* ---------- Exchange rates (free, CORS-enabled, no key) ---------- */
  var RATES_KEY = 'th-rates-v1';
  var ratesPromise = null;
  function getRates() {
    if (ratesPromise) return ratesPromise;
    ratesPromise = new Promise(function (resolve) {
      var cached = null;
      try { cached = JSON.parse(store(RATES_KEY) || 'null'); } catch (e) { cached = null; }
      if (cached && cached.rates && Date.now() - cached.saved < 6 * 3600 * 1000) {
        resolve({ rates: cached.rates, date: cached.date, live: true });
        return;
      }
      var done = false;
      var timer = setTimeout(function () { finish(null); }, 6000);
      function finish(data) {
        if (done) return; done = true; clearTimeout(timer);
        if (data) resolve(data);
        else if (cached && cached.rates) resolve({ rates: cached.rates, date: cached.date, live: false });
        else resolve({ rates: FALLBACK.rates, date: FALLBACK.date, live: false });
      }
      if (!window.fetch) { finish(null); return; }
      fetch('https://open.er-api.com/v6/latest/USD', { cache: 'no-store' })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (j) {
          if (j && j.result === 'success' && j.rates && j.rates.PKR) {
            var d = new Date((j.time_last_update_unix || Date.now() / 1000) * 1000).toISOString().slice(0, 10);
            store(RATES_KEY, JSON.stringify({ rates: j.rates, date: d, saved: Date.now() }));
            finish({ rates: j.rates, date: d, live: true });
          } else finish(null);
        })
        .catch(function () { finish(null); });
    });
    return ratesPromise;
  }
  function convert(rates, amount, from, to) {
    if (!rates[from] || !rates[to]) return 0;
    return amount / rates[from] * rates[to];
  }
  function rateStatus(el, info) {
    if (!el) return;
    el.classList.toggle('live', !!info.live);
    el.innerHTML = '<span class="dot"></span>' + (info.live
      ? 'Live mid-market rates, updated ' + info.date
      : 'Offline estimate (' + info.date + '). Enter your own rate for exact figures.');
  }

  /* ---------- Payout slip ---------- */
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }

  function countUp(el, to, fmt) {
    var from = parseFloat(el.getAttribute('data-val') || '0');
    el.setAttribute('data-val', String(to));
    if (reduceMotion || from === to || !isFinite(from)) { el.textContent = fmt(to); return; }
    var start = null, dur = 420;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(from + (to - from) * e);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /*
   cfg = { title, meta, lines:[{label, value, type:'plus'|'minus'|'info'|'sub', text}], currency,
           total:{label, value, currency, sub}, bar:{keep, lose}, note, actions:true }
  */
  var uid = 0;
  function renderSlip(el, cfg) {
    if (!el) return;
    var cur = cfg.currency || 'USD';
    var first = !el.getAttribute('data-ready');
    var html = '<div class="res-head"><span class="res-title">' + esc(cfg.title || 'Result') + '</span>' +
      (cfg.meta ? '<span class="pill gold">' + esc(cfg.meta) + '</span>' : '') + '</div>';
    var k = null;
    if (cfg.total || cfg.bar) {
      html += '<div class="res-main">';
      if (cfg.total) {
        html += '<div class="res-total"><span class="l">' + esc(cfg.total.label) + '</span><output class="v" aria-live="polite"></output>' +
          (cfg.total.sub ? '<span class="sub2">' + esc(cfg.total.sub) + '</span>' : '') + '</div>';
      }
      if (cfg.bar) {
        var tot = Math.max(cfg.bar.keep + cfg.bar.lose, 0.0001);
        k = Math.max(0, Math.min(100, cfg.bar.keep / tot * 100));
        var id = 'kg' + (++uid);
        html += '<div class="donut" role="img" aria-label="' + esc((cfg.bar.label || 'You keep') + ' ' + pct(k)) + '"><svg viewBox="0 0 120 120" aria-hidden="true">' +
          '<defs><linearGradient id="' + id + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5ee6ab"/><stop offset="1" stop-color="#a08bff"/></linearGradient></defs>' +
          '<circle class="trk" cx="60" cy="60" r="48"/><circle class="arc" cx="60" cy="60" r="48" stroke="url(#' + id + ')" stroke-dasharray="301.59" stroke-dashoffset="301.59"/></svg>' +
          '<div class="ctr"><b>' + pct(k, (k > 99 && k < 100) || (k > 0 && k < 1) ? 2 : 0) + '</b><span>' + esc(cfg.bar.label || 'you keep') + '</span></div></div>';
      }
      html += '</div>';
    }
    if (cfg.lines && cfg.lines.length) {
      html += '<ul class="res-lines">';
      cfg.lines.forEach(function (ln) {
        var val = ln.text != null ? ln.text : (ln.type === 'minus' ? '−' : '') + money(Math.abs(ln.value), ln.currency || cur);
        html += '<li class="res-line ' + (ln.type || 'plus') + '"><span class="l">' + esc(ln.label) + '</span><span class="v">' + esc(val) + '</span></li>';
      });
      html += '</ul>';
    }
    if (cfg.note) html += '<p class="res-note">' + cfg.note + '</p>';
    if (cfg.actions !== false) {
      html += '<div class="res-actions"><button type="button" class="btn btn-ghost btn-small" data-copy-slip>' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>Copy breakdown</button>' +
        '<button type="button" class="btn btn-ghost btn-small" data-share-link>' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>Share result</button></div>';
    }
    var oldOut = el.querySelector('.res-total .v');
    var prev = oldOut ? oldOut.getAttribute('data-val') : null;
    var prevK = el._k != null ? el._k : 0;
    el.innerHTML = html;
    el.setAttribute('data-ready', '1');
    if (cfg.total) {
      var out = el.querySelector('.res-total .v');
      if (prev != null) out.setAttribute('data-val', prev);
      var tc = cfg.total.currency || cur;
      countUp(out, cfg.total.value, function (v) { return money(v, tc, cfg.total.digits != null ? { digits: cfg.total.digits } : null); });
    }
    if (k != null) {
      var arc = el.querySelector('.arc');
      var C = 301.59;
      arc.style.transition = 'none';
      arc.setAttribute('stroke-dashoffset', String(C * (1 - prevK / 100)));
      arc.getBoundingClientRect();
      arc.style.transition = '';
      requestAnimationFrame(function () { arc.setAttribute('stroke-dashoffset', String(C * (1 - k / 100))); });
      el._k = k;
    }
    if (first && !reduceMotion) {
      el.classList.add('reveal-in');
      setTimeout(function () { el.classList.remove('reveal-in'); }, 800);
    }
    el._plain = (cfg.title || '') + '\n' + (cfg.lines || []).map(function (ln) {
      return ln.label + ': ' + (ln.text != null ? ln.text : (ln.type === 'minus' ? '-' : '') + money(Math.abs(ln.value), ln.currency || cur));
    }).join('\n') + (cfg.total ? '\n' + cfg.total.label + ': ' + money(cfg.total.value, cfg.total.currency || cur) : '') + '\n— ' + location.href;
  }

  /* ---------- Clipboard + toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'toast'; toastEl.setAttribute('role', 'status'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove('show'); }, 2200);
  }
  function copy(text, msg) {
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); toast(msg || 'Copied'); } catch (e) { toast('Copy failed — select and copy manually'); }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { toast(msg || 'Copied'); }, fallback);
    } else fallback();
  }
  document.addEventListener('click', function (e) {
    var c = e.target.closest('[data-copy-slip]');
    if (c) { var s = c.closest('.slip'); if (s && s._plain) copy(s._plain, 'Breakdown copied'); }
    var l = e.target.closest('[data-share-link]');
    if (l) copy(location.href, 'Link copied — it opens with these exact numbers');
  });

  /* ---------- URL state (shareable results) ---------- */
  function readParams(form) {
    var p = new URLSearchParams(location.search);
    p.forEach(function (v, k) {
      var el = form.querySelector('[name="' + CSS.escape(k) + '"]');
      if (!el) return;
      if (el.type === 'checkbox') el.checked = v === '1';
      else el.value = v;
    });
    return p;
  }
  var urlTimer;
  function writeParams(form, keys) {
    clearTimeout(urlTimer);
    urlTimer = setTimeout(function () {
      var p = new URLSearchParams();
      keys.forEach(function (k) {
        var el = form.querySelector('[name="' + k + '"]');
        if (!el) return;
        var v = el.type === 'checkbox' ? (el.checked ? '1' : '0') : el.value;
        if (v !== '' && v != null) p.set(k, v);
      });
      try { history.replaceState(null, '', location.pathname + '?' + p.toString()); } catch (e) { /* file:// */ }
    }, 400);
  }

  /* ---------- Segmented controls ---------- */
  function seg(container, onChange) {
    if (!container) return;
    var input = container.querySelector('input[type="hidden"]');
    function set(val, silent) {
      container.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.v === val ? 'true' : 'false'); });
      if (input) input.value = val;
      if (!silent && onChange) onChange(val);
    }
    container.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (b) set(b.dataset.v);
    });
    set(input ? input.value : container.querySelector('button').dataset.v, true);
    return { set: set };
  }

  function currencyOptions(selected, list) {
    list = list || Object.keys(CURRENCIES);
    return list.map(function (c) {
      return '<option value="' + c + '"' + (c === selected ? ' selected' : '') + '>' + c + ' — ' + CURRENCIES[c].name + '</option>';
    }).join('');
  }


  /* ---------- Site UI: mega menu, reveal, TOC, card glow, search ---------- */
  var megaBtns = document.querySelectorAll('[data-mega]');
  var mega = document.getElementById('mega');
  function setMega(open) {
    if (!mega) return;
    mega.classList.toggle('open', open);
    megaBtns.forEach(function (b) { b.setAttribute('aria-expanded', open ? 'true' : 'false'); });
    document.documentElement.style.overflow = open && window.innerWidth <= 960 ? 'hidden' : '';
  }
  megaBtns.forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); setMega(!mega.classList.contains('open')); }); });
  document.addEventListener('click', function (e) { if (mega && mega.classList.contains('open') && !e.target.closest('#mega')) setMega(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && mega && mega.classList.contains('open')) { setMega(false); if (megaBtns[0]) megaBtns[0].focus(); } });
  window.addEventListener('resize', function () { if (mega && mega.classList.contains('open') && window.innerWidth > 960) document.documentElement.style.overflow = ''; });

  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revealEls.forEach(function (r) { io.observe(r); });
  } else revealEls.forEach(function (r) { r.classList.add('in'); });

  var toc = document.getElementById('toc');
  if (toc) {
    var hs = document.querySelectorAll('.prose h2');
    var items = '';
    hs.forEach(function (h, i) {
      if (!h.id) h.id = 's-' + (i + 1) + '-' + h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
      items += '<li><a href="#' + h.id + '">' + esc(h.textContent) + '</a></li>';
    });
    toc.innerHTML = items;
    if (!hs.length) toc.closest('.aside-box').hidden = true;
    if ('IntersectionObserver' in window) {
      var links = toc.querySelectorAll('a');
      var tio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + en.target.id); });
        });
      }, { rootMargin: '-20% 0px -70% 0px' });
      hs.forEach(function (h) { tio.observe(h); });
    }
  }

  document.addEventListener('pointermove', function (e) {
    var c = e.target.closest && e.target.closest('.tcard');
    if (!c) return;
    var r = c.getBoundingClientRect();
    c.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
    c.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
  });

  var search = document.getElementById('tool-search');
  if (search) {
    var cards = document.querySelectorAll('[data-search]');
    var none = document.getElementById('no-results');
    function filter() {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      cards.forEach(function (c) { var hit = !q || c.getAttribute('data-search').indexOf(q) > -1; c.hidden = !hit; if (hit) shown++; });
      document.querySelectorAll('.cat').forEach(function (sec) { sec.hidden = !sec.querySelector('[data-search]:not([hidden])'); });
      if (none) none.hidden = shown > 0;
    }
    search.addEventListener('input', filter);
    search.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { var f = document.querySelector('[data-search]:not([hidden]) a'); if (f) location.href = f.getAttribute('href'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); search.focus(); }
    });
  }

  window.TH = {
    num: num, money: money, pct: pct, round2: round2, esc: esc,
    getRates: getRates, convert: convert, rateStatus: rateStatus, CURRENCIES: CURRENCIES, currencyOptions: currencyOptions,
    renderSlip: renderSlip, toast: toast, copy: copy, readParams: readParams, writeParams: writeParams, seg: seg, store: store,
    reduceMotion: reduceMotion
  };
})();
