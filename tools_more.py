# The ten tools added in round two. Appended to TOOLS on import.
from tools_content import TOOLS, I, money_field, pct_field, OUT_SLIP, OUT_SLIP_NORATE

RATE_FIELD = '''<div class="field"><label for="rate">Exchange rate</label><input class="input" id="rate" name="rate" inputmode="decimal" value=""><p class="hint"><button type="button" class="btn btn-ghost btn-small" data-reset-rate style="padding:6px 12px">Use live rate</button></p></div>'''

# ---------------------------------------------------------------- Freelancer.com & PPH
TOOLS.append({
    "slug": "freelancer-peopleperhour-fee-calculator", "js": "platformfees", "cat": "fees", "icon": I["people"],
    "short": "Freelancer.com & PeoplePerHour fees", "blurb": "Project fees, $5 minimums and PPH's tiered client fee.",
    "title": "Freelancer.com & PeoplePerHour Fee Calculator (2026)",
    "desc": "Calculate Freelancer.com fees (10% or $5 minimum) and PeoplePerHour's tiered service fee (20%, 7.5%, 3.5% per client). See exactly what you earn on each project.",
    "h1": "Freelancer.com & PeoplePerHour fee calculator",
    "lede": "Two platforms, two very different fee models. Freelancer.com charges a flat 10% with a $5 minimum; PeoplePerHour's fee falls the more you bill the same client. See your real earnings on either.",
    "related": ["fiverr-fee-calculator", "upwork-fee-calculator", "fiverr-reverse-fee-calculator", "payoneer-to-pkr-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="plat-l">Platform</span>
<div class="seg" id="plat-seg" role="group" aria-labelledby="plat-l"><input type="hidden" name="plat" value="freelancer"><button type="button" data-v="freelancer" aria-pressed="true">Freelancer.com</button><button type="button" data-v="pph" aria-pressed="false">PeoplePerHour</button></div></div>
<div id="fl-box">
<div class="field"><span class="label" id="ft-l">Project type</span>
<div class="seg" id="ftype-seg" role="group" aria-labelledby="ft-l"><input type="hidden" name="ftype" value="fixed"><button type="button" data-v="fixed" aria-pressed="true">Fixed price</button><button type="button" data-v="hourly" aria-pressed="false">Hourly</button></div></div>
''' + money_field("famt", "famt", "Payment amount (USD)", 250) + '''
</div>
<div id="pph-box" hidden>
<div class="row">''' + money_field("pamt", "pamt", "Invoice amount", 400, "", "") + '''
<div class="field"><label for="pcur">Currency</label><select class="input" id="pcur" name="pcur"><option value="GBP">GBP — British Pound</option><option value="USD">USD — US Dollar</option><option value="EUR">EUR — Euro</option></select></div></div>
''' + money_field("prior", "prior", "Already billed this client (lifetime)", 0, "PeoplePerHour's fee tier depends on your total billing with each client.", "") + '''
<label class="check" style="margin-bottom:18px"><input type="checkbox" name="vat"> I'm in the UK or EU and pay VAT on the fee (20%)</label>
<details class="more"><summary>Fee tiers</summary>
<div class="row">''' + money_field("t1", "t1", "Tier 1 up to", 250, "", "") + pct_field("r1", "r1", "Tier 1 fee", 20) + '''</div>
<div class="row">''' + money_field("t2", "t2", "Tier 2 up to", 5000, "", "") + pct_field("r2", "r2", "Tier 2 fee", 7.5) + '''</div>
''' + pct_field("r3", "r3", "Fee above tier 2", 3.5) + '''
</details>
</div>
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>Freelancer.com fees</h2>
<p>Freelancer.com keeps it simple. On <strong>fixed-price projects</strong>, the fee is <strong>10% or $5, whichever is greater</strong>, charged when you accept the project. On <strong>hourly projects</strong> it's a straight <strong>10%</strong> of each payment. Contests work like fixed-price projects: 10% or $5.</p>
<p>The $5 minimum matters on small jobs. A $30 project costs $5 in fees — that's 16.7%, not 10%. Above $50, the 10% rate takes over.</p>
<p>Clients pay their own fee on top: 3% or $3 on fixed-price projects, and 3% on hourly payments. It doesn't come out of your earnings.</p>
<p class="formula">Fixed price: earnings = amount − max(10% × amount, $5)</p>

<h2>PeoplePerHour fees</h2>
<p>PeoplePerHour uses a <strong>tiered fee based on how much you've billed each client over time</strong>. The more work you do for the same client, the lower your fee:</p>
<div class="table-wrap"><table>
<thead><tr><th>Lifetime billing with a client</th><th class="num">Service fee</th></tr></thead>
<tbody>
<tr><td>Up to £250 ($350 / €300)</td><td class="num">20%</td></tr>
<tr><td>£250 to £5,000 ($7,000 / €6,000)</td><td class="num">7.5%</td></tr>
<tr><td>Above £5,000</td><td class="num">3.5%</td></tr>
</tbody></table></div>
<p>There's also a minimum fee of about £1 per invoice, and freelancers in the UK and EU pay VAT on the fee. Sources disagree on the exact thresholds, so the tiers are editable above — check your PeoplePerHour account for the numbers that apply to you.</p>

<h2>Example: £400 invoice to a new client</h2>
<p>The first £250 is charged at 20% (£50) and the next £150 at 7.5% (£11.25). Total fee: £61.25, an effective 15.3%. You earn £338.75. Bill the same client another £400 later and the whole invoice falls in the 7.5% tier.</p>

<h2>Which platform is cheaper?</h2>
<ul>
<li><strong>Small one-off jobs:</strong> Freelancer.com's 10% usually beats PeoplePerHour's 20% first tier — unless the $5 minimum kicks in.</li>
<li><strong>Long-term clients:</strong> PeoplePerHour wins. Once you pass the first tier, 7.5% and then 3.5% are among the lowest marketplace fees around.</li>
<li>Compare with the <a href="/fiverr-fee-calculator/">Fiverr</a> and <a href="/upwork-fee-calculator/">Upwork</a> calculators to see all four side by side.</li>
</ul>''',
    "faq": [
        ("How much does Freelancer.com take from freelancers?", "10% of fixed-price projects or $5, whichever is greater, and 10% of hourly payments."),
        ("Why was I charged $5 on a small Freelancer.com project?", "Fixed-price projects have a $5 minimum fee. On any project under $50, $5 is more than 10%, so the minimum applies."),
        ("What are PeoplePerHour's fees?", "A service fee that drops as your lifetime billing with each client grows: 20% on the first tier, then 7.5%, then 3.5%. A small minimum fee applies per invoice."),
        ("Does PeoplePerHour's fee reset for each project?", "No. It's based on your total billing with the same client across all projects. A new client starts again at the first tier."),
        ("Do I pay VAT on PeoplePerHour fees?", "If you're based in the UK or EU, VAT is usually added to the service fee. Tick the VAT box to include it."),
    ],
})

# ---------------------------------------------------------------- Wise vs Payoneer vs bank
TOOLS.append({
    "slug": "wise-vs-payoneer-vs-bank", "js": "compare", "cat": "payments", "icon": I["scale"],
    "short": "Wise vs Payoneer vs bank", "blurb": "Compare what each route lands in your account.",
    "title": "Wise vs Payoneer vs Bank Transfer — Which Gives More PKR?",
    "desc": "Compare how much you receive in PKR, INR or PHP through Payoneer, Wise or a bank wire. Live exchange rates, editable fees and spreads, and the cheapest route highlighted.",
    "h1": "Wise vs Payoneer vs bank transfer",
    "lede": "Enter the dollars you're bringing home and see, side by side, how much each route leaves in your account after fees and exchange-rate spreads.",
    "related": ["payoneer-to-pkr-calculator", "freelancer-currency-converter", "fiverr-fee-calculator", "pakistan-freelancer-tax-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="row">''' + money_field("amount", "amount", "Amount (USD)", 1000) + '''
<div class="field"><label for="to">To your bank in</label><select class="input" id="to" name="to"></select></div></div>
''' + RATE_FIELD + '''
<details class="more" open><summary>Provider fees</summary>
<p class="hint" style="margin-bottom:14px">Typical costs, pre-filled. Replace them with what your provider actually charges.</p>
<div class="row-3">''' + pct_field("p_fee", "p_fee", "Payoneer fee", 0) + money_field("p_fixed", "p_fixed", "Payoneer fixed", 0) + pct_field("p_sp", "p_sp", "Payoneer spread", 2) + '''</div>
<div class="row-3">''' + pct_field("w_fee", "w_fee", "Wise fee", 0.7) + money_field("w_fixed", "w_fixed", "Wise fixed", 0) + pct_field("w_sp", "w_sp", "Wise spread", 0) + '''</div>
<div class="row-3">''' + pct_field("b_fee", "b_fee", "Bank fee", 0) + money_field("b_fixed", "b_fixed", "Wire charges", 20) + pct_field("b_sp", "b_sp", "Bank spread", 1.5) + '''</div>
</details>
</form>''' + OUT_SLIP,
    "content": '''<h2>Where the money goes</h2>
<p>Every route from a dollar balance to your local bank costs something. The costs come in three forms, and providers mix them differently:</p>
<ul>
<li><strong>A percentage fee</strong> — Wise shows its fee upfront as a percentage of the transfer.</li>
<li><strong>A fixed fee</strong> — bank wires often lose $15–30 to sending and intermediary banks.</li>
<li><strong>An exchange-rate spread</strong> — the gap between the mid-market rate and the rate you get. Payoneer's conversion to local currency is up to about 2% below mid-market, and many banks are similar or higher.</li>
</ul>
<p class="formula">Received = (amount × (1 − fee %) − fixed fee) × mid-market rate × (1 − spread %)</p>

<h2>Typical result on $1,000 to PKR</h2>
<p>With a mid-market rate of Rs 277, a 2% Payoneer spread leaves about Rs 2,71,460. A transfer with a 0.7% fee at the mid-market rate leaves about Rs 2,75,061. A bank wire losing $20 in charges and 1.5% on the rate leaves about Rs 2,67,388. The gap between the best and worst route is close to Rs 8,000 — on every $1,000.</p>

<h2>Things the numbers don't show</h2>
<ul>
<li><strong>Availability.</strong> Wise doesn't offer accounts to residents of every country, and not every marketplace pays into every provider. Check what works for you before comparing.</li>
<li><strong>Speed.</strong> Local bank withdrawals through Payoneer usually take one to three business days; SWIFT wires can take longer.</li>
<li><strong>Proof of income.</strong> In Pakistan, keep the bank's Proceeds Realisation Certificate for each transfer. It supports the reduced tax rate on IT exports — see the <a href="/pakistan-freelancer-tax-calculator/">Pakistan freelancer tax calculator</a>.</li>
</ul>''',
    "faq": [
        ("Is Wise cheaper than Payoneer for PKR?", "Often, when Wise is available to you: Wise converts at the mid-market rate and charges a small visible fee, while Payoneer's spread is up to about 2%. Enter the fees you actually see to compare."),
        ("Why does my bank give a worse rate?", "Banks add a margin to the exchange rate, and SWIFT transfers can lose a fixed amount to intermediary banks before the money arrives."),
        ("Are the default fees accurate?", "They're typical figures, not quotes. Providers set fees by country and change them. Replace them with your own numbers under Provider fees."),
        ("Can Pakistani freelancers open a Wise account?", "Wise sets eligibility by country of residence and has not offered personal accounts to residents of every country. Check Wise's own eligibility page before relying on it."),
    ],
})

# ---------------------------------------------------------------- Fixed vs hourly
TOOLS.append({
    "slug": "fixed-price-vs-hourly-calculator", "js": "fixedhourly", "cat": "pricing", "icon": I["split"],
    "short": "Fixed price vs hourly", "blurb": "Which billing model pays more for this project.",
    "title": "Fixed Price vs Hourly Calculator — Which Pays More?",
    "desc": "Compare a fixed-price offer against your hourly rate. Includes scope creep, platform fees and the break-even point, so you know which way to bill before you accept.",
    "h1": "Fixed price vs hourly calculator",
    "lede": "A client offers a fixed price. Is it a good deal? Compare it with billing by the hour — including the extra hours projects usually take — and see the break-even point.",
    "related": ["hourly-rate-calculator", "project-quote-calculator", "profit-margin-calculator", "upwork-fee-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
<div class="row">''' + money_field("fixed", "fixed", "Fixed price offered", 600, "", "") + money_field("rate", "rate", "Your hourly rate", 25, "", "") + '''</div>
<div class="row">''' + pct_field("hours", "hours", "Estimated hours", 20, "", "h") + pct_field("overrun", "overrun", "Expected overrun", 25, "Extra time from revisions and scope creep") + '''</div>
''' + pct_field("pfee", "pfee", "Platform fee", 10, "Applied to both options") + '''
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>The real question: how long will it take?</h2>
<p>A fixed price is a bet on your estimate. Finish faster than planned and you earn more per hour than your rate. Run over — through extra revisions, unclear briefs or scope creep — and your effective rate drops with every hour.</p>
<p>That's why the calculator asks for an <strong>expected overrun</strong>. Most freelancers underestimate; 20–30% is a realistic buffer for projects with any uncertainty.</p>
<p class="formula">Effective rate = fixed price after fees ÷ (estimated hours × (1 + overrun))</p>
<p class="formula">Break-even hours = fixed price after fees ÷ hourly rate after fees</p>

<h2>Example</h2>
<p>A client offers $600 for a job you estimate at 20 hours. Your rate is $25/hour and the platform takes 10%.</p>
<div class="table-wrap"><table><tbody>
<tr><td>Fixed price after fees</td><td class="num">$540</td></tr>
<tr><td>Hours with 25% overrun</td><td class="num">25 h</td></tr>
<tr><td>Hourly for 25 h, after fees</td><td class="num">$562.50</td></tr>
<tr><td>Fixed price per hour</td><td class="num">$21.60</td></tr>
<tr><th>Break-even</th><th class="num">24 h</th></tr>
</tbody></table></div>
<p>If the job really takes 25 hours, hourly pays $22.50 more. If you finish in 20, fixed pays $90 more. The break-even of 24 hours tells you how much room you have.</p>

<h2>When to choose each</h2>
<ul>
<li><strong>Fixed price</strong> suits clearly defined work you've done many times — you're fast, and the client gets certainty.</li>
<li><strong>Hourly</strong> suits open-ended work, ongoing support and clients who keep changing their minds.</li>
<li><strong>Fixed with limits</strong> is often best: a fixed price with a set number of revisions, and hourly billing for anything beyond. Put that in writing with the <a href="/freelance-contract-generator/">contract generator</a>.</li>
</ul>''',
    "faq": [
        ("Is fixed price or hourly better for freelancers?", "Fixed price pays more when you can finish faster than the estimate; hourly protects you when the work is uncertain. Compare both with a realistic overrun."),
        ("What is the break-even point?", "The number of hours at which both options pay the same. Finish under it and fixed price wins; go over it and hourly wins."),
        ("How much overrun should I assume?", "20–30% for typical projects. Use more for new clients, vague briefs or work with many stakeholders."),
        ("How do I protect a fixed-price project?", "Agree a written scope, a fixed number of revisions and an hourly rate for extra work before you start."),
    ],
})

# ---------------------------------------------------------------- Quotation generator
TOOLS.append({
    "slug": "quotation-generator", "js": "invoice", "cat": "documents", "icon": I["quote"], "appcat": "BusinessApplication",
    "short": "Quotation generator", "blurb": "A clean quote PDF to send before the work starts.",
    "title": "Free Quotation Generator for Freelancers — Download PDF",
    "desc": "Create a professional quotation for your client in any currency. Add items, terms, validity date and your logo, then download a PDF. Free, no sign-up, nothing uploaded.",
    "h1": "Free quotation generator",
    "lede": "Send clients a clear, professional quote before you start. Add your items, terms and validity date — the quote updates as you type and downloads as a PDF.",
    "related": ["invoice-generator", "project-quote-calculator", "freelance-contract-generator", "hourly-rate-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off" data-doc="quote">
<div class="row-3"><div class="field"><label for="num">Quote number</label><input class="input" id="num" name="num"></div>
<div class="field"><label for="issued">Issued</label><input class="input" type="date" id="issued" name="issued"></div>
<div class="field"><label for="due">Valid until</label><input class="input" type="date" id="due" name="due"></div></div>
<div class="row"><div class="field"><label for="from">From (you)</label><textarea class="input" id="from" name="from" rows="3"></textarea></div>
<div class="field"><label for="to">Prepared for</label><textarea class="input" id="to" name="to" rows="3"></textarea></div></div>
<div class="row"><div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
<div class="field"><label for="logo">Logo (optional)</label><input class="input" type="file" id="logo" accept="image/*"><button type="button" class="btn btn-ghost btn-small" id="logo-clear" hidden>Remove logo</button></div></div>
<div class="field"><span class="label">Items</span>
<div class="item-row item-head" aria-hidden="true"><span>Description</span><span>Qty</span><span>Price</span><span></span></div>
<div class="items" id="items"></div>
<div><button type="button" class="btn btn-ghost btn-small" id="add-item">Add item</button></div></div>
<div class="row">''' + pct_field("taxp", "taxp", "Tax", 0) + pct_field("discp", "discp", "Discount", 0) + '''</div>
<div class="field"><label for="pay">Terms</label><textarea class="input" id="pay" name="pay" rows="3"></textarea><p class="hint">Payment schedule, revisions included, timeline.</p></div>
<div class="field"><label for="notes">Notes</label><textarea class="input" id="notes" name="notes" rows="2"></textarea></div>
</form>
<div class="tool-out">
<div class="doc-paper" id="doc-print"></div>
<div class="res-actions">
<button type="button" class="btn" id="pdf-inv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>Download PDF</button>
<button type="button" class="btn btn-ghost" id="print-inv">Print</button>
<button type="button" class="btn btn-ghost" id="new-inv">New quote</button></div>
</div>''',
    "content": '''<h2>Quote vs invoice</h2>
<p>A <strong>quotation</strong> is sent <em>before</em> the work: it tells the client what you'll do and what it will cost, and is valid until a set date. An <strong>invoice</strong> is sent <em>after</em> (or during) the work and asks for payment. Many clients — especially companies — need a quote to approve a budget before they can hire you.</p>

<h2>What a good quote includes</h2>
<ul>
<li>A quote number and the date it was issued</li>
<li>A “valid until” date — 15 to 30 days is common, so old prices don't come back to bite you</li>
<li>Itemised deliverables with prices, so the client sees exactly what they're paying for</li>
<li>Terms: payment schedule (for example 50% upfront), revisions included and the timeline</li>
<li>Your contact details and the client's</li>
</ul>

<h2>From quote to signed project</h2>
<ol>
<li>Work out your price with the <a href="/project-quote-calculator/">project quote calculator</a>.</li>
<li>Send this quotation for approval.</li>
<li>Once accepted, put the scope in writing with the <a href="/freelance-contract-generator/">contract generator</a>.</li>
<li>Bill with the <a href="/invoice-generator/">invoice generator</a> — your details are remembered.</li>
</ol>''',
    "faq": [
        ("Is the quotation generator free?", "Yes — no sign-up, no watermark and no limit."),
        ("How long should a quote be valid?", "15 to 30 days is typical. It protects you from clients accepting an old price months later."),
        ("Can I turn a quote into an invoice?", "Open the invoice generator and add the same items. Your own details are stored separately for each, in this browser only."),
        ("Is my quote saved?", "Yes, in your browser's local storage on this device. Nothing is uploaded."),
    ],
})

# ---------------------------------------------------------------- Contract generator
TOOLS.append({
    "slug": "freelance-contract-generator", "js": "contract", "cat": "documents", "icon": I["pen"], "appcat": "BusinessApplication",
    "short": "Freelance contract generator", "blurb": "Plain-language agreement for scope and payment.",
    "title": "Free Freelance Contract Generator — Simple Agreement PDF",
    "desc": "Generate a plain-language freelance service agreement: scope, deliverables, timeline, payment terms, revisions, ownership and cancellation. Download as PDF or copy. Free.",
    "h1": "Freelance contract generator",
    "lede": "Fill in the project details and get a clear, plain-language service agreement covering scope, payment, revisions and ownership. Download it as a PDF or copy it into an email.",
    "related": ["quotation-generator", "invoice-generator", "fixed-price-vs-hourly-calculator", "project-quote-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="row"><div class="field"><label for="freelancer">Your name</label><input class="input" id="freelancer" name="freelancer"></div>
<div class="field"><label for="client">Client</label><input class="input" id="client" name="client"></div></div>
<div class="row"><div class="field"><label for="project">Project name</label><input class="input" id="project" name="project"></div>
<div class="field"><label for="date">Agreement date</label><input class="input" type="date" id="date" name="date"></div></div>
<div class="field"><label for="scope">Scope of work</label><textarea class="input" id="scope" name="scope" rows="3"></textarea></div>
<div class="field"><label for="deliverables">Deliverables</label><textarea class="input" id="deliverables" name="deliverables" rows="4"></textarea><p class="hint">One per line.</p></div>
<div class="row"><div class="field"><label for="start">Start date</label><input class="input" type="date" id="start" name="start"></div>
<div class="field"><label for="end">Delivery date</label><input class="input" type="date" id="end" name="end"></div></div>
<div class="row">''' + money_field("price", "price", "Total fee", 1200, "", "") + '''
<div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div></div>
<div class="field"><label for="payment">Payment terms</label><select class="input" id="payment" name="payment">
<option value="50-50">50% upfront, 50% on delivery</option><option value="100">100% upfront</option><option value="milestones">Three equal milestones</option><option value="completion">Full payment within 7 days of delivery</option></select></div>
<div class="row">''' + pct_field("revisions", "revisions", "Revision rounds", 2, "", "×") + money_field("extra", "extra", "Rate for extra work / hour", 30, "", "") + '''</div>
<div class="row">''' + pct_field("notice", "notice", "Cancellation notice", 7, "", "days") + '''
<div class="field"><label for="law">Governing law</label><input class="input" id="law" name="law"></div></div>
<label class="check" style="margin-bottom:12px"><input type="checkbox" name="ip"> Ownership transfers to the client after full payment</label>
<label class="check"><input type="checkbox" name="conf"> Include a confidentiality clause</label>
</form>
<div class="tool-out">
<div class="doc-paper" id="doc-print"></div>
<div class="res-actions">
<button type="button" class="btn" id="pdf-doc"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>Download PDF</button>
<button type="button" class="btn btn-ghost" id="copy-doc">Copy text</button>
<button type="button" class="btn btn-ghost" id="print-doc">Print</button>
<button type="button" class="btn btn-ghost" id="reset-doc">Reset</button></div>
<p class="hint" style="margin-top:12px">A starting point, not legal advice. For large projects, have a lawyer review it.</p>
</div>''',
    "content": '''<h2>Why a simple contract matters</h2>
<p>Most freelance disputes come from three things: unclear scope, endless revisions and late payment. A one-page agreement that both sides read before work starts prevents almost all of them. It doesn't need legal jargon — it needs to be specific.</p>

<h2>What this agreement covers</h2>
<ol>
<li><strong>Parties and project</strong> — who is working with whom, on what.</li>
<li><strong>Scope and deliverables</strong> — exactly what's included, and that anything else is extra.</li>
<li><strong>Timeline</strong> — start and delivery dates, and what happens if feedback is late.</li>
<li><strong>Fee and payment</strong> — the total and when each part is due.</li>
<li><strong>Revisions and extra work</strong> — how many rounds are included and the rate beyond that.</li>
<li><strong>Ownership</strong> — the client owns the final work once they've paid in full.</li>
<li><strong>Confidentiality, cancellation, liability and governing law.</strong></li>
</ol>

<h2>Tips for using it</h2>
<ul>
<li><strong>Be specific in the deliverables.</strong> “Five-page website” is better than “website”. “Two logo concepts, three revision rounds” is better than “logo design”.</li>
<li><strong>Get agreement in writing.</strong> A signed PDF is best, but a client replying “I agree” by email is far better than nothing.</li>
<li><strong>On Fiverr and Upwork</strong>, the platform's terms govern the order. Use this to put the scope in writing and attach it to the order or contract.</li>
</ul>''',
    "faq": [
        ("Is this contract legally binding?", "A written agreement both parties accept is generally enforceable, but laws vary by country. This template is a plain-language starting point, not legal advice — have a lawyer review it for large or high-risk projects."),
        ("Do I need a contract for Fiverr or Upwork orders?", "The platform's terms apply to marketplace orders, but a written scope still prevents disputes. For direct clients, a contract is essential."),
        ("Can I edit the generated text?", "Yes. Copy the text into Word or Google Docs and change anything you need, or adjust the fields here and download a new PDF."),
        ("Is my information stored?", "Only in your browser on this device, so you can come back to it. Nothing is uploaded."),
    ],
})

# ---------------------------------------------------------------- Proposal generator
TOOLS.append({
    "slug": "upwork-proposal-generator", "js": "proposal", "cat": "gig", "icon": I["send"], "appcat": "BusinessApplication",
    "short": "Proposal template generator", "blurb": "Upwork proposals that answer the client's brief.",
    "title": "Upwork Proposal Generator — Free Cover Letter Template",
    "desc": "Write a winning Upwork proposal in minutes. Fill in the client's need, your proof and your plan, choose a tone, and get a focused cover letter with a word count. Free.",
    "h1": "Upwork proposal generator",
    "lede": "Clients skim proposals in seconds. Answer their brief, show proof, give a plan and ask one smart question — fill in the blanks and get a focused proposal ready to send.",
    "related": ["fiverr-profile-bio-generator", "upwork-fee-calculator", "fixed-price-vs-hourly-calculator", "hourly-rate-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="tone-l">Tone</span>
<div class="seg" id="tone-seg" role="group" aria-labelledby="tone-l"><input type="hidden" name="tone" value="friendly"><button type="button" data-v="friendly" aria-pressed="true">Friendly</button><button type="button" data-v="professional" aria-pressed="false">Professional</button><button type="button" data-v="concise" aria-pressed="false">Concise</button></div></div>
<div class="row"><div class="field"><label for="client">Client's name (optional)</label><input class="input" id="client" name="client" placeholder="Sarah"></div>
<div class="field"><label for="price">Price (optional)</label><input class="input" id="price" name="price" placeholder="$450 fixed"></div></div>
<div class="field"><label for="need">What they need</label><input class="input" id="need" name="need" value="a fast, mobile-friendly Shopify store"></div>
<div class="field"><label for="goal">Their real goal</label><input class="input" id="goal" name="goal" value="more sales from mobile visitors"><p class="hint">The outcome behind the task. Clients hire for results.</p></div>
<div class="field"><label for="proof">Your most relevant proof</label><textarea class="input" id="proof" name="proof" rows="2">I recently rebuilt a skincare store on Shopify and its mobile conversion rate rose 38% in two months</textarea></div>
<div class="field"><label for="steps">Your plan</label><textarea class="input" id="steps" name="steps" rows="4">Audit your current store and speed
Design a clean mobile-first theme
Set up products, payments and shipping
Test on real devices and launch</textarea><p class="hint">One step per line.</p></div>
<div class="row"><div class="field"><label for="timeline">Timeline</label><input class="input" id="timeline" name="timeline" value="10 working days"></div>
<div class="field"><label for="question">One question for them</label><input class="input" id="question" name="question" value="do you already have product photos ready"></div></div>
</form>
<div class="tool-out"><div class="result"><div class="res-head"><span class="res-title">Your proposal</span><button type="button" class="btn btn-ghost btn-small" id="shuffle">Try another opening</button></div>
<pre class="gen-out" id="gen-out"></pre><div class="count-row" id="gen-count" style="margin-top:10px"></div>
<div class="res-actions"><button type="button" class="btn" id="copy-gen"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>Copy proposal</button></div></div></div>''',
    "content": '''<h2>What makes a proposal win</h2>
<p>Clients on Upwork often receive dozens of proposals and read only the first two lines before deciding. A winning proposal is short, specific and about <em>them</em>, not you. This generator follows a structure that works:</p>
<ol>
<li><strong>Open with their project</strong>, not your name or “Dear Sir”. Show you read the brief.</li>
<li><strong>Name the real goal.</strong> They asked for a Shopify store; they want more sales.</li>
<li><strong>Give one piece of proof</strong> — a similar project with a result.</li>
<li><strong>Lay out a short plan</strong>, so they can picture working with you.</li>
<li><strong>Ask one smart question.</strong> It invites a reply, and replies lead to interviews.</li>
</ol>

<h2>Mistakes to avoid</h2>
<ul>
<li><strong>Copy-paste templates.</strong> Clients spot them instantly. Change the need, goal and proof for every job.</li>
<li><strong>Long life stories.</strong> Aim for 120–200 words. The counter tells you when you're too long.</li>
<li><strong>Listing every skill.</strong> One relevant result beats ten technologies.</li>
<li><strong>Ignoring the client's questions.</strong> If the job post asks something, answer it in the first lines.</li>
</ul>

<h2>Before you send</h2>
<p>Check the job's service fee and Connects cost with the <a href="/upwork-fee-calculator/">Upwork fee calculator</a>, and make sure your price covers them using the <a href="/fiverr-reverse-fee-calculator/">reverse fee calculator</a>.</p>''',
    "faq": [
        ("How long should an Upwork proposal be?", "Usually 120–200 words. Long enough to show you understood the job and have a plan, short enough to read in under a minute."),
        ("Does this use AI?", "No. It assembles your own details into a proven structure, instantly and privately in your browser. That keeps the proposal specific to you."),
        ("Should I include my price in the proposal?", "If the job is fixed-price or the client asked, yes. Otherwise you can discuss it after they reply."),
        ("Can I use this for Fiverr buyer requests or email?", "Yes. The structure — their need, proof, plan, question — works for any client message."),
    ],
})

# ---------------------------------------------------------------- Bio generator
TOOLS.append({
    "slug": "fiverr-profile-bio-generator", "js": "bio", "cat": "gig", "icon": I["user"], "appcat": "BusinessApplication",
    "short": "Profile bio generator", "blurb": "A focused seller bio within platform limits.",
    "title": "Fiverr & Upwork Profile Bio Generator — Free Description Writer",
    "desc": "Generate a Fiverr profile description (150–600 characters), an Upwork overview and a headline from your skills and results. Three tones, live character counts, one-click copy.",
    "h1": "Profile bio generator",
    "lede": "Turn your skills, experience and results into a Fiverr description that fits the 600-character limit, a structured Upwork overview and a headline — in the tone you choose.",
    "related": ["upwork-proposal-generator", "fiverr-gig-character-counter", "fiverr-gig-image-resizer", "fiverr-fee-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="tone-l">Tone</span>
<div class="seg" id="tone-seg" role="group" aria-labelledby="tone-l"><input type="hidden" name="tone" value="warm"><button type="button" data-v="warm" aria-pressed="true">Warm</button><button type="button" data-v="pro" aria-pressed="false">Professional</button><button type="button" data-v="bold" aria-pressed="false">Bold</button></div></div>
<div class="row"><div class="field"><label for="name">Your first name</label><input class="input" id="name" name="name" value="Ali"></div>
<div class="field"><label for="years">Years of experience</label><input class="input" id="years" name="years" inputmode="numeric" value="4"></div></div>
<div class="field"><label for="role">Your role</label><input class="input" id="role" name="role" value="WordPress developer"></div>
<div class="field"><label for="skills">Main skills</label><input class="input" id="skills" name="skills" value="custom themes, Elementor, WooCommerce, speed optimization"><p class="hint">Separate with commas. The first three or four matter most.</p></div>
<div class="field"><label for="clients">Who you've worked with</label><input class="input" id="clients" name="clients" value="small businesses and startups in the US and UK"></div>
<div class="field"><label for="proof">A result you're proud of</label><input class="input" id="proof" name="proof" value="Over 200 projects delivered with a 5-star average"></div>
<div class="field"><label for="offer">What clients can hire you for</label><input class="input" id="offer" name="offer" value="a fast, good-looking website that brings in customers"></div>
</form>
<div class="tool-out"><div class="result"><div class="res-head"><span class="res-title">Your bios</span><span class="pill gold">3 versions</span></div><div class="variants" id="variants"></div></div></div>''',
    "content": '''<h2>Profile limits to know</h2>
<div class="table-wrap"><table>
<thead><tr><th>Where</th><th class="num">Length</th></tr></thead>
<tbody>
<tr><td>Fiverr profile description</td><td class="num">150–600 characters</td></tr>
<tr><td>Upwork profile overview</td><td class="num">Up to 5,000 characters</td></tr>
<tr><td>Profile headline / title</td><td class="num">Keep under ~70 characters</td></tr>
</tbody></table></div>

<h2>What a strong bio does</h2>
<ul>
<li><strong>Says what you do in the first sentence.</strong> Visitors decide in seconds.</li>
<li><strong>Names who you help.</strong> “Small businesses in the UK” is more convincing than “clients worldwide”.</li>
<li><strong>Shows one concrete result.</strong> A number — projects, reviews, revenue, speed — builds trust fast.</li>
<li><strong>Ends with a next step.</strong> Invite them to message you.</li>
</ul>

<h2>Choosing a tone</h2>
<p><strong>Warm</strong> works well on Fiverr, where buyers often hire a person they like. <strong>Professional</strong> suits agencies and corporate clients. <strong>Bold</strong> is short and confident — good when you have strong numbers to back it up.</p>
<p>Avoid emails, links and phone numbers in your Fiverr profile — Fiverr doesn't allow contact details. Check your gig text with the <a href="/fiverr-gig-character-counter/">gig character counter</a>.</p>''',
    "faq": [
        ("What is the Fiverr profile description limit?", "Between 150 and 600 characters. The counter turns red if your Fiverr version goes over."),
        ("Does this use AI?", "No. It builds your bio from your own details using proven structures, instantly and privately in your browser."),
        ("How long should an Upwork overview be?", "Most strong overviews are 1,000–2,000 characters: a clear opening, what you do, results and how you work."),
        ("Can I edit the generated bio?", "Yes. Copy it and adjust the wording so it sounds like you — that's the best final step."),
    ],
})

# ---------------------------------------------------------------- Pakistan tax
TOOLS.append({
    "slug": "pakistan-freelancer-tax-calculator", "js": "pktax", "cat": "tax", "icon": I["moon"],
    "short": "Pakistan freelancer tax", "blurb": "IT export remittance tax and filer status.",
    "title": "Pakistan Freelancer Tax Calculator 2026-27 — 0.25% PSEB vs 1%",
    "desc": "Estimate tax on freelance income in Pakistan for tax year 2026-27: 0.25% final tax with PSEB registration or 1% without. Converts USD to PKR at live rates. Free.",
    "h1": "Pakistan freelancer tax calculator",
    "lede": "Freelancers exporting IT services from Pakistan can pay a low final tax on foreign remittances. See your tax at 0.25% with PSEB registration or 1% without — and what filing your return saves you.",
    "related": ["payoneer-to-pkr-calculator", "wise-vs-payoneer-vs-bank", "fiverr-fee-calculator", "invoice-generator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="period-l">Income entered is</span>
<div class="seg" id="period-seg" role="group" aria-labelledby="period-l"><input type="hidden" name="period" value="annual"><button type="button" data-v="annual" aria-pressed="true">Per year</button><button type="button" data-v="monthly" aria-pressed="false">Per month</button></div></div>
<div class="row"><div class="field"><label for="amount">Foreign income received</label><div class="input-money"><span class="sym" id="amt-sym">$</span><input class="input" id="amount" name="amount" inputmode="decimal" value="12000"></div></div>
<div class="field"><label for="icur">In</label><select class="input" id="icur" name="icur"><option value="USD">US dollars</option><option value="PKR">Pakistani rupees</option></select></div></div>
<div id="rate-box">''' + RATE_FIELD + '''</div>
<div class="field"><span class="label" id="pseb-l">Registered with PSEB?</span>
<div class="seg" id="pseb-seg" role="group" aria-labelledby="pseb-l"><input type="hidden" name="pseb" value="yes"><button type="button" data-v="yes" aria-pressed="true">Yes</button><button type="button" data-v="no" aria-pressed="false">No</button></div></div>
<div class="field"><span class="label" id="atl-l">On the Active Taxpayers List (filed your return)?</span>
<div class="seg" id="atl-seg" role="group" aria-labelledby="atl-l"><input type="hidden" name="atl" value="yes"><button type="button" data-v="yes" aria-pressed="true">Yes</button><button type="button" data-v="no" aria-pressed="false">No</button></div></div>
</form>''' + OUT_SLIP,
    "content": '''<h2>How freelancers are taxed in Pakistan</h2>
<p>Income from exporting computer software, IT and IT-enabled services — which covers most online freelancing — can be taxed under a <strong>final tax regime</strong> on the foreign remittance (section 154A of the Income Tax Ordinance). For tax year 2026-27 the rates are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Status</th><th class="num">Final tax on remittances</th></tr></thead>
<tbody>
<tr><td>Registered with and certified by PSEB</td><td class="num">0.25%</td></tr>
<tr><td>Not registered with PSEB</td><td class="num">1%</td></tr>
</tbody></table></div>
<p>The tax is usually deducted by your bank when the remittance arrives through proper banking channels, and the 0.25% rate is set to apply for tax years 2026 to 2029.</p>
<p class="formula">Tax = annual remittances in PKR × 0.25% (PSEB) or 1% (not registered)</p>

<h2>Conditions for the low rate</h2>
<ul>
<li><strong>File your income tax return</strong> and stay on the Active Taxpayers List (ATL).</li>
<li>File withholding statements, if they apply to you.</li>
<li>Bring the money in through banking channels and keep the bank's <strong>Proceeds Realisation Certificate (PRC)</strong> for each transfer.</li>
<li>Don't claim a credit for foreign taxes paid on the same income.</li>
</ul>
<p>If the conditions aren't met, the final-tax treatment doesn't apply and the income can be taxed at normal individual slab rates, which are much higher. Filing your return on time is the biggest saving available.</p>

<h2>Example</h2>
<p>$12,000 a year at Rs 277 is Rs 33,24,000. At 0.25% the tax is Rs 8,310 for the year — about Rs 693 a month. Without PSEB registration, at 1%, it's Rs 33,240.</p>
<p>See what reaches your account before tax with the <a href="/payoneer-to-pkr-calculator/">Payoneer to PKR calculator</a>.</p>''',
    "faq": [
        ("How much tax do freelancers pay in Pakistan?", "For IT and IT-enabled service exports, a final tax of 0.25% on foreign remittances if you're registered with PSEB, or 1% if you're not — provided you file your return and meet the conditions."),
        ("How do I register with PSEB as a freelancer?", "Through the Pakistan Software Export Board's online registration for freelancers. Registration is renewed periodically; check pseb.org.pk for the current process and fee."),
        ("What if I'm not a filer?", "The reduced final-tax regime requires a filed return. Non-filers can lose the concession and be taxed at normal rates, so filing is the first thing to do."),
        ("Is the tax deducted automatically?", "Usually your bank deducts it when the remittance is received through banking channels. Keep each Proceeds Realisation Certificate for your return."),
        ("Is this tax advice?", "No. It's an estimate based on published rates. Rules change with each budget — confirm with FBR or a tax adviser."),
    ],
})

# ---------------------------------------------------------------- US tax
TOOLS.append({
    "slug": "self-employment-tax-calculator", "js": "ustax", "cat": "tax", "icon": I["globe"],
    "short": "US self-employment tax", "blurb": "Social Security and Medicare on 1099 income.",
    "title": "Self-Employment Tax Calculator 2026 — 1099 Freelancer Taxes",
    "desc": "Calculate 2026 self-employment tax (15.3%) and estimated federal income tax for freelancers and 1099 contractors. Uses the $184,500 wage base, 2026 brackets and standard deduction.",
    "h1": "Self-employment tax calculator",
    "lede": "As a US freelancer you pay both halves of Social Security and Medicare. Enter your net profit to see your 2026 self-employment tax, estimated federal income tax and quarterly payments.",
    "related": ["uk-freelancer-tax-calculator", "hourly-rate-calculator", "profit-margin-calculator", "invoice-generator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="status-l">Filing status</span>
<div class="seg" id="status-seg" role="group" aria-labelledby="status-l"><input type="hidden" name="status" value="single"><button type="button" data-v="single" aria-pressed="true">Single</button><button type="button" data-v="mfj" aria-pressed="false">Married filing jointly</button></div></div>
''' + money_field("profit", "profit", "Net self-employment profit (year)", 60000, "Income minus business expenses — Schedule C line 31.") + '''
''' + money_field("wages", "wages", "W-2 wages (if any)", 0, "Used for the Social Security cap and your tax bracket.") + '''
<label class="check" style="margin-bottom:12px"><input type="checkbox" name="inc" checked> Include federal income tax estimate</label>
<label class="check"><input type="checkbox" name="qbi" checked> Apply the 20% qualified business income (QBI) deduction</label>
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>How self-employment tax works</h2>
<p>Employees split Social Security and Medicare with their employer. When you're self-employed, you pay both halves: <strong>15.3%</strong> in total — 12.4% for Social Security and 2.9% for Medicare.</p>
<ul>
<li>It applies to <strong>92.35%</strong> of your net profit (the employer-equivalent portion is excluded).</li>
<li>The Social Security part stops at the <strong>2026 wage base of $184,500</strong>, combined with any W-2 wages.</li>
<li>Medicare has no cap, and an extra <strong>0.9%</strong> applies above $200,000 (single) or $250,000 (married filing jointly).</li>
<li>You owe it once net earnings reach $400.</li>
</ul>
<p class="formula">SE tax = profit × 92.35% × 15.3% (Social Security part capped at $184,500)</p>
<p>Half of your SE tax is deductible when working out your income tax.</p>

<h2>2026 federal income tax brackets</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rate</th><th class="num">Single</th><th class="num">Married filing jointly</th></tr></thead>
<tbody>
<tr><td>10%</td><td class="num">up to $12,400</td><td class="num">up to $24,800</td></tr>
<tr><td>12%</td><td class="num">to $50,400</td><td class="num">to $100,800</td></tr>
<tr><td>22%</td><td class="num">to $105,700</td><td class="num">to $211,400</td></tr>
<tr><td>24%</td><td class="num">to $201,775</td><td class="num">to $403,550</td></tr>
<tr><td>32%</td><td class="num">to $256,225</td><td class="num">to $512,450</td></tr>
<tr><td>35%</td><td class="num">to $640,600</td><td class="num">to $768,700</td></tr>
<tr><td>37%</td><td class="num">above</td><td class="num">above</td></tr>
</tbody></table></div>
<p>The 2026 standard deduction is $16,100 (single) and $32,200 (married filing jointly).</p>

<h2>Quarterly estimated payments</h2>
<p>Freelancers don't have tax withheld, so the IRS expects estimated payments four times a year. The calculator divides your total by four as a starting point. Setting aside 25–30% of every payment you receive is a simple habit that avoids a surprise in April.</p>''',
    "faq": [
        ("What is the self-employment tax rate for 2026?", "15.3% on 92.35% of net profit: 12.4% Social Security up to the $184,500 wage base, plus 2.9% Medicare with no cap."),
        ("Do I pay self-employment tax and income tax?", "Yes. SE tax covers Social Security and Medicare; income tax is separate. Half of your SE tax is deducted when calculating income tax."),
        ("What is the QBI deduction?", "A deduction of up to 20% of qualified business income for many self-employed people. It phases out for higher incomes in some service fields; the calculator uses a simplified version."),
        ("Does this include state tax?", "No — federal only. Most states add their own income tax."),
        ("Is this tax advice?", "No. It's an estimate using 2026 IRS figures. Your actual tax depends on credits, deductions and other income."),
    ],
})

# ---------------------------------------------------------------- UK tax
TOOLS.append({
    "slug": "uk-freelancer-tax-calculator", "js": "uktax", "cat": "tax", "icon": I["pound"],
    "short": "UK freelancer tax", "blurb": "Income tax and National Insurance for sole traders.",
    "title": "UK Self-Employed Tax Calculator 2026/27 — Income Tax & Class 4 NI",
    "desc": "Work out income tax and Class 4 National Insurance on your self-employed profit for 2026/27. Personal allowance taper, higher and additional rates, and monthly take-home.",
    "h1": "UK freelancer tax calculator",
    "lede": "Enter your trading profit to see income tax, Class 4 National Insurance and what you keep for 2026/27 in England, Wales and Northern Ireland.",
    "related": ["self-employment-tax-calculator", "hourly-rate-calculator", "freelancer-peopleperhour-fee-calculator", "invoice-generator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
''' + money_field("profit", "profit", "Trading profit for the year", 45000, "Income minus allowable expenses.", "£") + '''
<label class="check"><input type="checkbox" name="class2"> Add voluntary Class 2 National Insurance (£3.65 a week)</label>
<p class="hint" style="margin-top:14px">Class 2 is no longer compulsory. Some people with low profits pay it voluntarily to protect their State Pension record.</p>
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>Income tax for 2026/27</h2>
<p>Self-employed people pay income tax on their <strong>trading profit</strong> — income minus allowable expenses — through Self Assessment. For England, Wales and Northern Ireland:</p>
<div class="table-wrap"><table>
<thead><tr><th>Band</th><th class="num">Taxable income</th><th class="num">Rate</th></tr></thead>
<tbody>
<tr><td>Personal allowance</td><td class="num">up to £12,570</td><td class="num">0%</td></tr>
<tr><td>Basic rate</td><td class="num">£12,571 to £50,270</td><td class="num">20%</td></tr>
<tr><td>Higher rate</td><td class="num">£50,271 to £125,140</td><td class="num">40%</td></tr>
<tr><td>Additional rate</td><td class="num">over £125,140</td><td class="num">45%</td></tr>
</tbody></table></div>
<p>The personal allowance falls by £1 for every £2 of income over £100,000, reaching zero at £125,140. Scotland sets its own income tax bands.</p>

<h2>National Insurance</h2>
<ul>
<li><strong>Class 4:</strong> 6% on profits between £12,570 and £50,270, and 2% above that.</li>
<li><strong>Class 2:</strong> no longer compulsory. You can pay £3.65 a week voluntarily to fill gaps in your National Insurance record.</li>
</ul>
<p class="formula">Class 4 NI = 6% × (profit between £12,570 and £50,270) + 2% × (profit above £50,270)</p>

<h2>Example: £45,000 profit</h2>
<div class="table-wrap"><table><tbody>
<tr><td>Income tax (20% on £32,430)</td><td class="num">£6,486</td></tr>
<tr><td>Class 4 NI (6% on £32,430)</td><td class="num">£1,945.80</td></tr>
<tr><th>You keep</th><th class="num">£36,568.20</th></tr>
</tbody></table></div>

<h2>Paying it</h2>
<p>Tax for the year is due by 31 January after the tax year ends. Once your bill is over £1,000, HMRC usually asks for <strong>payments on account</strong> — two advance payments towards next year's bill, due in January and July. Putting aside a share of every invoice keeps it painless.</p>''',
    "faq": [
        ("How much tax does a self-employed person pay in the UK?", "Income tax at 20%, 40% or 45% above the £12,570 personal allowance, plus Class 4 National Insurance at 6% (2% above £50,270) on trading profit."),
        ("Do I still have to pay Class 2 National Insurance?", "No. Class 2 stopped being compulsory from April 2024. You can still pay it voluntarily to protect your State Pension record."),
        ("What counts as trading profit?", "Your self-employed income minus allowable business expenses, such as equipment, software and platform fees."),
        ("Does this work for Scotland?", "Class 4 NI is the same, but Scotland has different income tax bands, so the income tax figure would differ."),
        ("Is this tax advice?", "No. It's an estimate using 2026/27 rates for England, Wales and Northern Ireland."),
    ],
})
