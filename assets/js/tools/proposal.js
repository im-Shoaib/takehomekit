(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var out = document.getElementById('gen-out');
  var countEl = document.getElementById('gen-count');
  var KEY = 'th-proposal-v1';
  var FIELDS = ['tone', 'client', 'need', 'goal', 'proof', 'steps', 'timeline', 'price', 'question'];
  var variant = 0;
  TH.seg(document.getElementById('tone-seg'), function () { variant = 0; render(); });

  function lines(t) { return (t || '').split('\n').map(function (x) { return x.replace(/^[-•*\d.)\s]+/, '').trim(); }).filter(Boolean); }
  function cap(s) { s = (s || '').trim(); return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
  function lc(s) { s = (s || '').trim().replace(/[.!]+$/, ''); return s ? s.charAt(0).toLowerCase() + s.slice(1) : s; }
  function end(s) { s = (s || '').trim(); return s && !/[.!?]$/.test(s) ? s + '.' : s; }

  var OPEN = {
    friendly: [
      function (d) { return 'I read your post about ' + lc(d.need) + ', and it’s exactly the kind of project I enjoy.'; },
      function (d) { return 'Your project caught my eye — ' + lc(d.need) + ' is right in my wheelhouse.'; },
      function (d) { return 'I’d love to help you with ' + lc(d.need) + '.'; }
    ],
    professional: [
      function (d) { return 'I’ve reviewed your requirements for ' + lc(d.need) + ' and I’m confident I can deliver what you need.'; },
      function (d) { return 'Thank you for the detailed brief on ' + lc(d.need) + '. Here is how I would approach it.'; },
      function (d) { return 'You need ' + lc(d.need) + ', delivered properly the first time. That is what I do.'; }
    ],
    concise: [
      function (d) { return 'I can handle ' + lc(d.need) + '.'; },
      function (d) { return 'Ready to start on ' + lc(d.need) + ' right away.'; },
      function (d) { return lc(d.need) ? cap(lc(d.need)) + ' — I can do this.' : 'I can do this.'; }
    ]
  };
  function build(d) {
    var t = d.tone || 'friendly';
    var opens = OPEN[t];
    var parts = [];
    var hi = d.client ? (t === 'professional' ? 'Hello ' + d.client + ',' : 'Hi ' + d.client + ',') : (t === 'professional' ? 'Hello,' : 'Hi there,');
    parts.push(hi);
    var p1 = opens[variant % opens.length](d);
    if (d.goal) p1 += ' ' + (t === 'concise' ? 'Goal: ' + lc(d.goal) + '.' : 'I understand the real goal is ' + lc(d.goal) + ', so that’s what I’ll focus on.');
    parts.push(p1);
    if (d.proof) parts.push(t === 'concise' ? 'Relevant work: ' + end(d.proof) : (t === 'friendly' ? 'Why me: ' : 'Relevant experience: ') + end(cap(d.proof)));
    var st = lines(d.steps);
    if (st.length) parts.push((t === 'concise' ? 'Plan:' : 'Here’s how I’d approach it:') + '\n' + st.map(function (s, i) { return (i + 1) + '. ' + end(cap(s)); }).join('\n'));
    var tp = [];
    if (d.timeline) tp.push((t === 'concise' ? 'Timeline: ' : 'Timeline: ') + end(d.timeline));
    if (d.price) tp.push('Price: ' + end(d.price));
    if (tp.length) parts.push(tp.join('\n'));
    if (d.question) parts.push(t === 'concise' ? 'Quick question: ' + end(cap(d.question)).replace(/\.$/, '?') : 'One question before I start: ' + end(cap(d.question)).replace(/\.$/, '?'));
    parts.push(t === 'professional' ? 'I’d be glad to discuss the details. Looking forward to your reply.\n\nBest regards,' : (t === 'concise' ? 'Let me know and I’ll start.' : 'Happy to jump on a quick chat if that helps. Looking forward to hearing from you!\n\nThanks,'));
    return parts.join('\n\n');
  }
  function get() { var d = {}; FIELDS.forEach(function (k) { d[k] = f.elements[k].value.trim(); }); return d; }
  function render() {
    var d = get();
    var txt = build(d);
    out.textContent = txt;
    var words = txt.split(/\s+/).filter(Boolean).length;
    countEl.innerHTML = '<span>' + words + ' words · ' + txt.length + ' characters</span><span class="' + (words > 250 ? 'over' : '') + '">' + (words > 250 ? 'Long — clients skim, aim for under 200 words' : words < 60 ? 'Add a little more detail' : 'Good length') + '</span>';
    TH.store(KEY, JSON.stringify(d));
  }
  var saved = null;
  try { saved = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { saved = null; }
  if (saved) FIELDS.forEach(function (k) { if (saved[k] != null) f.elements[k].value = saved[k]; });
  TH.seg(document.getElementById('tone-seg')).set(f.elements.tone.value, true);
  document.getElementById('copy-gen').addEventListener('click', function () { TH.copy(out.textContent, 'Proposal copied'); });
  document.getElementById('shuffle').addEventListener('click', function () { variant++; render(); });
  f.addEventListener('input', render);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  render();
})();
