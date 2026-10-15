(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['mode', 'cur', 'cost', 'price', 'target', 'pfee'];
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');
  TH.readParams(f);
  TH.seg(document.getElementById('mode-seg'), update);

  function update() {
    var cur = f.cur.value;
    var mode = f.mode.value;
    document.getElementById('price-box').hidden = mode !== 'margin';
    document.getElementById('target-box').hidden = mode !== 'price';
    var cost = Math.max(0, TH.num(f.cost.value));
    var pfee = Math.min(80, Math.max(0, TH.num(f.pfee.value))) / 100;
    var price, target;
    if (mode === 'price') {
      target = Math.min(95, Math.max(0, TH.num(f.target.value))) / 100;
      // price*(1-pfee) - cost = target*price  → price = cost / (1 - pfee - target)
      var denom = 1 - pfee - target;
      price = denom > 0 ? cost / denom : 0;
    } else {
      price = Math.max(0, TH.num(f.price.value));
    }
    var fee = price * pfee;
    var profit = price - fee - cost;
    var margin = price > 0 ? profit / price * 100 : 0;
    var markup = cost > 0 ? (price - cost) / cost * 100 : 0;
    var lines = [{ label: 'Selling price', value: price }];
    if (fee) lines.push({ label: 'Platform fee (' + TH.pct(pfee * 100) + ')', value: fee, type: 'minus' });
    lines.push({ label: 'Your cost', value: cost, type: 'minus' });
    lines.push({ label: 'Profit margin', text: TH.pct(margin, 2), type: 'info' });
    lines.push({ label: 'Markup on cost', text: cost ? TH.pct(markup, 2) : '—', type: 'info' });
    var bad = mode === 'price' && price === 0 && cost > 0;
    TH.renderSlip(slip, {
      title: mode === 'price' ? 'Price for your margin' : 'Margin check', meta: cur, currency: cur, lines: lines,
      total: mode === 'price'
        ? { label: 'Charge', value: price, sub: bad ? 'Fee plus target margin must stay under 100%.' : 'Profit per sale: ' + TH.money(profit, cur) }
        : { label: 'Profit per sale', value: profit, sub: profit < 0 ? 'You lose money on this price.' : 'That is a ' + TH.pct(margin, 1) + ' margin.' },
      bar: price > 0 ? { keep: Math.max(0, profit), lose: Math.max(0, fee + cost), label: 'profit' } : null,
      note: 'Margin is profit ÷ price. Markup is profit ÷ cost. A 50% markup is only a 33.3% margin.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
