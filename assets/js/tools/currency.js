(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var list = document.getElementById('conv-list');
  var statusEl = document.getElementById('rate-status');
  var keys = ['amount', 'from', 'to', 'spread'];
  var rates = null;
  var TARGETS = ['PKR', 'INR', 'PHP', 'BDT', 'NGN', 'EGP', 'KES', 'LKR', 'NPR', 'IDR', 'VND', 'EUR', 'GBP', 'USD', 'AED', 'SAR', 'CAD', 'AUD', 'TRY', 'BRL', 'MXN', 'UAH', 'MYR', 'ZAR'];
  f.querySelector('[name="from"]').innerHTML = TH.currencyOptions('USD');
  f.querySelector('[name="to"]').innerHTML = TH.currencyOptions('PKR');
  TH.readParams(f);
  var main = document.getElementById('main-result');

  document.getElementById('swap').addEventListener('click', function () {
    var a = f.from.value; f.from.value = f.to.value; f.to.value = a; update();
  });

  function update() {
    var amt = Math.max(0, TH.num(f.amount.value));
    var from = f.from.value, to = f.to.value;
    var sp = Math.max(0, TH.num(f.spread.value)) / 100;
    if (!rates) { main.innerHTML = '<span class="hint">Loading rates…</span>'; return; }
    var v = TH.convert(rates, amt, from, to);
    var r1 = TH.convert(rates, 1, from, to);
    var html = '<div class="res-total"><span class="l">' + TH.esc(TH.money(amt, from)) + ' is</span><output class="v"></output>' +
      '<span class="sub2">1 ' + from + ' = ' + r1.toFixed(r1 >= 100 ? 2 : 4) + ' ' + to + (sp ? ' · after ' + TH.pct(sp * 100) + ' spread you get ≈ ' + TH.esc(TH.money(v * (1 - sp), to)) : '') + '</span></div>';
    main.innerHTML = html;
    var out = main.querySelector('output');
    out.textContent = TH.money(v, to);
    var rows = '';
    TARGETS.filter(function (c) { return c !== from; }).forEach(function (c) {
      var x = TH.convert(rates, amt, from, c);
      rows += '<li><span class="cur"><i>' + c + '</i><small>' + TH.CURRENCIES[c].name + '</small></span><span class="amt">' + TH.esc(TH.money(x * (1 - sp), c)) + '</span></li>';
    });
    list.innerHTML = rows;
    document.getElementById('list-title').textContent = TH.money(amt, from) + ' in other freelancer currencies' + (sp ? ' (after spread)' : '');
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); update(); });
})();
