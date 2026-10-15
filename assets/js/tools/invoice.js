(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var DOC = f.getAttribute('data-doc') === 'quote' ? 'quote' : 'invoice';
  var Q = DOC === 'quote';
  var L = Q ? { title: 'Quotation', date2: 'Valid until', grand: 'Total', pay: 'Terms', prefix: 'QT-0001', empty: 'Add an item to start your quote' }
            : { title: 'Invoice', date2: 'Due', grand: 'Total due', pay: 'Payment details', prefix: 'INV-0001', empty: 'Add an item to start' };
  var KEY = Q ? 'th-quotation-v1' : 'th-invoice-v1';
  var itemsEl = document.getElementById('items');
  var paper = document.getElementById('doc-print');
  var logoData = null;
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');

  function today(offset) {
    var d = new Date(); d.setDate(d.getDate() + (offset || 0));
    return d.toISOString().slice(0, 10);
  }
  var DEFAULT = {
    num: L.prefix, issued: today(0), due: today(Q ? 30 : 14), cur: 'USD',
    from: 'Your Name\nYour City, Country\nyou@email.com',
    to: 'Client Name\nCompany\nclient@email.com',
    items: [['Website design (5 pages)', 1, 450], ['Hosting setup & launch', 1, 75]],
    taxp: 0, discp: 0,
    notes: Q ? 'Looking forward to working with you.' : 'Thank you for your business!',
    pay: Q ? '50% upfront, 50% on delivery.\nIncludes 2 rounds of revisions.\nTimeline: 10 working days from deposit.' : 'Payoneer: you@email.com\nBank: Account title / IBAN'
  };

  function rowHtml(it) {
    return '<div class="item-row">' +
      '<input class="input" aria-label="Description" placeholder="Description" value="' + TH.esc(it[0]) + '">' +
      '<input class="input" aria-label="Quantity" inputmode="decimal" value="' + TH.esc(it[1]) + '">' +
      '<input class="input" aria-label="Unit price" inputmode="decimal" value="' + TH.esc(it[2]) + '">' +
      '<button type="button" class="del" aria-label="Remove item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>';
  }
  function collect() {
    return {
      num: f.num.value, issued: f.issued.value, due: f.due.value, cur: f.cur.value,
      from: f.from.value, to: f.to.value,
      items: Array.prototype.map.call(itemsEl.querySelectorAll('.item-row'), function (r) {
        var i = r.querySelectorAll('input'); return [i[0].value, i[1].value, i[2].value];
      }),
      taxp: f.taxp.value, discp: f.discp.value, notes: f.notes.value, pay: f.pay.value, logo: logoData
    };
  }
  function fill(d) {
    ['num', 'issued', 'due', 'cur', 'from', 'to', 'taxp', 'discp', 'notes', 'pay'].forEach(function (k) { if (d[k] != null) f[k].value = d[k]; });
    itemsEl.innerHTML = (d.items || []).map(rowHtml).join('');
    logoData = d.logo || null;
    document.getElementById('logo-clear').hidden = !logoData;
  }
  function totals(d) {
    var sub = 0;
    d.items.forEach(function (it) { sub += Math.max(0, TH.num(it[1])) * TH.num(it[2]); });
    var disc = sub * Math.min(100, Math.max(0, TH.num(d.discp))) / 100;
    var tax = (sub - disc) * Math.max(0, TH.num(d.taxp)) / 100;
    return { sub: sub, disc: disc, tax: tax, total: sub - disc + tax };
  }
  function fmtDate(s) {
    if (!s) return '—';
    var d = new Date(s + 'T00:00:00');
    if (isNaN(d)) return s;
    return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
  }
  function render() {
    var d = collect();
    var t = totals(d);
    var m = function (v) { return TH.esc(TH.money(v, d.cur, { digits: 2 })); };
    var rows = d.items.filter(function (it) { return it[0] || TH.num(it[2]); }).map(function (it) {
      var q = TH.num(it[1]), p = TH.num(it[2]);
      return '<tr><td>' + TH.esc(it[0] || '—') + '</td><td class="num">' + q + '</td><td class="num">' + m(p) + '</td><td class="num">' + m(q * p) + '</td></tr>';
    }).join('');
    paper.innerHTML =
      '<div class="doc-top"><div><div class="doc-title">' + L.title + '</div><div class="muted">' + TH.esc(d.num) + '</div></div>' +
      (logoData ? '<img class="doc-logo" alt="Logo" src="' + logoData + '">' : '') + '</div>' +
      '<div class="doc-parties"><div><div class="muted">From</div>' + TH.esc(d.from) + '</div><div><div class="muted">' + (Q ? 'Prepared for' : 'Bill to') + '</div>' + TH.esc(d.to) + '</div></div>' +
      '<div class="doc-parties"><div><div class="muted">Issued</div>' + fmtDate(d.issued) + '</div><div><div class="muted">' + L.date2 + '</div>' + fmtDate(d.due) + '</div></div>' +
      '<div class="table-wrap"><table><thead><tr><th>Description</th><th class="num">Qty</th><th class="num">Price</th><th class="num">Amount</th></tr></thead><tbody>' + (rows || '<tr><td colspan="4" class="muted">' + L.empty + '</td></tr>') + '</tbody></table></div>' +
      '<div class="doc-totals"><div><span>Subtotal</span><span>' + m(t.sub) + '</span></div>' +
      (t.disc ? '<div><span>Discount (' + TH.num(d.discp) + '%)</span><span>−' + m(t.disc) + '</span></div>' : '') +
      (t.tax ? '<div><span>Tax (' + TH.num(d.taxp) + '%)</span><span>' + m(t.tax) + '</span></div>' : '') +
      '<div class="grand"><span>' + L.grand + '</span><span>' + m(t.total) + '</span></div></div>' +
      (d.pay ? '<div class="doc-notes"><div class="muted">' + L.pay + '</div>' + TH.esc(d.pay) + '</div>' : '') +
      (d.notes ? '<div class="doc-notes">' + TH.esc(d.notes) + '</div>' : '');
    TH.store(KEY, JSON.stringify(d));
  }

  /* logo */
  var logoInput = document.getElementById('logo');
  logoInput.addEventListener('change', function () {
    var file = logoInput.files && logoInput.files[0];
    if (!file) return;
    if (!/^image\//.test(file.type)) { TH.toast('Choose an image file for the logo'); return; }
    var img = new Image();
    var url = URL.createObjectURL(file);
    img.onload = function () {
      var max = 360, s = Math.min(1, max / Math.max(img.width, img.height));
      var c = document.createElement('canvas');
      c.width = Math.max(1, Math.round(img.width * s)); c.height = Math.max(1, Math.round(img.height * s));
      c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
      logoData = c.toDataURL('image/png');
      URL.revokeObjectURL(url);
      document.getElementById('logo-clear').hidden = false;
      render();
    };
    img.onerror = function () { TH.toast('That image could not be read'); URL.revokeObjectURL(url); };
    img.src = url;
  });
  document.getElementById('logo-clear').addEventListener('click', function () { logoData = null; logoInput.value = ''; this.hidden = true; render(); });

  document.getElementById('add-item').addEventListener('click', function () {
    itemsEl.insertAdjacentHTML('beforeend', rowHtml(['', 1, '']));
    itemsEl.lastElementChild.querySelector('input').focus();
    render();
  });
  itemsEl.addEventListener('click', function (e) { var b = e.target.closest('.del'); if (b) { b.closest('.item-row').remove(); render(); } });
  document.getElementById('new-inv').addEventListener('click', function () {
    var d = collect();
    var n = (d.num.match(/(\d+)(?!.*\d)/) || [])[1];
    var next = n ? d.num.replace(/(\d+)(?!.*\d)/, String(+n + 1).padStart(n.length, '0')) : d.num;
    fill({ num: next, issued: today(0), due: today(14), cur: d.cur, from: d.from, to: '', items: [['', 1, '']], taxp: d.taxp, discp: 0, notes: d.notes, pay: d.pay, logo: logoData });
    render();
    TH.toast('New ' + L.title.toLowerCase() + ' ' + next + ' — your details were kept');
  });
  document.getElementById('print-inv').addEventListener('click', function () { window.print(); });

  /* PDF (jsPDF loaded only when needed) */
  function loadJsPdf() {
    return new Promise(function (resolve, reject) {
      if (window.jspdf) return resolve(window.jspdf);
      var s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
      s.async = true;
      s.onload = function () { window.jspdf ? resolve(window.jspdf) : reject(); };
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }
  function plainMoney(v, cur) {
    return cur + ' ' + (v || 0).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  document.getElementById('pdf-inv').addEventListener('click', function () {
    var btn = this;
    btn.disabled = true;
    var old = btn.innerHTML;
    btn.textContent = 'Preparing PDF…';
    loadJsPdf().then(function (lib) {
      var d = collect(), t = totals(d);
      var doc = new lib.jsPDF({ unit: 'pt', format: 'a4' });
      var W = doc.internal.pageSize.getWidth(), H = doc.internal.pageSize.getHeight(), M = 48, y = M;
      var ink = [20, 33, 61], muted = [107, 117, 144];
      doc.setTextColor.apply(doc, ink);
      doc.setFont('helvetica', 'bold'); doc.setFontSize(26); doc.text(L.title, M, y + 18);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(10); doc.setTextColor.apply(doc, muted); doc.text(d.num || '', M, y + 36);
      if (logoData) {
        try {
          var p = doc.getImageProperties(logoData);
          var lw = 120, lh = lw * p.height / p.width;
          if (lh > 60) { lh = 60; lw = lh * p.width / p.height; }
          doc.addImage(logoData, 'PNG', W - M - lw, y, lw, lh);
        } catch (e) { /* ignore bad logo */ }
      }
      y += 76;
      function block(label, text, x, w) {
        doc.setFontSize(9); doc.setTextColor.apply(doc, muted); doc.text(label, x, y);
        doc.setFontSize(10.5); doc.setTextColor.apply(doc, ink);
        var lines = doc.splitTextToSize(text || '—', w);
        doc.text(lines, x, y + 15);
        return lines.length * 13 + 15;
      }
      var colW = (W - 2 * M - 24) / 2;
      var h1 = Math.max(block('From', d.from, M, colW), block(Q ? 'Prepared for' : 'Bill to', d.to, M + colW + 24, colW));
      y += h1 + 14;
      var h2 = Math.max(block('Issued', fmtDate(d.issued), M, colW), block(L.date2, fmtDate(d.due), M + colW + 24, colW));
      y += h2 + 20;
      var cx = [M + 10, W - M - 210, W - M - 120, W - M - 10];
      function head() {
        doc.setFillColor(238, 241, 246); doc.rect(M, y, W - 2 * M, 24, 'F');
        doc.setFont('helvetica', 'bold'); doc.setFontSize(9.5); doc.setTextColor.apply(doc, ink);
        doc.text('Description', cx[0], y + 16);
        doc.text('Qty', cx[1], y + 16, { align: 'right' });
        doc.text('Price', cx[2], y + 16, { align: 'right' });
        doc.text('Amount', cx[3], y + 16, { align: 'right' });
        doc.setFont('helvetica', 'normal'); y += 24;
      }
      head();
      d.items.filter(function (it) { return it[0] || TH.num(it[2]); }).forEach(function (it) {
        var q = TH.num(it[1]), pr = TH.num(it[2]);
        var desc = doc.splitTextToSize(it[0] || '—', cx[1] - cx[0] - 50);
        var rh = Math.max(24, desc.length * 13 + 11);
        if (y + rh > H - 160) { doc.addPage(); y = M; head(); }
        doc.setFontSize(10); doc.setTextColor.apply(doc, ink);
        doc.text(desc, cx[0], y + 16);
        doc.text(String(q), cx[1], y + 16, { align: 'right' });
        doc.text(plainMoney(pr, d.cur), cx[2], y + 16, { align: 'right' });
        doc.text(plainMoney(q * pr, d.cur), cx[3], y + 16, { align: 'right' });
        y += rh;
        doc.setDrawColor(226, 230, 238); doc.line(M, y, W - M, y);
      });
      y += 18;
      var tx = W - M - 220;
      function tline(label, val, bold) {
        doc.setFont('helvetica', bold ? 'bold' : 'normal'); doc.setFontSize(bold ? 12 : 10);
        doc.text(label, tx, y); doc.text(val, W - M - 10, y, { align: 'right' }); y += bold ? 20 : 16;
      }
      tline('Subtotal', plainMoney(t.sub, d.cur));
      if (t.disc) tline('Discount (' + TH.num(d.discp) + '%)', '-' + plainMoney(t.disc, d.cur));
      if (t.tax) tline('Tax (' + TH.num(d.taxp) + '%)', plainMoney(t.tax, d.cur));
      doc.setDrawColor.apply(doc, ink); doc.setLineWidth(1.5); doc.line(tx, y - 6, W - M, y - 6); y += 10;
      tline(L.grand, plainMoney(t.total, d.cur), true);
      doc.setFont('helvetica', 'normal');
      y += 16;
      if (y > H - 120) { doc.addPage(); y = M; }
      if (d.pay) { y += block(L.pay, d.pay, M, W - 2 * M) + 10; }
      if (d.notes) { doc.setFontSize(10); doc.setTextColor.apply(doc, muted); doc.text(doc.splitTextToSize(d.notes, W - 2 * M), M, y + 8); }
      var name = (d.num || DOC).replace(/[^\w\-]+/g, '_') + '.pdf';
      doc.save(name);
      TH.toast('Saved ' + name);
    }).catch(function () {
      TH.toast('PDF library could not load — opening print dialog instead');
      window.print();
    }).then(function () { btn.disabled = false; btn.innerHTML = old; });
  });

  var saved = null;
  try { saved = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { saved = null; }
  fill(saved || DEFAULT);
  f.addEventListener('input', render);
  f.addEventListener('change', render);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  render();
})();
