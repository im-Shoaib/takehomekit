(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['amount', 'from', 'to', 'src', 'conv', 'rate', 'wht', 'flat'];
  var rates = null, liveRate = null;
  f.querySelector('[name="from"]').innerHTML = TH.currencyOptions('USD', ['USD', 'EUR', 'GBP', 'CAD', 'AUD', 'AED']);
  f.querySelector('[name="to"]').innerHTML = TH.currencyOptions('PKR', ['PKR', 'INR', 'BDT', 'PHP', 'NGN', 'EGP', 'KES', 'LKR', 'NPR', 'IDR', 'VND', 'TRY', 'BRL', 'MXN', 'UAH', 'MYR', 'ZAR']);
  var params = TH.readParams(f);
  var userRate = params.has('rate');

  function syncRate() {
    if (!rates) return;
    liveRate = TH.convert(rates, 1, f.from.value, f.to.value);
    if (!userRate) f.rate.value = liveRate >= 100 ? liveRate.toFixed(2) : liveRate.toFixed(4);
  }
  f.rate.addEventListener('input', function () { userRate = f.rate.value !== ''; });
  f.querySelector('[data-reset-rate]').addEventListener('click', function () { userRate = false; syncRate(); update(); });

  function update(e) {
    if (e && (e.target === f.from || e.target === f.to)) { userRate = false; syncRate(); }
    var from = f.from.value, to = f.to.value;
    var amt = Math.max(0, TH.num(f.amount.value));
    var srcP = TH.num(f.src.value) / 100;
    var recv = amt * srcP;
    var after = amt - recv;
    var flat = Math.max(0, TH.num(f.flat.value));
    var afterFlat = Math.max(0, after - flat);
    var rate = TH.num(f.rate.value);
    var conv = TH.num(f.conv.value) / 100;
    var effRate = rate * (1 - conv);
    var mid = afterFlat * rate;
    var gotLocal = afterFlat * effRate;
    var wht = gotLocal * TH.num(f.wht.value) / 100;
    var final = Math.max(0, gotLocal - wht);
    var ideal = amt * rate;
    var lines = [{ label: 'Payoneer balance', value: amt, currency: from }];
    if (recv) lines.push({ label: 'Receiving fee (' + TH.pct(srcP * 100) + ')', value: recv, type: 'minus', currency: from });
    if (flat) lines.push({ label: 'Flat withdrawal fee', value: flat, type: 'minus', currency: from });
    lines.push({ label: 'Mid-market value', value: mid, currency: to, type: 'sub' });
    lines.push({ label: 'Conversion spread (' + TH.pct(conv * 100) + ')', value: mid - gotLocal, type: 'minus', currency: to });
    if (wht) lines.push({ label: 'Bank withholding tax (' + TH.pct(TH.num(f.wht.value), 2) + ')', value: wht, type: 'minus', currency: to });
    lines.push({ label: 'Your rate', text: '1 ' + from + ' = ' + effRate.toFixed(effRate >= 100 ? 2 : 4) + ' ' + to, type: 'info' });
    TH.renderSlip(slip, {
      title: 'Withdrawal estimate', meta: from + ' → ' + to, currency: to, lines: lines,
      total: { label: 'Lands in your bank', value: final, currency: to, sub: 'You lose ' + TH.money(Math.max(0, ideal - final), to) + ' versus the mid-market rate.' },
      bar: { keep: final, lose: Math.max(0, ideal - final), label: 'of mid-market' },
      note: 'Payoneer shows the exact rate on the withdrawal screen before you confirm. Use that number in “Exchange rate” for a precise result.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); syncRate(); update(); });
})();
