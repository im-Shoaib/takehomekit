(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['mode', 'amount', 'rate', 'hours', 'fee', 'connects', 'wd', 'wdc', 'cur', 'conv'];
  var rates = null;
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('PKR', ['USD', 'PKR', 'INR', 'BDT', 'PHP', 'NGN', 'EGP', 'KES', 'LKR', 'NPR', 'IDR', 'VND', 'EUR', 'GBP', 'UAH', 'BRL', 'MXN']);
  TH.readParams(f);
  TH.seg(document.getElementById('mode-seg'), update);
  var feeOut = document.getElementById('fee-out');

  function update() {
    var hourly = f.mode.value === 'hourly';
    document.getElementById('fixed-box').hidden = hourly;
    document.getElementById('hourly-box').hidden = !hourly;
    document.getElementById('wd-custom').hidden = f.wd.value !== 'custom';
    var gross = hourly ? Math.max(0, TH.num(f.rate.value)) * Math.max(0, TH.num(f.hours.value)) : Math.max(0, TH.num(f.amount.value));
    var feeP = Math.min(15, Math.max(0, TH.num(f.fee.value)));
    feeOut.textContent = TH.pct(feeP);
    var fee = gross * feeP / 100;
    var net = gross - fee;
    var connects = Math.max(0, Math.round(TH.num(f.connects.value))) * 0.15;
    var wd = f.wd.value === 'custom' ? TH.num(f.wdc.value) : TH.num(f.wd.value);
    if (net <= 0) wd = 0;
    var take = Math.max(0, net - connects);
    var cur = f.cur.value, conv = TH.num(f.conv.value) / 100;
    var lines = [];
    if (hourly) lines.push({ label: TH.num(f.hours.value) + ' h × ' + TH.money(TH.num(f.rate.value)), value: gross });
    else lines.push({ label: 'Contract payment', value: gross });
    lines.push({ label: 'Upwork service fee (' + TH.pct(feeP) + ')', value: fee, type: 'minus' });
    if (connects) lines.push({ label: 'Connects spent (' + Math.round(TH.num(f.connects.value)) + ' × $0.15)', value: connects, type: 'minus' });
    if (wd) lines.push({ label: 'Withdrawal fee (once per withdrawal)', text: TH.money(wd), type: 'info' });
    var sub = '';
    if (rates && cur !== 'USD') sub = '≈ ' + TH.money(TH.convert(rates, take, 'USD', cur) * (1 - conv), cur) + ' after a ' + TH.pct(conv * 100) + ' conversion spread';
    var note = 'Upwork shows the exact service fee (0–15%) on each job before you send a proposal, and it stays fixed for that contract.';
    if (wd && take > 0) note += ' The ' + TH.money(wd) + ' withdrawal fee is charged once each time you withdraw, whatever the amount — so it isn’t taken from every payment.';
    TH.renderSlip(slip, {
      title: 'Payout slip', meta: hourly ? 'Upwork hourly' : 'Upwork fixed-price', currency: 'USD', lines: lines,
      total: { label: 'You earn from this contract', value: take, sub: sub },
      bar: { keep: take, lose: gross - take },
      note: note
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); update(); });
})();
