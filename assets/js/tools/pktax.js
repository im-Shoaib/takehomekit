(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['amount', 'icur', 'period', 'rate', 'pseb', 'atl'];
  var rates = null;
  var params = TH.readParams(f);
  var userRate = params.has('rate');
  TH.seg(document.getElementById('period-seg'), update);
  TH.seg(document.getElementById('pseb-seg'), update);
  TH.seg(document.getElementById('atl-seg'), update);
  function syncRate() { if (rates && !userRate) f.rate.value = TH.convert(rates, 1, 'USD', 'PKR').toFixed(2); }
  f.rate.addEventListener('input', function () { userRate = f.rate.value !== ''; });
  f.querySelector('[data-reset-rate]').addEventListener('click', function () { userRate = false; syncRate(); update(); });

  function update() {
    var usd = f.icur.value === 'USD';
    document.getElementById('rate-box').hidden = !usd;
    document.querySelector('#amt-sym').textContent = usd ? '$' : 'Rs';
    var amt = Math.max(0, TH.num(f.amount.value));
    var rate = TH.num(f.rate.value) || 0;
    var monthly = f.period.value === 'monthly';
    var annualPkr = (usd ? amt * rate : amt) * (monthly ? 12 : 1);
    var pseb = f.pseb.value === 'yes';
    var atl = f.atl.value === 'yes';
    var r = pseb ? 0.0025 : 0.01;
    var tax = annualPkr * r;
    var alt = annualPkr * (pseb ? 0.01 : 0.0025);
    var lines = [
      { label: 'Annual remittances', value: annualPkr, currency: 'PKR' },
      { label: 'Final tax rate (section 154A)', text: TH.pct(r * 100, 2), type: 'info' },
      { label: 'Tax for the year', value: tax, currency: 'PKR', type: 'minus' },
      { label: 'Per month', value: tax / 12, currency: 'PKR', type: 'info' }
    ];
    var sub = pseb ? 'Without PSEB registration you’d pay ' + TH.money(alt, 'PKR') + ' (1%).' : 'Register with PSEB and pay ' + TH.money(alt, 'PKR') + ' instead — you’d save ' + TH.money(tax - alt, 'PKR') + '.';
    TH.renderSlip(slip, {
      title: 'Freelancer tax estimate', meta: 'Tax year 2026-27', currency: 'PKR', lines: lines,
      total: { label: 'Estimated tax', value: tax, currency: 'PKR', sub: sub },
      bar: { keep: annualPkr - tax, lose: tax, label: 'you keep' },
      note: atl
        ? 'The reduced final-tax rate applies when you file your return (and statements, if required) and stay on the Active Taxpayers List. Banks usually deduct this tax when your remittance arrives.'
        : '<b style="color:var(--fee)">Not on the Active Taxpayers List:</b> the concessional final-tax treatment requires a filed return, so your income could be taxed at normal slab rates — often far higher. Filing your return is the single biggest saving here.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); syncRate(); update(); });
})();
