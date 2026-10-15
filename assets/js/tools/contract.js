(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var KEY = 'th-contract-v1';
  var paper = document.getElementById('doc-print');
  var FIELDS = ['date', 'freelancer', 'client', 'project', 'scope', 'deliverables', 'start', 'end', 'price', 'cur', 'payment', 'revisions', 'extra', 'ip', 'conf', 'notice', 'law'];
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');
  function today(o) { var d = new Date(); d.setDate(d.getDate() + (o || 0)); return d.toISOString().slice(0, 10); }
  var DEFAULT = {
    date: today(0), freelancer: 'Your Name', client: 'Client Name / Company', project: 'Business website redesign',
    scope: 'Design and build a responsive five-page website based on the client’s brand guidelines.',
    deliverables: 'Homepage design and development\nAbout, Services, Blog and Contact pages\nContact form connected to the client’s email\nBasic on-page SEO setup',
    start: today(3), end: today(24), price: '1200', cur: 'USD', payment: '50-50', revisions: '2', extra: '30',
    ip: true, conf: true, notice: '7', law: 'Pakistan'
  };
  var PAY = {
    '50-50': '50% of the total fee is due before work begins. The remaining 50% is due on delivery, before final files are handed over.',
    '100': 'The full fee is due before work begins.',
    'milestones': 'The fee is paid in three equal milestones: on signing, at the halfway review, and on final delivery.',
    'completion': 'The full fee is due within 7 days of final delivery.'
  };
  function fmtDate(s) { if (!s) return '—'; var d = new Date(s + 'T00:00:00'); return isNaN(d) ? s : d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); }
  function get() {
    var d = {};
    FIELDS.forEach(function (k) { var el = f.elements[k]; d[k] = el.type === 'checkbox' ? el.checked : el.value; });
    return d;
  }
  function sections(d) {
    var price = TH.money(TH.num(d.price), d.cur, { digits: 2 }).replace(/[^\d.,]/g, '');
    var priceTxt = d.cur + ' ' + price;
    var s = [];
    s.push(['Parties', 'This agreement is made on ' + fmtDate(d.date) + ' between ' + (d.freelancer || '[Freelancer]') + ' (“the Freelancer”) and ' + (d.client || '[Client]') + ' (“the Client”).']);
    s.push(['Project and scope', 'The Freelancer will provide the following services for the project “' + (d.project || '[Project]') + '”: ' + (d.scope || '') ]);
    var dl = (d.deliverables || '').split('\n').map(function (x) { return x.trim(); }).filter(Boolean);
    if (dl.length) s.push(['Deliverables', dl.map(function (x, i) { return (i + 1) + '. ' + x; }).join('\n') + '\nAnything not listed here is outside the scope of this agreement.']);
    s.push(['Timeline', 'Work starts on ' + fmtDate(d.start) + ' and is due for delivery by ' + fmtDate(d.end) + '. Delays caused by late feedback, content or approvals from the Client extend the deadline by the same amount of time.']);
    s.push(['Fee and payment', 'The total fee for this project is ' + priceTxt + '. ' + (PAY[d.payment] || '') + ' Payments are made by bank transfer, Payoneer or another method agreed in writing.']);
    s.push(['Revisions and extra work', 'The fee includes ' + (TH.num(d.revisions) || 0) + ' round' + (TH.num(d.revisions) === 1 ? '' : 's') + ' of revisions. Further revisions or work outside the scope will be quoted separately' + (TH.num(d.extra) ? ', at ' + d.cur + ' ' + TH.num(d.extra) + ' per hour,' : '') + ' and started only after the Client agrees in writing.']);
    if (d.ip) s.push(['Ownership', 'Once the Client has paid the full fee, ownership of the final deliverables transfers to the Client. The Freelancer may show the work in their portfolio unless the Client asks otherwise in writing. Tools, code libraries and materials the Freelancer created before this project remain the Freelancer’s property.']);
    if (d.conf) s.push(['Confidentiality', 'Both parties will keep private any confidential business information they receive from each other during this project, and will not share it with third parties without permission.']);
    s.push(['Cancellation', 'Either party may end this agreement with ' + (TH.num(d.notice) || 7) + ' days’ written notice. The Client will pay for all work completed up to the end date. Any deposit covers work already started and is non-refundable.']);
    s.push(['Liability', 'The Freelancer will deliver the work with reasonable skill and care. The Freelancer’s total liability under this agreement is limited to the fee paid.']);
    s.push(['Governing law', 'This agreement is governed by the laws of ' + (d.law || '[country]') + '. The parties will first try to settle any dispute in good faith.']);
    return s;
  }
  function render() {
    var d = get();
    var s = sections(d);
    var html = '<div class="doc-top"><div><div class="doc-title">Freelance Service Agreement</div><div class="muted">' + TH.esc(d.project || '') + '</div></div></div>';
    s.forEach(function (sec, i) {
      html += '<h3>' + (i + 1) + '. ' + TH.esc(sec[0]) + '</h3><p style="white-space:pre-line">' + TH.esc(sec[1]) + '</p>';
    });
    html += '<div class="sign"><div>' + TH.esc(d.freelancer || 'Freelancer') + ' — signature and date</div><div>' + TH.esc(d.client || 'Client') + ' — signature and date</div></div>';
    paper.innerHTML = html;
    paper._sections = s; paper._d = d;
    TH.store(KEY, JSON.stringify(d));
  }
  function plain() {
    var d = paper._d;
    return 'FREELANCE SERVICE AGREEMENT\n' + d.project + '\n\n' + paper._sections.map(function (s, i) { return (i + 1) + '. ' + s[0] + '\n' + s[1]; }).join('\n\n') +
      '\n\n______________________\n' + d.freelancer + '\n\n______________________\n' + d.client;
  }
  var saved = null;
  try { saved = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { saved = null; }
  var d0 = saved || DEFAULT;
  FIELDS.forEach(function (k) { var el = f.elements[k]; if (!el || d0[k] == null) return; if (el.type === 'checkbox') el.checked = !!d0[k]; else el.value = d0[k]; });
  document.getElementById('copy-doc').addEventListener('click', function () { TH.copy(plain(), 'Agreement copied'); });
  document.getElementById('print-doc').addEventListener('click', function () { window.print(); });
  document.getElementById('reset-doc').addEventListener('click', function () {
    FIELDS.forEach(function (k) { var el = f.elements[k]; if (el.type === 'checkbox') el.checked = !!DEFAULT[k]; else el.value = DEFAULT[k]; });
    render(); TH.toast('Reset to the example agreement');
  });
  document.getElementById('pdf-doc').addEventListener('click', function () {
    var btn = this; btn.disabled = true;
    var d = paper._d;
    var blocks = [{ type: 'title', text: 'Freelance Service Agreement' }, { type: 'meta', text: d.project || '' }];
    paper._sections.forEach(function (s, i) { blocks.push({ type: 'h', text: (i + 1) + '. ' + s[0] }); blocks.push({ type: 'p', text: s[1] }); });
    blocks.push({ type: 'sign', left: (d.freelancer || 'Freelancer') + ' — signature & date', right: (d.client || 'Client') + ' — signature & date' });
    THPDF.textDoc('freelance-agreement.pdf', blocks).then(function () { TH.toast('Saved freelance-agreement.pdf'); }, function () { TH.toast('PDF library could not load — opening print instead'); window.print(); })
      .then(function () { btn.disabled = false; });
  });
  f.addEventListener('input', render);
  f.addEventListener('change', render);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  render();
})();
