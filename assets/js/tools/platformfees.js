(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['plat', 'ftype', 'famt', 'pamt', 'pcur', 'prior', 'vat', 't1', 't2', 'r1', 'r2', 'r3'];
  var TIERS = { GBP: [250, 5000, 1], USD: [350, 7000, 1.4], EUR: [300, 6000, 1.2] };
  var params = TH.readParams(f);
  TH.seg(document.getElementById('plat-seg'), update);
  TH.seg(document.getElementById('ftype-seg'), update);
  function tierDefaults() { var t = TIERS[f.pcur.value] || TIERS.GBP; f.t1.value = t[0]; f.t2.value = t[1]; }
  if (!params.has('t1')) tierDefaults();
  f.pcur.addEventListener('change', tierDefaults);

  function update() {
    var pph = f.plat.value === 'pph';
    document.getElementById('fl-box').hidden = pph;
    document.getElementById('pph-box').hidden = !pph;
    if (!pph) {
      var hourly = f.ftype.value === 'hourly';
      var a = Math.max(0, TH.num(f.famt.value));
      var fee = a > 0 ? (hourly ? a * 0.10 : Math.max(a * 0.10, 5)) : 0;
      fee = Math.min(fee, a);
      var emp = a > 0 ? (hourly ? a * 0.03 : Math.max(a * 0.03, 3)) : 0;
      var lines = [
        { label: hourly ? 'Hourly payment' : 'Project payment', value: a },
        { label: hourly ? 'Freelancer.com fee (10%)' : 'Project fee (10% or $5 minimum)', value: fee, type: 'minus' },
        { label: 'Client pays on top', text: TH.money(emp) + (hourly ? ' (3%)' : ' (3% or $3)'), type: 'info' }
      ];
      TH.renderSlip(slip, {
        title: 'Your earnings', meta: 'Freelancer.com', currency: 'USD', lines: lines,
        total: { label: 'You earn', value: a - fee, sub: !hourly && a > 0 && a * 0.10 < 5 ? 'The $5 minimum applies — on small projects that’s more than 10%.' : '' },
        bar: { keep: a - fee, lose: fee, label: 'you keep' },
        note: 'Fixed-price fees are charged when you accept the project; hourly fees on each payment. Promotions can reduce fees for some new clients.'
      });
    } else {
      var cur = f.pcur.value;
      var amt = Math.max(0, TH.num(f.pamt.value));
      var prior = Math.max(0, TH.num(f.prior.value));
      var t1 = Math.max(0, TH.num(f.t1.value)), t2 = Math.max(t1, TH.num(f.t2.value));
      var r = [TH.num(f.r1.value) / 100, TH.num(f.r2.value) / 100, TH.num(f.r3.value) / 100];
      var lo = prior, hi = prior + amt;
      function part(a, b) { return Math.max(0, Math.min(hi, b) - Math.max(lo, a)); }
      var p1 = part(0, t1), p2 = part(t1, t2), p3 = part(t2, Infinity);
      var fee = p1 * r[0] + p2 * r[1] + p3 * r[2];
      var minFee = (TIERS[cur] || TIERS.GBP)[2];
      var minUsed = false;
      if (amt > 0 && fee < minFee) { fee = Math.min(minFee, amt); minUsed = true; }
      var vat = f.vat.checked ? fee * 0.2 : 0;
      var l = [{ label: 'Invoice amount', value: amt }];
      if (p1) l.push({ label: TH.money(p1, cur) + ' at ' + TH.pct(r[0] * 100), value: p1 * r[0], type: 'minus' });
      if (p2) l.push({ label: TH.money(p2, cur) + ' at ' + TH.pct(r[1] * 100), value: p2 * r[1], type: 'minus' });
      if (p3) l.push({ label: TH.money(p3, cur) + ' at ' + TH.pct(r[2] * 100), value: p3 * r[2], type: 'minus' });
      if (minUsed) l.push({ label: 'Minimum fee applied', value: fee, type: 'minus' });
      if (vat) l.push({ label: 'VAT on the fee (20%)', value: vat, type: 'minus' });
      l.push({ label: 'Effective fee rate', text: TH.pct(amt ? (fee + vat) / amt * 100 : 0, 2), type: 'info' });
      TH.renderSlip(slip, {
        title: 'Your earnings', meta: 'PeoplePerHour', currency: cur, lines: l,
        total: { label: 'You earn', value: Math.max(0, amt - fee - vat), currency: cur, sub: 'Billed with this client after this invoice: ' + TH.money(hi, cur) },
        bar: { keep: Math.max(0, amt - fee - vat), lose: fee + vat, label: 'you keep' },
        note: 'PeoplePerHour’s fee drops as your lifetime billing with the same client grows. Enter what you’ve already billed this client to see the tier you’re in.'
      });
    }
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
