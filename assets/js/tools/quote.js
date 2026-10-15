(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var itemsEl = document.getElementById('items');
  var KEY = 'th-quote-v1';
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');
  var DEFAULT = { cur: 'USD', items: [['Discovery & planning', 4, 30], ['Design', 12, 30], ['Development', 24, 30]], buffer: 15, rush: 0, discount: 0, pfee: 20, gross: true, deposit: 50 };

  function rowHtml(it) {
    return '<div class="item-row">' +
      '<input class="input" aria-label="Task" placeholder="Task or deliverable" value="' + TH.esc(it[0]) + '">' +
      '<input class="input" aria-label="Hours" inputmode="decimal" value="' + TH.esc(it[1]) + '">' +
      '<input class="input" aria-label="Rate per hour" inputmode="decimal" value="' + TH.esc(it[2]) + '">' +
      '<button type="button" class="del" aria-label="Remove line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>';
  }
  function load() {
    var d = null;
    try { d = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { d = null; }
    d = d || DEFAULT;
    f.cur.value = d.cur; f.buffer.value = d.buffer; f.rush.value = d.rush; f.discount.value = d.discount;
    f.pfee.value = d.pfee; f.gross.checked = !!d.gross; f.deposit.value = d.deposit;
    itemsEl.innerHTML = d.items.map(rowHtml).join('');
  }
  function items() {
    return Array.prototype.map.call(itemsEl.querySelectorAll('.item-row'), function (r) {
      var i = r.querySelectorAll('input');
      return [i[0].value, i[1].value, i[2].value];
    });
  }
  document.getElementById('add-item').addEventListener('click', function () {
    itemsEl.insertAdjacentHTML('beforeend', rowHtml(['', 1, items().length ? items()[0][2] : 25]));
    itemsEl.lastElementChild.querySelector('input').focus();
    update();
  });
  itemsEl.addEventListener('click', function (e) {
    var b = e.target.closest('.del');
    if (b) { b.closest('.item-row').remove(); update(); }
  });

  function update() {
    var cur = f.cur.value;
    var its = items();
    var base = 0, hrs = 0;
    var lines = [];
    its.forEach(function (it) {
      var h = Math.max(0, TH.num(it[1])), r = Math.max(0, TH.num(it[2]));
      base += h * r; hrs += h;
      if (it[0] || h * r) lines.push({ label: (it[0] || 'Untitled') + ' · ' + h + ' h', value: h * r });
    });
    var buffer = base * Math.max(0, TH.num(f.buffer.value)) / 100;
    var rush = (base + buffer) * Math.max(0, TH.num(f.rush.value)) / 100;
    var sub = base + buffer + rush;
    var disc = sub * Math.min(100, Math.max(0, TH.num(f.discount.value))) / 100;
    var net = sub - disc;
    var pfee = Math.min(80, Math.max(0, TH.num(f.pfee.value))) / 100;
    var total = f.gross.checked ? net / (1 - pfee) : net;
    if (buffer) lines.push({ label: 'Revision buffer (' + TH.pct(TH.num(f.buffer.value)) + ')', value: buffer, type: 'plus' });
    if (rush) lines.push({ label: 'Rush fee (' + TH.pct(TH.num(f.rush.value)) + ')', value: rush, type: 'plus' });
    if (disc) lines.push({ label: 'Discount (' + TH.pct(TH.num(f.discount.value)) + ')', value: disc, type: 'minus' });
    if (f.gross.checked && pfee) lines.push({ label: 'Platform fee cover (' + TH.pct(pfee * 100) + ')', value: total - net, type: 'plus' });
    var dep = total * Math.min(100, Math.max(0, TH.num(f.deposit.value))) / 100;
    TH.renderSlip(slip, {
      title: 'Project quote', meta: hrs + ' hours · ' + cur, currency: cur, lines: lines,
      total: { label: 'Quote the client', value: total, sub: (dep ? 'Upfront deposit: ' + TH.money(dep, cur) + ' · ' : '') + 'You keep ' + TH.money(net, cur) + ' after fees' },
      note: 'Effective rate: ' + TH.money(hrs ? net / hrs : 0, cur) + ' per hour after buffer, discount and fees.'
    });
    TH.store(KEY, JSON.stringify({ cur: cur, items: its, buffer: f.buffer.value, rush: f.rush.value, discount: f.discount.value, pfee: f.pfee.value, gross: f.gross.checked, deposit: f.deposit.value }));
  }
  document.getElementById('reset').addEventListener('click', function () { TH.store(KEY, null); load(); update(); TH.toast('Quote reset'); });
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  load();
  update();
})();
