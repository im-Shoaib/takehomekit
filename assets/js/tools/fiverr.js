(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var statusEl = document.getElementById('rate-status');
  var keys = ['role', 'price', 'tip', 'wd', 'wdc', 'cur', 'sfee', 'bfee', 'small', 'thr', 'conv'];
  var rates = null;

  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('PKR', ['USD', 'PKR', 'INR', 'BDT', 'PHP', 'NGN', 'EGP', 'KES', 'LKR', 'NPR', 'IDR', 'VND', 'EUR', 'GBP', 'TRY', 'BRL', 'MXN', 'UAH']);
  var noUrl = !!f.dataset.nourl;
  if (!noUrl) TH.readParams(f);
  var role = TH.seg(document.getElementById('role-seg'), update);

  var custom = document.getElementById('wd-custom');
  function toggleCustom() { custom.hidden = f.wd.value !== 'custom'; }

  function update() {
    toggleCustom();
    var R = f.role.value;
    document.getElementById('seller-only').hidden = R !== 'seller';
    var price = Math.max(0, TH.num(f.price.value));
    var tip = Math.max(0, TH.num(f.tip.value));
    var sfee = TH.num(f.sfee.value) / 100;
    var bfee = TH.num(f.bfee.value) / 100;
    var small = TH.num(f.small.value);
    var thr = TH.num(f.thr.value);

    if (R === 'buyer') {
      var svc = price * bfee;
      var smallFee = price > 0 && price < thr ? small : 0;
      var tipFee = tip * bfee;
      var total = price + svc + smallFee + tip + tipFee;
      var sellerGets = (price + tip) * (1 - sfee);
      var lines = [
        { label: 'Gig price', value: price },
        { label: 'Service fee (' + TH.pct(bfee * 100) + ')', value: svc, type: 'plus' }
      ];
      if (smallFee) lines.push({ label: 'Small order fee (under $' + thr + ')', value: smallFee, type: 'plus' });
      if (tip) { lines.push({ label: 'Tip', value: tip }); lines.push({ label: 'Service fee on tip', value: tipFee }); }
      TH.renderSlip(slip, {
        title: 'Checkout total', meta: 'Fiverr buyer', currency: 'USD', lines: lines,
        total: { label: 'You pay at checkout', value: total, sub: 'The seller receives ' + TH.money(sellerGets) + ' after their ' + TH.pct(sfee * 100) + ' fee.' },
        bar: { keep: price + tip, lose: total - price - tip, label: 'to the seller' },
        note: 'Fees added on top of the gig price: ' + TH.money(total - price - tip) + ' (' + TH.pct(price + tip ? (total - price - tip) / (price + tip) * 100 : 0) + ').'
      });
    } else {
      var gross = price + tip;
      var fee = gross * sfee;
      var net = gross - fee;
      var wd = f.wd.value === 'custom' ? TH.num(f.wdc.value) : TH.num(f.wd.value);
      if (net <= 0) wd = 0;
      var cur = f.cur.value;
      var conv = TH.num(f.conv.value) / 100;
      var local = null;
      if (rates && cur !== 'USD') local = TH.convert(rates, net, 'USD', cur) * (1 - conv);
      var l2 = [{ label: 'Order price', value: price }];
      if (tip) l2.push({ label: 'Tip', value: tip });
      l2.push({ label: 'Fiverr service fee (' + TH.pct(sfee * 100) + ')', value: fee, type: 'minus' });
      if (wd) l2.push({ label: 'Withdrawal fee (once per withdrawal)', text: TH.money(wd), type: 'info' });
      var sub = '';
      if (local != null) sub = '≈ ' + TH.money(local, cur) + ' in your bank, after a ' + TH.pct(conv * 100) + ' conversion spread';
      var note = 'Fiverr keeps ' + TH.money(fee) + ' of this order. Funds clear after the usual 7–14 day pending period.';
      if (wd && net > 0) note = 'The ' + TH.money(wd) + ' withdrawal fee is charged once per withdrawal, not per order. Withdraw this order on its own and you get ' +
        TH.money(Math.max(0, net - wd)) + '; withdraw ' + TH.money(net * 5) + ' (five orders like this) together and it costs you just ' + TH.money(wd / 5) + ' per order.';
      TH.renderSlip(slip, {
        title: 'Payout slip', meta: 'Fiverr seller', currency: 'USD', lines: l2,
        total: { label: 'You earn from this order', value: net, sub: sub },
        bar: { keep: net, lose: fee, label: 'you keep' },
        note: note
      });
    }
    if (!noUrl) TH.writeParams(f, keys);
  }

  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); update(); });
  update();
  TH.getRates().then(function (info) { rates = info.rates; TH.rateStatus(statusEl, info); update(); });
})();
