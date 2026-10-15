(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var KEY = 'th-gig-v1';
  var LIMITS = { title: 80, desc: 1200, profile: 600 };
  var MINS = { desc: 120, profile: 150 };

  function meter(name, len, max, min) {
    var row = document.getElementById(name + '-count');
    var bar = document.getElementById(name + '-meter');
    var p = Math.min(100, len / max * 100);
    bar.firstElementChild.style.width = p + '%';
    bar.classList.toggle('over', len > max);
    bar.classList.toggle('warn', len <= max && len > max * 0.92);
    var left = max - len;
    row.innerHTML = '<span>' + (min && len < min ? 'Minimum ' + min + ' characters' : '&nbsp;') + '</span><span class="' + (left < 0 ? 'over' : '') + '">' + len + ' / ' + max +
      (left < 0 ? ' · ' + (-left) + ' over' : ' · ' + left + ' left') + '</span>';
  }

  function check(list, ok, text) { list.push('<li class="' + (ok ? 'ok' : 'bad') + '">' + text + '</li>'); }

  function update() {
    var title = 'I will ' + f.title.value.replace(/^\s*i will\s*/i, '');
    var desc = f.desc.value;
    var profile = f.profile.value;
    var tags = f.tags.value.split(',').map(function (s) { return s.trim(); }).filter(Boolean);
    var kw = f.kw.value.trim().toLowerCase();
    meter('title', title.length, LIMITS.title);
    meter('desc', desc.length, LIMITS.desc, MINS.desc);
    meter('profile', profile.length, LIMITS.profile, MINS.profile);
    document.getElementById('tags-count').innerHTML = '<span>&nbsp;</span><span class="' + (tags.length > 5 ? 'over' : '') + '">' + tags.length + ' / 5 tags</span>';

    var c = [];
    var bare = f.title.value.trim();
    check(c, bare.length >= 10 && title.length <= LIMITS.title, 'Title is specific and within ' + LIMITS.title + ' characters');
    if (kw) {
      check(c, title.toLowerCase().indexOf(kw) > -1, 'Main keyword “' + TH.esc(kw) + '” is in the title');
      check(c, title.toLowerCase().indexOf(kw) > -1 && title.toLowerCase().indexOf(kw) < 40, 'Keyword appears early in the title');
      check(c, desc.toLowerCase().indexOf(kw) > -1, 'Keyword is used in the description');
      check(c, tags.some(function (t) { return t.toLowerCase().indexOf(kw) > -1 || kw.indexOf(t.toLowerCase()) > -1; }), 'A search tag matches your keyword');
    }
    check(c, desc.length >= MINS.desc && desc.length <= LIMITS.desc, 'Description is between ' + MINS.desc + ' and ' + LIMITS.desc + ' characters');
    var contact = /([\w.+-]+@[\w-]+\.[\w.]+)|(https?:\/\/|www\.)|(\+?\d[\d\s-]{8,}\d)|\b(whatsapp|skype|telegram|gmail)\b/i;
    check(c, !contact.test(desc + ' ' + title + ' ' + profile), 'No emails, links, phone numbers or outside apps (Fiverr removes gigs for these)');
    var caps = (desc + title).replace(/[^A-Z]/g, '').length / Math.max(1, (desc + title).replace(/[^A-Za-z]/g, '').length);
    check(c, caps < 0.3, 'Not written in ALL CAPS');
    check(c, tags.length > 0 && tags.length <= 5, 'Up to 5 search tags');
    check(c, tags.every(function (t) { return t.length <= 20; }), 'Each tag is short (20 characters or fewer)');
    if (desc) {
      var paras = desc.split(/\n\s*\n/).filter(function (s) { return s.trim(); }).length;
      check(c, paras >= 2 || /\n\s*[-•*✔✓]/.test(desc), 'Description is broken into paragraphs or bullet points');
    }
    document.getElementById('checks').innerHTML = c.join('');
    var passed = c.filter(function (x) { return x.indexOf('class="ok"') > -1; }).length;
    document.getElementById('score').textContent = passed + ' of ' + c.length + ' checks passed';
    document.getElementById('title-preview').textContent = title.length > 'I will '.length ? title : 'I will …';
    TH.store(KEY, JSON.stringify({ title: f.title.value, desc: desc, profile: profile, tags: f.tags.value, kw: f.kw.value }));
  }
  var saved = null;
  try { saved = JSON.parse(TH.store(KEY) || 'null'); } catch (e) { saved = null; }
  if (saved) ['title', 'desc', 'profile', 'tags', 'kw'].forEach(function (k) { if (saved[k] != null) f[k].value = saved[k]; });
  document.getElementById('copy-title').addEventListener('click', function () { TH.copy('I will ' + f.title.value.replace(/^\s*i will\s*/i, ''), 'Title copied'); });
  document.getElementById('copy-desc').addEventListener('click', function () { TH.copy(f.desc.value, 'Description copied'); });
  document.getElementById('clear').addEventListener('click', function () { ['title', 'desc', 'profile', 'tags', 'kw'].forEach(function (k) { f[k].value = ''; }); update(); });
  f.addEventListener('input', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
