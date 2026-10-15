/* Shared helper: lazy-load jsPDF and write flowing text documents. */
(function () {
  'use strict';
  function load() {
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
  /* blocks: [{type:'title'|'h'|'p'|'meta'|'sign', text}] */
  function textDoc(filename, blocks) {
    return load().then(function (lib) {
      var doc = new lib.jsPDF({ unit: 'pt', format: 'a4' });
      var W = doc.internal.pageSize.getWidth(), H = doc.internal.pageSize.getHeight(), M = 56, y = M;
      var ink = [27, 24, 53], muted = [109, 104, 144];
      function need(h) { if (y + h > H - M) { doc.addPage(); y = M; } }
      blocks.forEach(function (b) {
        if (b.type === 'title') {
          doc.setFont('helvetica', 'bold'); doc.setFontSize(22); doc.setTextColor.apply(doc, ink);
          need(30); doc.text(b.text, M, y + 16); y += 34;
          doc.setDrawColor.apply(doc, ink); doc.setLineWidth(1.5); doc.line(M, y, W - M, y); y += 18;
        } else if (b.type === 'meta') {
          doc.setFont('helvetica', 'normal'); doc.setFontSize(9.5); doc.setTextColor.apply(doc, muted);
          var ml = doc.splitTextToSize(b.text, W - 2 * M); need(ml.length * 13); doc.text(ml, M, y); y += ml.length * 13 + 8;
        } else if (b.type === 'h') {
          doc.setFont('helvetica', 'bold'); doc.setFontSize(11.5); doc.setTextColor.apply(doc, ink);
          need(34); y += 8; doc.text(b.text, M, y); y += 16;
        } else if (b.type === 'sign') {
          need(80); y += 40;
          var cw = (W - 2 * M - 40) / 2;
          doc.setDrawColor.apply(doc, ink); doc.setLineWidth(.8);
          doc.line(M, y, M + cw, y); doc.line(M + cw + 40, y, W - M, y);
          doc.setFont('helvetica', 'normal'); doc.setFontSize(9); doc.setTextColor.apply(doc, muted);
          doc.text(b.left, M, y + 14); doc.text(b.right, M + cw + 40, y + 14); y += 30;
        } else {
          doc.setFont('helvetica', 'normal'); doc.setFontSize(10.5); doc.setTextColor.apply(doc, ink);
          var lines = doc.splitTextToSize(b.text, W - 2 * M);
          lines.forEach(function (ln) { need(15); doc.text(ln, M, y); y += 15; });
          y += 6;
        }
      });
      doc.save(filename);
    });
  }
  window.THPDF = { load: load, textDoc: textDoc };
})();
