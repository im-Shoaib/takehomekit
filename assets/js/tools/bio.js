(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var box = document.getElementById('variants');
  var KEY = 'th-bio-v1';
  var FIELDS = ['name', 'role', 'years', 'skills', 'clients', 'proof', 'offer', 'tone'];
  TH.seg(document.getElementById('tone-seg'), render);

  function list(arr) {
    if (arr.length <= 1) return arr.join('');
    return arr.slice(0, -1).join(', ') + ' and ' + arr[arr.length - 1];
  }
  function end(s) { s = (s || '').trim(); return s && !/[.!?]$/.test(s) ? s + '.' : s; }
  function lc(s) { s = (s || '').trim(); return s ? s.charAt(0).toLowerCase() + s.slice(1) : s; }
  function get() { var d = {}; FIELDS.forEach(function (k) { d[k] = f.elements[k].value.trim(); }); return d; }

  function make(d) {
    var skills = d.skills.split(',').map(function (s) { return s.trim(); }).filter(Boolean);
    var yrs = TH.num(d.years);
    var exp = yrs ? yrs + '+ year' + (yrs === 1 ? '' : 's') + ' of experience' : '';
    var role = d.role || 'freelancer';
    var t = d.tone || 'warm';
    var fiverr, upwork, headline;
    if (t === 'bold') {
      fiverr = 'I’m ' + (d.name || 'a') + (d.name ? ', a ' : ' ') + lc(role) + (exp ? ' with ' + exp : '') + '. ' +
        (skills.length ? 'I specialise in ' + list(skills.slice(0, 4)) + '. ' : '') +
        (d.clients ? 'I work with ' + lc(end(d.clients)) + ' ' : '') + (d.proof ? end(d.proof) + ' ' : '') +
        (d.offer ? 'Need ' + lc(d.offer.replace(/[.!]+$/, '')) + '? Message me and let’s get it done.' : 'Message me and let’s get it done.');
    } else if (t === 'pro') {
      fiverr = (d.name ? d.name + ' — ' : '') + role + (exp ? ' with ' + exp : '') + '. ' +
        (skills.length ? 'Core skills: ' + list(skills.slice(0, 5)) + '. ' : '') +
        (d.clients ? 'Clients include ' + lc(end(d.clients)) + ' ' : '') + (d.proof ? end(d.proof) + ' ' : '') +
        (d.offer ? 'I offer ' + lc(end(d.offer)) + ' ' : '') + 'Clear communication, on-time delivery and revisions until you’re happy.';
    } else {
      fiverr = 'Hi, I’m ' + (d.name || 'a freelancer') + '! I’m a ' + lc(role) + (exp ? ' with ' + exp : '') + '. ' +
        (skills.length ? 'I love working on ' + list(skills.slice(0, 4)) + '. ' : '') +
        (d.clients ? 'I’ve helped ' + lc(end(d.clients)) + ' ' : '') + (d.proof ? end(d.proof) + ' ' : '') +
        (d.offer ? 'If you need ' + lc(d.offer.replace(/[.!]+$/, '')) + ', I’d love to help. ' : '') + 'Send me a message — I usually reply within a few hours.';
    }
    upwork = (headline = role + (skills.length ? ' | ' + skills.slice(0, 3).join(' | ') : '')) && (
      (d.offer ? 'Looking for someone to ' + lc(d.offer.replace(/[.!]+$/, '')) + '? ' : '') +
      'I’m ' + (d.name || 'a') + (d.name ? ', a ' : ' ') + lc(role) + (exp ? ' with ' + exp : '') + '.\n\n' +
      (skills.length ? 'What I do:\n' + skills.map(function (s) { return '• ' + s; }).join('\n') + '\n\n' : '') +
      (d.clients || d.proof ? 'Results:\n' + (d.clients ? '• Clients: ' + end(d.clients) + '\n' : '') + (d.proof ? '• ' + end(d.proof) + '\n' : '') + '\n' : '') +
      'How I work:\n• Clear scope and timeline before we start\n• Regular updates, no chasing\n• Revisions until it’s right\n\nSend me a message with your project details and I’ll reply with a plan and a quote.');
    return [
      { name: 'Fiverr profile description', text: fiverr.replace(/\s+/g, ' ').trim(), max: 600, min: 150 },
      { name: 'Upwork / LinkedIn overview', text: upwork, max: 5000 },
      { name: 'Profile headline', text: headline, max: 70 }
    ];
  }
  function render() {
    var d = get();
    var vs = make(d);
    box.innerHTML = vs.map(function (v, i) {
      var len = v.text.length;
      var over = len > v.max, under = v.min && len < v.min;
      return '<div class="variant"><div class="vh"><b>' + TH.esc(v.name) + '</b><button type="button" class="btn btn-ghost btn-small" data-copy-v="' + i + '">Copy</button></div>' +
        '<p>' + TH.esc(v.text) + '</p><div class="count-row"><span>' + (under ? 'Fiverr needs at least ' + v.min + ' characters' : '&nbsp;') + '</span><span class="' + (over ? 'over' : '') + '">' + len + ' / ' + v.max + '</span></div></div>';
    }).join('');
    box._v = vs;
    TH.store(KEY, JSON.stringify(d));
  }
  box.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy-v]');
    if (b) TH.copy(box._v[+b.getAttribute('data-copy-v')].text, 'Copied');
  });
  var saved = null;
  try { saved = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { saved = null; }
  if (saved) FIELDS.forEach(function (k) { if (saved[k] != null) f.elements[k].value = saved[k]; });
  TH.seg(document.getElementById('tone-seg')).set(f.elements.tone.value, true);
  f.addEventListener('input', render);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  render();
})();
