(function () {
  'use strict';
  var f = document.getElementById('calc');
  if (!f) return;
  var slip = document.getElementById('slip');
  var keys = ['cur', 'fixed', 'rate', 'hours', 'overrun', 'pfee'];
  f.querySelector('[name="cur"]').innerHTML = TH.currencyOptions('USD');
  TH.readParams(f);
  function update() {
    var cur = f.cur.value;
    var fixed = Math.max(0, TH.num(f.fixed.value));
    var rate = Math.max(0, TH.num(f.rate.value));
    var hours = Math.max(0, TH.num(f.hours.value));
    var over = Math.max(0, TH.num(f.overrun.value)) / 100;
    var pfee = Math.min(80, Math.max(0, TH.num(f.pfee.value))) / 100;
    var realHours = hours * (1 + over);
    var fixedNet = fixed * (1 - pfee);
    var hourlyNet = rate * realHours * (1 - pfee);
    var effOnTime = hours ? fixedNet / hours : 0;
    var effReal = realHours ? fixedNet / realHours : 0;
    var netRate = rate * (1 - pfee);
    var breakEven = netRate ? fixedNet / netRate : 0;
    var fixedWins = fixedNet >= hourlyNet;
    var diff = Math.abs(fixedNet - hourlyNet);
    TH.renderSlip(slip, {
      title: 'Which pays more?', meta: fixedWins ? 'Fixed price wins' : 'Hourly wins', currency: cur,
      total: { label: 'Fixed price works out to, per hour', value: effReal, sub: 'Your hourly rate after fees: ' + TH.money(netRate, cur) + '. ' + (fixedWins ? 'Fixed' : 'Hourly') + ' earns you ' + TH.money(diff, cur) + ' more on this project.' },
      lines: [
        { label: 'Fixed price, after fees', value: fixedNet, type: fixedWins ? 'sub' : 'plus' },
        { label: 'Hourly for ' + realHours.toFixed(1) + ' h, after fees', value: hourlyNet, type: fixedWins ? 'plus' : 'sub' },
        { label: 'Fixed rate if you finish on time', value: effOnTime, type: 'info' },
        { label: 'Break-even point', text: breakEven.toFixed(1) + ' hours', type: 'info' }
      ],
      note: fixedWins
        ? 'Fixed price pays more as long as the work takes under ' + breakEven.toFixed(1) + ' hours. Protect it with a clear scope and a revision limit.'
        : 'At this estimate the job runs past the break-even point of ' + breakEven.toFixed(1) + ' hours. Bill hourly, or raise the fixed price to at least ' + TH.money(rate * realHours, cur) + '.'
    });
    TH.writeParams(f, keys);
  }
  f.addEventListener('input', update);
  f.addEventListener('change', update);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  update();
})();
