(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['profit', 'status', 'wages', 'qbi', 'inc'];
  // Tax year 2026 (IRS inflation adjustments)
  var Y = {
    wageBase: 184500,
    std: { single: 16100, mfj: 32200 },
    addMed: { single: 200000, mfj: 250000 },
    brackets: {
      single: [[12400, .10], [50400, .12], [105700, .22], [201775, .24], [256225, .32], [640600, .35], [Infinity, .37]],
      mfj: [[24800, .10], [100800, .12], [211400, .22], [403550, .24], [512450, .32], [768700, .35], [Infinity, .37]]
    }
  };
  TH.readParams(f);
  TH.seg(document.getElementById('status-seg'), update);
  function incomeTax(taxable, st) {
    var t = 0, prev = 0;
    Y.brackets[st].forEach(function (b) { if (taxable > prev) { t += (Math.min(taxable, b[0]) - prev) * b[1]; } prev = b[0]; });
    return t;
  }
  function update() {
    var st = f.status.value === 'mfj' ? 'mfj' : 'single';
    var profit = Math.max(0, TH.num(f.profit.value));
    var wages = Math.max(0, TH.num(f.wages.value));
    var base = profit * 0.9235;
    if (base < 400) base = 0;
    var ss = 0.124 * Math.min(base, Math.max(0, Y.wageBase - wages));
    var med = 0.029 * base;
    var addMed = 0.009 * Math.max(0, base - Math.max(0, Y.addMed[st] - wages));
    var se = ss + med;
    var half = se / 2;
    var agi = profit - half + wages;
    var beforeQbi = Math.max(0, agi - Y.std[st]);
    var qbi = f.qbi.checked ? Math.min(0.2 * Math.max(0, profit - half), 0.2 * beforeQbi) : 0;
    var taxable = Math.max(0, beforeQbi - qbi);
    var it = f.inc.checked ? incomeTax(taxable, st) : 0;
    var total = se + addMed + it;
    var lines = [
      { label: 'Social Security (12.4%)', value: ss, type: 'minus' },
      { label: 'Medicare (2.9%)', value: med, type: 'minus' }
    ];
    if (addMed) lines.push({ label: 'Additional Medicare (0.9%)', value: addMed, type: 'minus' });
    lines.push({ label: 'Self-employment tax', value: se + addMed, type: 'sub' });
    if (f.inc.checked) {
      lines.push({ label: 'Taxable income' + (qbi ? ' (after QBI deduction)' : ''), value: taxable, type: 'info' });
      lines.push({ label: 'Federal income tax' + (wages ? ' (on all income)' : ''), value: it, type: 'minus' });
    }
    lines.push({ label: 'Effective rate on profit', text: TH.pct(profit ? total / profit * 100 : 0, 1), type: 'info' });
    TH.renderSlip(slip, {
      title: 'US tax estimate', meta: 'Tax year 2026', currency: 'USD', lines: lines,
      total: { label: f.inc.checked ? 'Total federal tax' : 'Self-employment tax', value: total, sub: 'Quarterly estimated payment: about ' + TH.money(total / 4) + '. Deductible half of SE tax: ' + TH.money(half) + '.' },
      bar: profit ? { keep: Math.max(0, profit + wages - total), lose: total, label: 'you keep' } : null,
      note: 'Federal only — state and local taxes aren’t included. The QBI deduction is simplified and can be limited for higher incomes and some service businesses.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
