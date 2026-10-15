(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var drop = document.getElementById('drop');
  var file = document.getElementById('file');
  var canvas = document.getElementById('canvas');
  var ctx = canvas.getContext('2d');
  var info = document.getElementById('img-info');
  var dl = document.getElementById('download');
  var editor = document.getElementById('editor');
  var img = null, name = 'gig-image';
  var fx = 0.5, fy = 0.5; // focal point for crop mode

  function size() {
    var v = f.size.value.split('x');
    return { w: +v[0], h: +v[1] };
  }
  function draw() {
    if (!img) return;
    var s = size();
    canvas.width = s.w; canvas.height = s.h;
    var mode = f.fit.value;
    document.getElementById('bg-box').hidden = mode !== 'contain';
    document.getElementById('drag-hint').hidden = mode !== 'cover';
    document.getElementById('zoom-box').hidden = mode !== 'cover';
    ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = 'high';
    ctx.fillStyle = f.bg.value || '#ffffff';
    ctx.fillRect(0, 0, s.w, s.h);
    var iw = img.naturalWidth, ih = img.naturalHeight;
    var scale = mode === 'cover' ? Math.max(s.w / iw, s.h / ih) : Math.min(s.w / iw, s.h / ih);
    scale *= mode === 'cover' ? (TH.num(f.zoom.value) / 100) : 1;
    var dw = iw * scale, dh = ih * scale;
    var dx, dy;
    if (mode === 'cover') {
      dx = Math.min(0, Math.max(s.w - dw, s.w / 2 - fx * dw));
      dy = Math.min(0, Math.max(s.h - dh, s.h / 2 - fy * dh));
    } else { dx = (s.w - dw) / 2; dy = (s.h - dh) / 2; }
    ctx.drawImage(img, dx, dy, dw, dh);
    var upscale = scale > 1.01;
    info.innerHTML = 'Original ' + iw + ' × ' + ih + ' px → <b>' + s.w + ' × ' + s.h + ' px</b>' +
      (upscale ? ' · <span style="color:var(--red)">Your image is being enlarged ' + Math.round(scale * 100) + '%, it may look soft. Start from a larger image if you can.</span>' : '');
  }
  function load(fl) {
    if (!fl || !/^image\//.test(fl.type)) { TH.toast('Choose a JPG, PNG or WebP image'); return; }
    name = fl.name.replace(/\.[^.]+$/, '').replace(/[^\w\-]+/g, '-').slice(0, 60) || 'gig-image';
    var url = URL.createObjectURL(fl);
    var im = new Image();
    im.onload = function () { img = im; fx = 0.5; fy = 0.5; f.zoom.value = 100; editor.hidden = false; drop.hidden = true; draw(); };
    im.onerror = function () { TH.toast('That image could not be opened'); };
    im.src = url;
  }
  drop.addEventListener('click', function () { file.click(); });
  drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); file.click(); } });
  file.addEventListener('change', function () { load(file.files[0]); });
  ['dragenter', 'dragover'].forEach(function (t) { drop.addEventListener(t, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
  ['dragleave', 'drop'].forEach(function (t) { drop.addEventListener(t, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
  drop.addEventListener('drop', function (e) { if (e.dataTransfer.files[0]) load(e.dataTransfer.files[0]); });
  document.addEventListener('paste', function (e) {
    var it = e.clipboardData && Array.prototype.find.call(e.clipboardData.items, function (i) { return i.type.indexOf('image') === 0; });
    if (it) load(it.getAsFile());
  });
  document.getElementById('change').addEventListener('click', function () { file.value = ''; file.click(); });

  // drag to reposition
  var dragging = false, sx, sy, sfx, sfy;
  canvas.addEventListener('pointerdown', function (e) {
    if (f.fit.value !== 'cover' || !img) return;
    dragging = true; sx = e.clientX; sy = e.clientY; sfx = fx; sfy = fy;
    canvas.setPointerCapture(e.pointerId);
  });
  canvas.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    var r = canvas.getBoundingClientRect();
    var s = size();
    var scale = Math.max(s.w / img.naturalWidth, s.h / img.naturalHeight) * TH.num(f.zoom.value) / 100;
    var k = s.w / r.width;
    fx = Math.min(1, Math.max(0, sfx - (e.clientX - sx) * k / (img.naturalWidth * scale)));
    fy = Math.min(1, Math.max(0, sfy - (e.clientY - sy) * k / (img.naturalHeight * scale)));
    draw();
  });
  canvas.addEventListener('pointerup', function () { dragging = false; });
  canvas.addEventListener('pointercancel', function () { dragging = false; });

  dl.addEventListener('click', function () {
    if (!img) return;
    var fmt = f.format.value;
    var s = size();
    canvas.toBlob(function (blob) {
      if (!blob) { TH.toast('Export failed — try PNG'); return; }
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = name + '-' + s.w + 'x' + s.h + (fmt === 'image/png' ? '.png' : '.jpg');
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
      TH.toast('Downloaded ' + a.download + ' (' + (blob.size / 1024 / 1024).toFixed(2) + ' MB)');
    }, fmt, 0.92);
  });
  f.addEventListener('input', draw);
  f.addEventListener('change', draw);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
})();
