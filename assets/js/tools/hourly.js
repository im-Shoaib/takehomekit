(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['cur', 'income', 'expenses', 'tax', 'hours', 'off', 'billable', 'pfee'];
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');
  TH.readParams(f);
  var symEls = f.querySelectorAll('.sym');

  function update() {
    var cur = f.cur.value;
    var sym = (TH.CURRENCIES[cur] || {}).sym || '';
    symEls.forEach(function (s) { s.textContent = sym.length > 2 ? '' : sym; });
    var income = Math.max(0, TH.num(f.income.value)) * 12;
    var expenses = Math.max(0, TH.num(f.expenses.value)) * 12;
    var tax = Math.min(80, Math.max(0, TH.num(f.tax.value))) / 100;
    var hours = Math.max(0, TH.num(f.hours.value));
    var off = Math.min(52, Math.max(0, TH.num(f.off.value)));
    var billable = Math.min(100, Math.max(1, TH.num(f.billable.value))) / 100;
    var pfee = Math.min(80, Math.max(0, TH.num(f.pfee.value))) / 100;
    var beforeTax = income / (1 - tax);
    var needed = beforeTax + expenses;
    var gross = needed / (1 - pfee);
    var billHours = hours * billable * (52 - off);
    var rate = billHours > 0 ? gross / billHours : 0;
    var lines = [
      { label: 'Take-home goal (year)', value: income },
      { label: 'Income tax (' + TH.pct(tax * 100) + ')', value: beforeTax - income, type: 'plus' },
      { label: 'Business costs (year)', value: expenses, type: 'plus' },
      { label: 'Platform fees (' + TH.pct(pfee * 100) + ')', value: gross - needed, type: 'plus' },
      { label: 'You must bill per year', value: gross, type: 'sub' },
      { label: 'Billable hours per year', text: Math.round(billHours).toLocaleString('en-US') + ' h', type: 'info' }
    ];
    TH.renderSlip(slip, {
      title: 'Your minimum rate', meta: cur, currency: cur, lines: lines,
      total: { label: 'Charge at least, per hour', value: rate, sub: 'Day rate (' + (hours / 5 * billable).toFixed(1) + ' billable h): ' + TH.money(rate * hours / 5 * billable, cur) + ' · Month: ' + TH.money(gross / 12, cur) },
      note: 'This is your floor, not your price. Add a margin for experience, rush work and demand in your niche.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
