(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['want', 'wcur', 'platform', 'pfee', 'wd', 'conv'];
  var rates = null;
  var PLATFORMS = {
    fiverr: { name: 'Fiverr', fee: 20, wd: 0 },
    upwork: { name: 'Upwork', fee: 10, wd: 0 },
    freelancer: { name: 'Freelancer.com', fee: 10, wd: 0, min: 5 },
    pph: { name: 'PeoplePerHour', fee: 20, wd: 0 },
    custom: { name: 'Other platform', fee: 15, wd: 0 }
  };
  f.querySelector('[name="wcur"]').innerHTML = TH.currencyOptions('USD', ['USD', 'PKR', 'INR', 'BDT', 'PHP', 'NGN', 'EGP', 'KES', 'LKR', 'EUR', 'GBP']);
  var params = TH.readParams(f);
  function applyDefaults() {
    var p = PLATFORMS[f.platform.value] || PLATFORMS.custom;
    f.pfee.value = p.fee; f.wd.value = p.wd;
  }
  if (!params.has('pfee')) applyDefaults();
  f.platform.addEventListener('change', applyDefaults);

  function update() {
    var p = PLATFORMS[f.platform.value] || PLATFORMS.custom;
    var wcur = f.wcur.value;
    document.getElementById('conv-box').hidden = wcur === 'USD';
    var want = Math.max(0, TH.num(f.want.value));
    var conv = TH.num(f.conv.value) / 100;
    var wantUsd = want;
    if (wcur !== 'USD') {
      if (!rates) { wantUsd = 0; } else wantUsd = TH.convert(rates, want, wcur, 'USD') / Math.max(1e-6, 1 - conv);
    }
    var feeP = Math.min(90, Math.max(0, TH.num(f.pfee.value))) / 100;
    var wd = Math.max(0, TH.num(f.wd.value));
    var needNet = wantUsd + (want > 0 ? wd : 0);
    var price = needNet / (1 - feeP);
    var minNote = '';
    if (p.min && f.platform.value === 'freelancer' && price * feeP < p.min && want > 0) { price = needNet + p.min; minNote = ' Freelancer.com charges at least $5 per fixed-price project, so the minimum applies here.'; }
    var fee = price * feeP;
    var rounded = Math.ceil(price / 5) * 5;
    var lines = [];
    if (wcur !== 'USD') lines.push({ label: 'You want in hand', value: want, currency: wcur });
    lines.push({ label: wcur !== 'USD' ? 'Needed in USD' : 'You want to receive', value: wantUsd });
    if (wd && want > 0) lines.push({ label: 'Withdrawal fee (included)', value: wd, type: 'plus' });
    lines.push({ label: p.name + ' fee (' + TH.pct(feeP * 100) + ')', value: fee, type: 'plus' });
    TH.renderSlip(slip, {
      title: 'Price to charge', meta: p.name, currency: 'USD', lines: lines,
      total: { label: 'Charge at least', value: price, sub: f.platform.value === 'fiverr' && want > 0 ? 'Fiverr packages go in $5 steps, so list it at ' + TH.money(rounded, 'USD', { digits: 0 }) + '.' : '' },
      bar: { keep: wantUsd, lose: price - wantUsd, label: 'you keep' },
      note: 'Fees add ' + TH.pct(wantUsd ? (price - wantUsd) / wantUsd * 100 : 0) + ' on top of what you want to keep.' + minNote
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); update(); });
})();
