(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['profit', 'class2'];
  // 2026/27, England, Wales and Northern Ireland
  var PA = 12570, BASIC = 37700, ADD = 125140, TAPER = 100000, LPL = 12570, UPL = 50270;
  TH.readParams(f);
  function update() {
    var profit = Math.max(0, TH.num(f.profit.value));
    var pa = Math.max(0, PA - Math.max(0, profit - TAPER) / 2);
    var taxable = Math.max(0, profit - pa);
    var basic = Math.min(taxable, BASIC);
    var higher = Math.max(0, Math.min(taxable, ADD) - BASIC);
    var additional = Math.max(0, taxable - ADD);
    var it = basic * .20 + higher * .40 + additional * .45;
    var nic4 = Math.max(0, Math.min(profit, UPL) - LPL) * .06 + Math.max(0, profit - UPL) * .02;
    var c2 = f.class2.checked ? 3.65 * 52 : 0;
    var total = it + nic4 + c2;
    var take = profit - total;
    var lines = [{ label: 'Personal allowance', value: pa, type: 'info' }];
    if (basic) lines.push({ label: 'Basic rate 20% on ' + TH.money(basic, 'GBP', { digits: 0 }), value: basic * .2, type: 'minus', currency: 'GBP' });
    if (higher) lines.push({ label: 'Higher rate 40% on ' + TH.money(higher, 'GBP', { digits: 0 }), value: higher * .4, type: 'minus', currency: 'GBP' });
    if (additional) lines.push({ label: 'Additional rate 45% on ' + TH.money(additional, 'GBP', { digits: 0 }), value: additional * .45, type: 'minus', currency: 'GBP' });
    lines.push({ label: 'Class 4 National Insurance', value: nic4, type: 'minus', currency: 'GBP' });
    if (c2) lines.push({ label: 'Voluntary Class 2 (£3.65/week)', value: c2, type: 'minus', currency: 'GBP' });
    lines.push({ label: 'Monthly take-home', value: take / 12, type: 'sub', currency: 'GBP' });
    TH.renderSlip(slip, {
      title: 'UK tax estimate', meta: '2026/27 · England, Wales & NI', currency: 'GBP', lines: lines,
      total: { label: 'You keep after tax', value: take, currency: 'GBP', sub: 'Tax and NI: ' + TH.money(total, 'GBP') + ' (' + TH.pct(profit ? total / profit * 100 : 0) + ' of profit)' },
      bar: profit ? { keep: take, lose: total, label: 'you keep' } : null,
      note: 'Based on trading profit only (income minus allowable expenses). If you also have a job, part of your allowance is used there. Scotland has different income tax bands.' + (profit > TAPER ? ' Your personal allowance is reduced by £1 for every £2 over £100,000.' : '')
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
