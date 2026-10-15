(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var out = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['amount', 'to', 'rate', 'p_fee', 'p_fixed', 'p_sp', 'w_fee', 'w_fixed', 'w_sp', 'b_fee', 'b_fixed', 'b_sp'];
  var rates = null;
  f.querySelector('[name="to"]').innerHTML = TH.currencyOptions('PKR', ['PKR', 'INR', 'BDT', 'PHP', 'NGN', 'EGP', 'KES', 'LKR', 'NPR', 'IDR', 'VND', 'TRY', 'BRL', 'MXN', 'UAH', 'MYR', 'ZAR', 'EUR', 'GBP']);
  var params = TH.readParams(f);
  var userRate = params.has('rate');
  function syncRate() {
    if (!rates) return;
    var r = TH.convert(rates, 1, 'USD', f.to.value);
    if (!userRate) f.rate.value = r >= 100 ? r.toFixed(2) : r.toFixed(4);
  }
  f.rate.addEventListener('input', function () { userRate = f.rate.value !== ''; });
  f.querySelector('[data-reset-rate]').addEventListener('click', function () { userRate = false; syncRate(); update(); });

  function calc(amt, feeP, fixed, sp, rate) {
    var usd = Math.max(0, amt * (1 - feeP / 100) - fixed);
    return { usd: usd, local: usd * rate * (1 - sp / 100) };
  }
  function update(e) {
    if (e && e.target === f.to) { userRate = false; syncRate(); }
    var amt = Math.max(0, TH.num(f.amount.value));
    var rate = TH.num(f.rate.value);
    var to = f.to.value;
    var ideal = amt * rate;
    var list = [
      { n: 'Payoneer', d: 'Conversion spread ' + TH.pct(TH.num(f.p_sp.value)) + (TH.num(f.p_fee.value) ? ' + ' + TH.pct(TH.num(f.p_fee.value)) + ' fee' : ''), r: calc(amt, TH.num(f.p_fee.value), TH.num(f.p_fixed.value), TH.num(f.p_sp.value), rate) },
      { n: 'Wise', d: 'Transfer fee ' + TH.pct(TH.num(f.w_fee.value), 2) + (TH.num(f.w_sp.value) ? ', spread ' + TH.pct(TH.num(f.w_sp.value)) : ', mid-market rate'), r: calc(amt, TH.num(f.w_fee.value), TH.num(f.w_fixed.value), TH.num(f.w_sp.value), rate) },
      { n: 'Bank wire (SWIFT)', d: TH.money(TH.num(f.b_fixed.value)) + ' in wire charges, spread ' + TH.pct(TH.num(f.b_sp.value)), r: calc(amt, TH.num(f.b_fee.value), TH.num(f.b_fixed.value), TH.num(f.b_sp.value), rate) }
    ];
    list.sort(function (a, b) { return b.r.local - a.r.local; });
    var best = list[0].r.local || 1;
    var html = '<div class="res-head"><span class="res-title">What lands in your bank</span><span class="pill gold">USD → ' + TH.esc(to) + '</span></div>' +
      '<div class="res-main"><div class="res-total"><span class="l">Best route: ' + TH.esc(list[0].n) + '</span><output class="v">' + TH.esc(TH.money(list[0].r.local, to)) + '</output>' +
      '<span class="sub2">' + (list[1] ? TH.money(list[0].r.local - list[1].r.local, to) + ' more than ' + list[1].n : '') + '</span></div></div><div class="cmp" style="margin-top:16px">';
    list.forEach(function (it, i) {
      var w = Math.max(2, it.r.local / best * 100);
      var lost = Math.max(0, ideal - it.r.local);
      html += '<div class="cmp-card' + (i === 0 ? ' best' : '') + '"><span class="n">' + (i === 0 ? '★ ' : '') + TH.esc(it.n) + '</span><span class="a">' + TH.esc(TH.money(it.r.local, to)) + '</span>' +
        '<span class="d">' + TH.esc(it.d) + ' · costs ' + TH.esc(TH.money(lost, to)) + ' (' + TH.pct(ideal ? lost / ideal * 100 : 0) + ')</span><span class="bar"><span style="width:' + w.toFixed(1) + '%"></span></span></div>';
    });
    html += '</div><p class="res-note">Defaults are typical costs, not quotes. Edit each provider’s fees under “Provider fees” to match the numbers you see. Wise accounts aren’t available to residents of every country — check eligibility first.</p>' +
      '<div class="res-actions"><button type="button" class="btn btn-ghost btn-small" data-share-link>Share comparison</button></div>';
    out.innerHTML = html;
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); syncRate(); update(); });
})();
