# Content + UI markup for every tool page. Plain strings (not f-strings).

def ico(d):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>'

I = {
    "receipt": ico('<path d="M6 3h12v18l-2-1.3L14 21l-2-1.3L10 21l-2-1.3L6 21z"/><path d="M9 8h6M9 12h6M9 16h3"/>'),
    "brief": ico('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>'),
    "target": ico('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>'),
    "bank": ico('<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>'),
    "fx": ico('<circle cx="8" cy="9" r="5"/><circle cx="16" cy="15" r="5"/><path d="M6.5 9h3M8 7.5v3"/>'),
    "clock": ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "list": ico('<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/>'),
    "pie": ico('<path d="M12 3a9 9 0 1 0 9 9h-9z"/><path d="M15 3.5A9 9 0 0 1 20.5 9H15z"/>'),
    "doc": ico('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
    "text": ico('<path d="M4 6V4h16v2M12 4v16M9 20h6"/>'),
    "image": ico('<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-8 8"/>'),
    "scale": ico('<path d="M12 4v16M5 20h14M6 8h12M6 8l-3 6a3 3 0 0 0 6 0zM18 8l-3 6a3 3 0 0 0 6 0z"/>'),
    "pen": ico('<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M14 6l4 4"/>'),
    "user": ico('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'),
    "flag": ico('<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>'),
    "swap": ico('<path d="M7 7h12l-3-3M17 17H5l3 3"/>'),
    "people": ico('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A5 5 0 0 1 21.5 19"/>'),
    "split": ico('<path d="M12 3v6M12 9l-6 6v6M12 9l6 6v6"/>'),
    "send": ico('<path d="M21 3L10 14"/><path d="M21 3l-7 18-4-7-7-4z"/>'),
    "calc": ico('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M16 11h0M8 15h2M12 15h2M8 18h6"/>'),
    "tag": ico('<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="8" cy="8" r="1.5"/>'),
    "spark": ico('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>'),
    "quote": ico('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h3M9 17h6M15 13h0"/>'),
    "globe": ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'),
    "pound": ico('<path d="M17 20H7c2-1 3-3 3-6V8a4 4 0 0 1 7.5-2"/><path d="M6 13h8"/>'),
    "moon": ico('<path d="M12 3l2.4 4.9 5.4.8-3.9 3.8.9 5.4L12 15.4 7.2 17.9l.9-5.4L4.2 8.7l5.4-.8z"/>'),
}

CATEGORIES = [
    {"id": "fees", "name": "Fees & earnings", "desc": "What each platform keeps, and what reaches you.", "icon": I["receipt"]},
    {"id": "payments", "name": "Payments & currency", "desc": "Withdrawals, exchange rates and the cheapest route home.", "icon": I["bank"]},
    {"id": "pricing", "name": "Pricing", "desc": "Rates and quotes that cover your costs, fees and time.", "icon": I["tag"]},
    {"id": "documents", "name": "Documents", "desc": "Invoices, quotes and contracts, ready in a minute.", "icon": I["doc"]},
    {"id": "gig", "name": "Gig & profile", "desc": "Win more work on Fiverr and Upwork.", "icon": I["spark"]},
    {"id": "tax", "name": "Tax", "desc": "Estimates for freelancers in Pakistan, the US and the UK.", "icon": I["calc"]},
]

SOON = []

def money_field(id_, name, label, value, hint="", sym="$"):
    h = '<p class="hint">' + hint + '</p>' if hint else ''
    return ('<div class="field"><label for="' + id_ + '">' + label + '</label><div class="input-money"><span class="sym">' + sym + '</span>'
            '<input class="input" id="' + id_ + '" name="' + name + '" inputmode="decimal" value="' + str(value) + '"></div>' + h + '</div>')

def pct_field(id_, name, label, value, hint="", suf="%"):
    h = '<p class="hint">' + hint + '</p>' if hint else ''
    return ('<div class="field"><label for="' + id_ + '">' + label + '</label><div class="input-suffix">'
            '<input class="input" id="' + id_ + '" name="' + name + '" inputmode="decimal" value="' + str(value) + '"><span class="suf">' + suf + '</span></div>' + h + '</div>')

OUT_SLIP = '<div class="tool-out"><div class="result" id="slip" aria-live="polite"></div><p class="rate-status" id="rate-status"></p></div>'
OUT_SLIP_NORATE = '<div class="tool-out"><div class="result" id="slip" aria-live="polite"></div></div>'

TOOLS = []

# ---------------------------------------------------------------- Fiverr
TOOLS.append({
    "slug": "fiverr-fee-calculator", "popular": True, "js": "fiverr", "cat": "fees", "icon": I["receipt"],
    "short": "Fiverr fee calculator", "blurb": "Seller take-home after the 20% fee, or the buyer's checkout total.",
    "title": "Fiverr Fee Calculator 2026 — Seller Earnings & Buyer Fees",
    "desc": "Free Fiverr fee calculator. See what you earn after Fiverr's 20% fee, how the withdrawal fee really works, or what a buyer pays with the 5.5% service fee. Shows PKR, INR and 20+ currencies.",
    "h1": "Fiverr fee calculator",
    "lede": "Enter your order price to see Fiverr's 20% cut and what each order adds to your balance — in dollars and your own currency. Switch to Buyer to see the checkout total.",
    "related": ["fiverr-reverse-fee-calculator", "payoneer-to-pkr-calculator", "upwork-fee-calculator", "fiverr-gig-character-counter"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="role-l">I'm the</span>
<div class="seg" id="role-seg" role="group" aria-labelledby="role-l"><input type="hidden" name="role" value="seller"><button type="button" data-v="seller" aria-pressed="true">Seller</button><button type="button" data-v="buyer" aria-pressed="false">Buyer</button></div></div>
<div class="row">''' + money_field("price", "price", "Order price", 100) + money_field("tip", "tip", "Tip (optional)", 0) + '''</div>
<div id="seller-only">
<div class="field"><label for="wd">Withdrawal fee (Fiverr → Payoneer)</label><select class="input" id="wd" name="wd">
<option value="3">$3 per withdrawal</option>
<option value="custom">A different amount…</option>
<option value="0">I'm not withdrawing yet</option></select>
<p class="hint">Fiverr pays out through Payoneer and charges this once per withdrawal, not per order — so withdrawing several orders together spreads it out. If your withdrawal screen shows a different fee, choose “A different amount”.</p></div>
<div id="wd-custom" hidden>''' + money_field("wdc", "wdc", "Withdrawal fee", 0) + '''</div>
<div class="field"><label for="cur">Also show take-home in</label><select class="input" id="cur" name="cur"></select></div>
</div>
<details class="more"><summary>Fee settings</summary>
<div class="row">''' + pct_field("sfee", "sfee", "Seller fee", 20) + pct_field("bfee", "bfee", "Buyer service fee", 5.5) + '''</div>
<div class="row">''' + money_field("small", "small", "Small order fee", 2.5) + money_field("thr", "thr", "Charged on orders under", 50) + '''</div>
''' + pct_field("conv", "conv", "Currency conversion spread", 2, "Payoneer converts at up to about 2% below the mid-market rate. Banks are often higher.") + '''
</details>
</form>''' + OUT_SLIP,
    "content": '''<h2>How Fiverr fees work in 2026</h2>
<p>Fiverr charges both sides of every order. As a <strong>seller</strong>, you pay a flat <strong>20% service fee</strong> on the full order value — the gig price, any gig extras and tips. There is no lower rate for higher seller levels or bigger orders, so a $1,000 order costs you $200 in fees just like ten $100 orders do.</p>
<p>As a <strong>buyer</strong>, you pay a <strong>5.5% service fee</strong> on top of the gig price, plus a small order fee of $2.50 on orders under $50. Fiverr has adjusted the buyer fee several times, so the fee settings above are editable if your checkout shows something different.</p>
<p>After an order is completed, your earnings stay pending for 14 days (7 days for Top Rated sellers and Fiverr Pro). Then you withdraw. In Pakistan and many other countries Fiverr pays out only through <strong>Payoneer</strong> — even the “bank transfer” option runs through Payoneer — and charges a flat <strong>$3 per withdrawal</strong>. Payoneer then converts your dollars to local currency at a rate up to about 2% below mid-market.</p>
<p>The withdrawal fee is charged <strong>once per withdrawal, not per order</strong>. Ten $100 orders add $800 to your balance; withdraw all of it at once and you pay $3 in total, not $30. That's why the calculator shows what each order earns, and lists the withdrawal fee separately.</p>

<h2>The formula</h2>
<p class="formula">Earnings per order = (order price + tip) × (1 − 20%)</p>
<p class="formula">Money withdrawn = total balance withdrawn − one withdrawal fee</p>
<p>And for buyers:</p>
<p class="formula">Checkout total = gig price × 1.055 + $2.50 (if under $50)</p>

<h2>Fiverr fees at common prices</h2>
<div class="table-wrap"><table>
<thead><tr><th class="num">Gig price</th><th class="num">Fiverr fee (20%)</th><th class="num">Seller earns</th><th class="num">Buyer pays</th></tr></thead>
<tbody>
<tr><td class="num">$5</td><td class="num">$1.00</td><td class="num">$4.00</td><td class="num">$7.78</td></tr>
<tr><td class="num">$10</td><td class="num">$2.00</td><td class="num">$8.00</td><td class="num">$13.05</td></tr>
<tr><td class="num">$25</td><td class="num">$5.00</td><td class="num">$20.00</td><td class="num">$28.88</td></tr>
<tr><td class="num">$50</td><td class="num">$10.00</td><td class="num">$40.00</td><td class="num">$52.75</td></tr>
<tr><td class="num">$100</td><td class="num">$20.00</td><td class="num">$80.00</td><td class="num">$105.50</td></tr>
<tr><td class="num">$250</td><td class="num">$50.00</td><td class="num">$200.00</td><td class="num">$263.75</td></tr>
<tr><td class="num">$500</td><td class="num">$100.00</td><td class="num">$400.00</td><td class="num">$527.50</td></tr>
<tr><td class="num">$1,000</td><td class="num">$200.00</td><td class="num">$800.00</td><td class="num">$1,055.00</td></tr>
</tbody></table></div>
<p class="hint">Bank transfers via Payoneer have a $20 minimum, so small orders are withdrawn together and share one fee.</p>

<h2>How to keep more of each order</h2>
<ul>
<li><strong>Withdraw in batches.</strong> The withdrawal fee is flat. Taking out $400 once costs $3; taking out $50 eight times costs $24.</li>
<li><strong>Price for the fee, not around it.</strong> Adding 20% to your price isn't enough, because the fee is charged on the new, higher price. Use the <a href="/fiverr-reverse-fee-calculator/">reverse fee calculator</a> to find the exact price.</li>
<li><strong>Sell gig extras.</strong> Extras carry the same 20% fee, but they raise the order value without extra marketing, so your fee per hour of work drops.</li>
<li><strong>Watch the conversion.</strong> On a $1,000 withdrawal to PKR, a 2% spread costs about $20. Compare routes with the <a href="/payoneer-to-pkr-calculator/">Payoneer to PKR calculator</a>.</li>
</ul>''',
    "faq": [
        ("How much does Fiverr take from a $5 gig?", "Fiverr keeps $1 (20%) and you earn $4. The buyer pays $7.78: the $5 price, a 5.5% service fee of $0.28 and the $2.50 small order fee."),
        ("Does Fiverr take 20% of tips?", "Yes. Tips are treated as part of your earnings, so the 20% seller fee applies to them too. A $10 tip adds $8 to your balance."),
        ("Is the Fiverr fee lower for Level 2 or Top Rated sellers?", "No. The 20% seller fee is the same for every level. Higher levels mainly get faster clearing (7 days instead of 14), more gig slots and other perks."),
        ("What is the cheapest way to withdraw from Fiverr?", "In Pakistan and many other countries, Fiverr pays out only through Payoneer, at a flat $3 per withdrawal. Because the fee is flat, withdrawing larger amounts less often is cheapest. The bigger cost is usually the currency conversion when Payoneer sends rupees to your bank, so compare that rate too."),
        ("How much does a buyer pay on Fiverr?", "The gig price plus a 5.5% service fee, plus $2.50 on orders under $50. A $100 gig costs $105.50 at checkout."),
        ("How do I see my Fiverr earnings in Pakistani rupees?", "Choose PKR under “Also show take-home in”. The calculator converts your take-home at the live mid-market rate and subtracts the conversion spread you set (2% by default)."),
    ],
})

# ---------------------------------------------------------------- Upwork
TOOLS.append({
    "slug": "upwork-fee-calculator", "js": "upwork", "cat": "fees", "icon": I["brief"],
    "short": "Upwork fee calculator", "blurb": "Variable 0–15% service fee, Connects and withdrawal costs.",
    "title": "Upwork Fee Calculator 2026 — Variable 0–15% Freelancer Fee",
    "desc": "Calculate your Upwork earnings under the 2026 variable service fee (0–15%). Includes Connects, withdrawal fees and conversion to PKR, INR, PHP and more. Free, no sign-up.",
    "h1": "Upwork fee calculator",
    "lede": "Set the service fee Upwork shows on your job (0–15%), add Connects and your withdrawal method, and see exactly what you take home from a fixed-price or hourly contract.",
    "related": ["fiverr-reverse-fee-calculator", "fiverr-fee-calculator", "hourly-rate-calculator", "payoneer-to-pkr-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="mode-l">Contract type</span>
<div class="seg" id="mode-seg" role="group" aria-labelledby="mode-l"><input type="hidden" name="mode" value="fixed"><button type="button" data-v="fixed" aria-pressed="true">Fixed price</button><button type="button" data-v="hourly" aria-pressed="false">Hourly</button></div></div>
<div id="fixed-box">''' + money_field("amount", "amount", "Payment amount", 500) + '''</div>
<div id="hourly-box" class="row" hidden>''' + money_field("rate", "rate", "Hourly rate", 25) + pct_field("hours", "hours", "Hours worked", 20, "", "h") + '''</div>
<div class="field"><label for="fee">Upwork service fee: <output id="fee-out">10%</output></label>
<input type="range" id="fee" name="fee" min="0" max="15" step="0.5" value="10">
<p class="hint">Upwork shows this rate before you submit a proposal, and it stays fixed for the contract.</p></div>
<div class="row"><div class="field"><label for="connects">Connects used</label><input class="input" id="connects" name="connects" inputmode="numeric" value="0"><p class="hint">$0.15 each</p></div>
<div class="field"><label for="wd">Withdrawal method</label><select class="input" id="wd" name="wd">
<option value="0.99">Direct to local bank ($0.99)</option><option value="2">Payoneer ($2)</option><option value="50">Wire transfer ($50)</option><option value="0">No withdrawal yet</option><option value="custom">Other amount…</option></select></div></div>
<div id="wd-custom" hidden>''' + money_field("wdc", "wdc", "Withdrawal fee", 0) + '''</div>
<div class="row"><div class="field"><label for="cur">Also show in</label><select class="input" id="cur" name="cur"></select></div>
''' + pct_field("conv", "conv", "Conversion spread", 2) + '''</div>
</form>''' + OUT_SLIP,
    "content": '''<h2>Upwork's fee structure in 2026</h2>
<p>Since <strong>1 May 2025</strong>, Upwork no longer uses the old sliding scale (20% on the first $500 with a client, then 10%, then 5%). Instead, every contract has a <strong>variable freelancer service fee between 0% and 15%</strong>. Upwork sets the rate using factors such as the job category, demand and your history with that client.</p>
<p>The important part: Upwork <strong>shows the fee before you submit a proposal</strong>, and that rate stays locked for the life of the contract. So you always know the number — enter it in the slider above. Most freelancers report fees around 10%, with commodity categories closer to 15%.</p>
<p>Your real cost is more than the service fee. <strong>Connects</strong> (used to send proposals) cost $0.15 each, and each withdrawal has a fee that depends on the method. Clients pay their own separate marketplace fee, which doesn't come out of your earnings.</p>

<h2>The formula</h2>
<p class="formula">Earnings = payment × (1 − service fee %) − Connects × $0.15</p>
<p>The withdrawal fee is separate: it's charged once each time you withdraw, whatever the amount, not on every payment.</p>

<h2>Upwork fees on a $500 contract</h2>
<div class="table-wrap"><table>
<thead><tr><th>Service fee</th><th class="num">Upwork keeps</th><th class="num">You earn</th></tr></thead>
<tbody>
<tr><td>0% (some direct contracts)</td><td class="num">$0.00</td><td class="num">$500.00</td></tr>
<tr><td>5%</td><td class="num">$25.00</td><td class="num">$475.00</td></tr>
<tr><td>10%</td><td class="num">$50.00</td><td class="num">$450.00</td></tr>
<tr><td>12.5%</td><td class="num">$62.50</td><td class="num">$437.50</td></tr>
<tr><td>15%</td><td class="num">$75.00</td><td class="num">$425.00</td></tr>
</tbody></table></div>

<h2>Upwork vs Fiverr on the same job</h2>
<p>On a $500 job, Fiverr's flat 20% leaves you $400, while Upwork at 10% leaves $450. But Upwork's Connects add up if you send many proposals: 16 Connects per proposal across 10 proposals is $24 for one win. Use the <a href="/fiverr-fee-calculator/">Fiverr fee calculator</a> side by side to compare your real numbers.</p>

<h2>Ways to lower your Upwork costs</h2>
<ul>
<li><strong>Check the fee before you bid.</strong> If two similar jobs show 8% and 15%, the first pays you $35 more on every $500.</li>
<li><strong>Raise your rate to absorb the fee.</strong> The <a href="/fiverr-reverse-fee-calculator/">reverse fee calculator</a> tells you what to quote for the amount you want to keep.</li>
<li><strong>Be selective with Connects.</strong> Proposals sent within the first hour of a job posting tend to perform better than late ones.</li>
<li><strong>Withdraw less often.</strong> Flat withdrawal fees hurt most on small amounts.</li>
</ul>''',
    "faq": [
        ("What is Upwork's freelancer fee in 2026?", "A variable service fee from 0% to 15% per contract, introduced on 1 May 2025. Upwork shows the exact rate before you send a proposal, and it doesn't change during the contract."),
        ("Why is my Upwork fee different on each job?", "Upwork prices the fee per contract based on things like the category, market demand and your relationship with the client. Two jobs on the same day can show different rates."),
        ("Does the Upwork fee apply to bonuses?", "Yes. The service fee applies to all payments you receive from the client on that contract, including bonuses."),
        ("How much do Upwork Connects cost?", "Connects cost $0.15 each. Proposals usually need several Connects, and boosted proposals need more, so track them as a business expense."),
        ("Is the old 20% / 10% / 5% Upwork fee still used?", "No. The tiered fee based on lifetime billings with a client was replaced by the variable 0–15% fee in May 2025."),
    ],
})

# ---------------------------------------------------------------- Reverse
TOOLS.append({
    "slug": "fiverr-reverse-fee-calculator", "js": "reverse", "cat": "fees", "icon": I["target"],
    "short": "Reverse fee calculator", "blurb": "How much to charge so you keep the amount you want.",
    "title": "Reverse Fee Calculator — How Much to Charge on Fiverr & Upwork",
    "desc": "Work backwards from the money you want in hand. Find the exact price to charge on Fiverr, Upwork, Freelancer.com or PeoplePerHour after platform fees and currency conversion.",
    "h1": "How much should I charge to receive my amount?",
    "lede": "Tell us what you want to receive — in dollars or rupees — and pick your platform. You'll get the exact price to list, with the platform fee built in.",
    "related": ["fiverr-fee-calculator", "upwork-fee-calculator", "hourly-rate-calculator", "project-quote-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="row">''' + money_field("want", "want", "I want to receive", 100, "", "") + '''
<div class="field"><label for="wcur">Currency</label><select class="input" id="wcur" name="wcur"></select></div></div>
<div class="field"><label for="platform">Platform</label><select class="input" id="platform" name="platform">
<option value="fiverr">Fiverr (20%)</option><option value="upwork">Upwork (variable, 10% typical)</option><option value="freelancer">Freelancer.com (10%, $5 minimum)</option><option value="pph">PeoplePerHour (20% typical)</option><option value="custom">Other platform</option></select></div>
<div class="row">''' + pct_field("pfee", "pfee", "Platform fee", 20) + money_field("wd", "wd", "Withdrawal fee to include", 0, "Usually leave at 0. It's charged once per withdrawal, not per order — only add it if you'll withdraw this one order on its own.") + '''</div>
<div id="conv-box" hidden>''' + pct_field("conv", "conv", "Conversion spread", 2, "The gap between the mid-market rate and the rate your payout provider gives you.") + '''</div>
</form>''' + OUT_SLIP,
    "content": '''<h2>Why adding 20% doesn't work</h2>
<p>Most freelancers price like this: “I want $100, Fiverr takes 20%, so I'll charge $120.” But Fiverr takes 20% of <em>$120</em>, which is $24 — leaving you $96, not $100. Platform fees are a percentage of the <strong>final</strong> price, so you need to divide, not add.</p>
<p class="formula">Price to charge = amount you want ÷ (1 − platform fee %)</p>
<p>For $100 on Fiverr: 100 ÷ 0.80 = <strong>$125</strong>. The withdrawal fee isn't part of this, because it's charged once per withdrawal, not per order — spread across many orders it's only cents each.</p>

<h2>Price needed to keep $100</h2>
<div class="table-wrap"><table>
<thead><tr><th>Platform</th><th class="num">Fee</th><th class="num">Charge</th></tr></thead>
<tbody>
<tr><td>Fiverr</td><td class="num">20%</td><td class="num">$125.00</td></tr>
<tr><td>PeoplePerHour</td><td class="num">20%</td><td class="num">$125.00</td></tr>
<tr><td>Upwork (15%)</td><td class="num">15%</td><td class="num">$117.65</td></tr>
<tr><td>Upwork (10%)</td><td class="num">10%</td><td class="num">$111.11</td></tr>
<tr><td>Freelancer.com</td><td class="num">10%</td><td class="num">$111.11</td></tr>
</tbody></table></div>

<h2>Starting from rupees or another currency</h2>
<p>If your goal is a local amount — say Rs 50,000 in your bank — choose your currency. The calculator converts at today's mid-market rate, then adds the conversion spread your payout provider charges (about 2% for Payoneer), so the price you list really does land as Rs 50,000.</p>

<h2>Tips for pricing with fees</h2>
<ul>
<li>Round <strong>up</strong> to the platform's price step, never down.</li>
<li>Re-check your price when a platform changes its fee. Your margin is the first thing to disappear.</li>
<li>For bigger projects, build the quote line by line with the <a href="/project-quote-calculator/">project quote calculator</a>.</li>
</ul>''',
    "faq": [
        ("How much should I charge on Fiverr to get $100?", "$125. Fiverr keeps 20% ($25) and $100 reaches your balance. The $3 withdrawal fee is charged once per withdrawal, not per order, so it doesn't need to be priced into each gig."),
        ("What's the formula to include platform fees in my price?", "Divide the amount you want by (1 − the fee rate). For a 20% fee, divide by 0.8. Adding 20% instead leaves you short, because the fee is taken from the higher price."),
        ("How much should I charge on Upwork to receive $500?", "At a 10% service fee, $555.56. At 15%, $588.24. Use the exact fee Upwork shows on the job."),
        ("Can I calculate the price for an amount in PKR?", "Yes. Set the currency to PKR and enter the rupee amount you want. The calculator converts it and accounts for the conversion spread."),
    ],
})

# ---------------------------------------------------------------- Payoneer
TOOLS.append({
    "slug": "payoneer-to-pkr-calculator", "popular": True, "js": "payoneer", "cat": "payments", "icon": I["bank"],
    "short": "Payoneer to PKR calculator", "blurb": "What your Payoneer dollars become in your bank.",
    "title": "Payoneer to PKR Calculator — Live Rate, Fees & Amount Received",
    "desc": "Convert Payoneer USD, EUR or GBP to PKR with live rates. Includes Payoneer's conversion fee, receiving fees and bank withholding tax. Also works for INR, BDT, PHP and NGN.",
    "h1": "Payoneer to PKR calculator",
    "lede": "See how many rupees reach your bank when you withdraw from Payoneer. Uses the live mid-market rate and subtracts Payoneer's conversion spread — or type in the exact rate Payoneer shows you.",
    "related": ["freelancer-currency-converter", "fiverr-fee-calculator", "upwork-fee-calculator", "fiverr-reverse-fee-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="row">''' + money_field("amount", "amount", "Amount to withdraw", 500, "", "") + '''
<div class="field"><label for="from">From</label><select class="input" id="from" name="from"></select></div></div>
<div class="field"><label for="to">To your bank in</label><select class="input" id="to" name="to"></select></div>
<div class="field"><label for="src">Where the money came from</label><select class="input" id="src" name="src">
<option value="0">Fiverr, Upwork or another marketplace</option><option value="1">Client paid by bank transfer (1% fee)</option><option value="3">Client paid by card (3% fee)</option></select></div>
<div class="row">''' + pct_field("conv", "conv", "Payoneer conversion fee", 2, "Up to 2% above mid-market") + '''
<div class="field"><label for="rate">Exchange rate</label><input class="input" id="rate" name="rate" inputmode="decimal" value=""><p class="hint"><button type="button" class="btn btn-ghost btn-small" data-reset-rate style="padding:6px 12px">Use live rate</button></p></div></div>
<details class="more"><summary>Extra deductions</summary>
<div class="row">''' + money_field("flat", "flat", "Flat withdrawal fee", 0, "In the source currency") + pct_field("wht", "wht", "Bank withholding tax", 0, "Only if your bank deducts it") + '''</div>
</details>
</form>''' + OUT_SLIP,
    "content": '''<h2>How Payoneer converts your dollars to rupees</h2>
<p>When you withdraw USD, EUR or GBP from Payoneer to a bank account in Pakistan, Payoneer converts it to PKR. It doesn't list this as a separate line — instead, the rate you get is <strong>up to about 2% below the mid-market rate</strong> (the rate you see on Google). That gap is the conversion fee.</p>
<p>For example, if the mid-market rate is Rs 277 per dollar, a 2% spread gives you about Rs 271.46. On a $1,000 withdrawal that's roughly Rs 5,540 you never see itemised.</p>
<p class="formula">Rupees received = amount × mid-market rate × (1 − conversion fee %) − any bank tax</p>

<h2>Payoneer to PKR at Rs 277 and a 2% spread</h2>
<div class="table-wrap"><table>
<thead><tr><th class="num">Payoneer balance</th><th class="num">Mid-market value</th><th class="num">You receive</th><th class="num">Spread cost</th></tr></thead>
<tbody>
<tr><td class="num">$100</td><td class="num">Rs 27,700</td><td class="num">Rs 27,146</td><td class="num">Rs 554</td></tr>
<tr><td class="num">$250</td><td class="num">Rs 69,250</td><td class="num">Rs 67,865</td><td class="num">Rs 1,385</td></tr>
<tr><td class="num">$500</td><td class="num">Rs 1,38,500</td><td class="num">Rs 1,35,730</td><td class="num">Rs 2,770</td></tr>
<tr><td class="num">$1,000</td><td class="num">Rs 2,77,000</td><td class="num">Rs 2,71,460</td><td class="num">Rs 5,540</td></tr>
<tr><td class="num">$2,000</td><td class="num">Rs 5,54,000</td><td class="num">Rs 5,42,920</td><td class="num">Rs 11,080</td></tr>
</tbody></table></div>
<p class="hint">Example rate only. The calculator above uses today's live rate.</p>

<h2>Other Payoneer fees to know</h2>
<ul>
<li><strong>Receiving fees.</strong> Payments from clients via a Payoneer payment request typically cost 1% by bank transfer and 3% by card. Marketplace payouts from Fiverr or Upwork are charged by the marketplace instead (see the <a href="/fiverr-fee-calculator/">Fiverr</a> and <a href="/upwork-fee-calculator/">Upwork</a> calculators).</li>
<li><strong>Annual account fee.</strong> Since February 2026, Payoneer charges $29.95 if your account receives less than $6,000 in 12 months (in the countries where this rule applies). Your account's Fees page shows whether it applies to you.</li>
<li><strong>2025 changes for Pakistan.</strong> Payoneer revised several fees for Pakistani accounts in 2025, including charges on Payoneer-to-Payoneer transfers and withdrawals to foreign-currency accounts. Check the Fees page inside your account for your exact rates.</li>
</ul>

<h2>Getting the exact number</h2>
<p>Before you confirm a withdrawal, Payoneer shows the exact rate. Type that into “Exchange rate” and set the conversion fee to 0% to get a precise rupee figure. Keep your <strong>Proof of Remittance Certificate (PRC)</strong> from the bank — it documents your income as an IT export for tax purposes.</p>''',
    "faq": [
        ("What rate does Payoneer use for PKR?", "Payoneer converts at its own rate, which is up to about 2% below the mid-market rate. The calculator applies that spread to today's live rate. For an exact figure, enter the rate Payoneer shows on the withdrawal screen."),
        ("How much is $100 from Payoneer in Pakistani rupees?", "At a mid-market rate of Rs 277 and a 2% spread, about Rs 27,146. Rates move daily, so use the calculator above for today's figure."),
        ("Can I avoid Payoneer's conversion fee?", "If you hold a USD account at a Pakistani bank, you can withdraw in dollars for a flat fee instead of converting. Your bank then converts when you need rupees, at its own rate — so compare both before choosing."),
        ("Does my bank deduct tax on Payoneer withdrawals?", "Some banks deduct withholding tax on freelance export remittances. The rate depends on your filer status and registration. If your bank deducts it, enter the percentage under Extra deductions."),
        ("Does this work for India, Bangladesh or the Philippines?", "Yes. Change “To your bank in” to INR, BDT, PHP, NGN or another currency and the calculator uses the live rate for it."),
    ],
})

# ---------------------------------------------------------------- Currency
TOOLS.append({
    "slug": "freelancer-currency-converter", "js": "currency", "cat": "payments", "icon": I["fx"],
    "short": "Freelancer currency converter", "blurb": "Live USD, GBP and EUR rates to PKR, INR, PHP and more.",
    "title": "Freelancer Currency Converter — USD to PKR, INR, PHP, BDT (Live)",
    "desc": "Convert freelance earnings between USD, GBP, EUR and 20+ currencies including PKR, INR, PHP, BDT and NGN. Live mid-market rates, optional provider spread, all currencies at once.",
    "h1": "Currency converter for freelancers",
    "lede": "Convert a payment into every currency freelancers get paid in, at once. Add your provider's spread to see what you'd actually receive, not just the headline rate.",
    "related": ["payoneer-to-pkr-calculator", "fiverr-fee-calculator", "invoice-generator", "hourly-rate-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
''' + money_field("amount", "amount", "Amount", 100, "", "") + '''
<div class="row" style="grid-template-columns:1fr auto 1fr;align-items:end">
<div class="field"><label for="from">From</label><select class="input" id="from" name="from"></select></div>
<div class="field"><button type="button" class="icon-btn" id="swap" aria-label="Swap currencies" style="height:50px;width:50px">''' + I["swap"] + '''</button></div>
<div class="field"><label for="to">To</label><select class="input" id="to" name="to"></select></div></div>
''' + pct_field("spread", "spread", "Provider spread (optional)", 0, "Set 2% for Payoneer, 3–5% for a typical bank. Leave at 0 for the pure mid-market rate.") + '''
<div class="result" style="margin-top:4px"><div id="main-result" aria-live="polite"></div></div>
<p class="rate-status" id="rate-status"></p>
</form>
<div class="tool-out"><div class="result"><div class="res-head"><span class="res-title" id="list-title">In other currencies</span><span class="pill gold">Live</span></div><ul class="conv-list" id="conv-list"></ul></div></div>''',
    "content": '''<h2>What the mid-market rate means</h2>
<p>The <strong>mid-market rate</strong> is the midpoint between what banks pay to buy a currency and what they charge to sell it. It's the rate you see on Google and the one this converter shows by default. It's also a rate almost nobody gives you: payout providers and banks add a margin, called the <strong>spread</strong>.</p>
<p>Set the spread field to your provider's margin to see a realistic figure. As a rough guide, Payoneer's conversion fee is up to about 2%, many banks charge 3–5% on incoming foreign transfers, and specialist transfer services are often under 1%.</p>
<p class="formula">Amount received = amount × mid-market rate × (1 − spread %)</p>

<h2>Why freelancers need more than one currency</h2>
<p>A designer in Lahore might quote a UK client in pounds, get paid through Fiverr in dollars and pay rent in rupees. Seeing all three at once helps you set prices clients understand, spot a bad rate before you accept it, and invoice in the currency that costs least to convert.</p>

<h2>Tips for getting a better rate</h2>
<ul>
<li><strong>Invoice in the client's currency</strong> only if your provider converts it cheaply. Otherwise, invoice in USD.</li>
<li><strong>Don't convert in small amounts</strong> if each conversion has a minimum fee.</li>
<li><strong>Check the rate on the day.</strong> Currencies like PKR, NGN and EGP can move several percent in a month.</li>
<li>See the full Payoneer picture, including receiving fees, with the <a href="/payoneer-to-pkr-calculator/">Payoneer to PKR calculator</a>.</li>
</ul>''',
    "faq": [
        ("Where do these exchange rates come from?", "From a free public rates feed that updates daily. Rates are mid-market. If the feed can't be reached, the converter falls back to an approximate rate and tells you so."),
        ("Why is the rate I get lower than this?", "Banks and payout providers add a spread on top of the mid-market rate. Enter that spread in the optional field to see what you'd actually receive."),
        ("Which currencies are supported?", "USD, EUR, GBP, PKR, INR, PHP, BDT, NGN, EGP, KES, LKR, NPR, IDR, VND, AED, SAR, CAD, AUD, TRY, BRL, MXN, UAH, MYR and ZAR."),
        ("Is the converter accurate enough for invoices?", "It's accurate for estimates and quotes. For a payment you're about to receive, use the rate your provider shows at the moment of conversion."),
    ],
})

# ---------------------------------------------------------------- Hourly
TOOLS.append({
    "slug": "hourly-rate-calculator", "js": "hourly", "cat": "pricing", "icon": I["clock"],
    "short": "Hourly rate calculator", "blurb": "Your minimum rate from income goal, costs and taxes.",
    "title": "Freelance Hourly Rate Calculator — Find Your Minimum Rate",
    "desc": "Calculate the hourly rate you need as a freelancer from your income goal, business costs, tax, billable hours and platform fees. Works in USD, PKR, INR, GBP and 20+ currencies.",
    "h1": "Freelance hourly rate calculator",
    "lede": "Start from what you want to earn each month, add your costs, tax and platform fees, and be honest about how many hours you can actually bill. The result is the lowest rate that makes it work.",
    "related": ["project-quote-calculator", "fiverr-reverse-fee-calculator", "profit-margin-calculator", "upwork-fee-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
<div class="row">''' + money_field("income", "income", "Take-home goal per month", 1500) + money_field("expenses", "expenses", "Business costs per month", 150, "Software, internet, equipment, Connects") + '''</div>
<div class="row">''' + pct_field("tax", "tax", "Income tax", 10) + pct_field("pfee", "pfee", "Platform fee", 20, "0 if clients pay you directly") + '''</div>
<div class="row-3">''' + pct_field("hours", "hours", "Work hours / week", 40, "", "h") + pct_field("off", "off", "Weeks off / year", 4, "", "wk") + pct_field("billable", "billable", "Billable share", 70) + '''</div>
<p class="hint">Billable share is the part of your working time a client pays for. Messages, revisions you don't charge for and finding work aren't billable — 60–75% is typical.</p>
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>How the calculator works</h2>
<p>Most freelancers set their rate by looking at what others charge. The problem is that their costs, taxes and workloads aren't yours. This calculator works from the bottom up:</p>
<ol>
<li>It turns your monthly take-home goal into a yearly figure and grosses it up for income tax.</li>
<li>It adds your yearly business costs.</li>
<li>It grosses that up again for the platform's fee, because Fiverr or Upwork take their cut before you see anything.</li>
<li>It divides by the hours you can realistically bill in a year.</li>
</ol>
<p class="formula">Hourly rate = ((goal ÷ (1 − tax) + costs) ÷ (1 − platform fee)) ÷ billable hours per year</p>

<h2>A worked example</h2>
<p>You want $1,500 a month in hand, spend $150 a month on tools, pay about 10% tax and sell on Fiverr (20% fee). You work 40 hours a week, take 4 weeks off, and about 70% of your time is billable.</p>
<div class="table-wrap"><table><tbody>
<tr><td>Take-home goal per year</td><td class="num">$18,000</td></tr>
<tr><td>Plus tax (10%)</td><td class="num">$20,000</td></tr>
<tr><td>Plus business costs</td><td class="num">$21,800</td></tr>
<tr><td>Plus platform fee (20%)</td><td class="num">$27,250</td></tr>
<tr><td>Billable hours (40 × 70% × 48 weeks)</td><td class="num">1,344 h</td></tr>
<tr><th>Minimum hourly rate</th><th class="num">$20.28</th></tr>
</tbody></table></div>

<h2>Common mistakes</h2>
<ul>
<li><strong>Assuming 100% billable time.</strong> If you bill 40 hours but only 28 are paid, your real rate is 30% lower than you think.</li>
<li><strong>Forgetting the platform fee.</strong> A $20 rate on Fiverr is $16 to you.</li>
<li><strong>Treating the minimum as the price.</strong> This number covers your life. Your price should add a margin for skill, speed and demand.</li>
</ul>
<p>Turn the rate into a client-ready number with the <a href="/project-quote-calculator/">project quote calculator</a>.</p>''',
    "faq": [
        ("What is a good hourly rate for a beginner freelancer?", "Start from your costs, not from competitors. The calculator gives your break-even rate; beginners often price close to it and raise rates as reviews come in."),
        ("How many billable hours does a freelancer have per year?", "Usually 1,000 to 1,500. Forty hours a week for 48 weeks is 1,920 hours, but only 60–75% of that is typically paid client work."),
        ("Should I include platform fees in my hourly rate?", "Yes. If you sell through Fiverr or Upwork, your listed rate must cover their fee or your real hourly income will be lower than planned."),
        ("Can I calculate my rate in Pakistani rupees?", "Yes. Choose PKR as the currency and enter your monthly goal and costs in rupees. The result is your rupee rate; convert it to USD for international clients with the currency converter."),
    ],
})

# ---------------------------------------------------------------- Quote
TOOLS.append({
    "slug": "project-quote-calculator", "js": "quote", "cat": "pricing", "icon": I["list"],
    "short": "Project quote calculator", "blurb": "Line-by-line quote with buffer, rush fee and deposit.",
    "title": "Freelance Project Quote Calculator — Price a Project Line by Line",
    "desc": "Build a freelance project quote from tasks and hours. Add a revision buffer, rush fee, discount and platform fees, then see the deposit and your real hourly rate. Free and private.",
    "h1": "Project quote calculator",
    "lede": "List the tasks, estimate the hours and set your rate. Add a buffer for revisions, a rush fee if the deadline is tight, and cover the platform fee — then quote with confidence.",
    "related": ["hourly-rate-calculator", "invoice-generator", "fiverr-reverse-fee-calculator", "profit-margin-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
<div class="field"><span class="label">Tasks</span>
<div class="item-row item-head" aria-hidden="true"><span>Task</span><span>Hours</span><span>Rate / h</span><span></span></div>
<div class="items" id="items"></div>
<div><button type="button" class="btn btn-ghost btn-small" id="add-item">Add task</button></div></div>
<div class="row">''' + pct_field("buffer", "buffer", "Revision buffer", 15) + pct_field("rush", "rush", "Rush fee", 0) + '''</div>
<div class="row">''' + pct_field("discount", "discount", "Discount", 0) + pct_field("deposit", "deposit", "Upfront deposit", 50) + '''</div>
<div class="row" style="align-items:center">''' + pct_field("pfee", "pfee", "Platform fee", 20) + '''
<label class="check"><input type="checkbox" name="gross" id="gross" checked> Add the platform fee to the quote</label></div>
<div class="res-actions" style="margin-top:4px"><button type="button" class="btn btn-ghost btn-small" id="reset">Start over</button></div>
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>How to quote a freelance project</h2>
<p>A good quote is built from the work, not from a number that “feels right”. Break the project into tasks, estimate hours for each, and multiply by your rate. Then adjust for the things that always happen:</p>
<ul>
<li><strong>Revision buffer.</strong> Clients ask for changes. A 10–20% buffer pays for them without arguing over every round.</li>
<li><strong>Rush fee.</strong> If the deadline means late nights or moving other clients, charge for it — 25–50% is common.</li>
<li><strong>Platform fee.</strong> On Fiverr or Upwork, gross up the quote so the fee comes out of the client's price, not your pocket.</li>
<li><strong>Deposit.</strong> Asking for 30–50% upfront on direct clients protects you if a project stalls.</li>
</ul>
<p class="formula">Quote = (Σ hours × rate) × (1 + buffer) × (1 + rush) × (1 − discount) ÷ (1 − platform fee)</p>

<h2>Example: a five-page website</h2>
<div class="table-wrap"><table>
<thead><tr><th>Line</th><th class="num">Amount</th></tr></thead>
<tbody>
<tr><td>Discovery &amp; planning · 4 h × $30</td><td class="num">$120</td></tr>
<tr><td>Design · 12 h × $30</td><td class="num">$360</td></tr>
<tr><td>Development · 24 h × $30</td><td class="num">$720</td></tr>
<tr><td>Revision buffer (15%)</td><td class="num">$180</td></tr>
<tr><td>Platform fee cover (20%)</td><td class="num">$345</td></tr>
<tr><th>Quote</th><th class="num">$1,725</th></tr>
</tbody></table></div>
<p>You keep $1,380 after Fiverr's fee — exactly the work plus buffer you planned.</p>

<h2>After the client says yes</h2>
<p>Your quote is saved in this browser, so you can come back and adjust it. When the work is done, turn it into an invoice with the <a href="/invoice-generator/">free invoice generator</a>.</p>''',
    "faq": [
        ("How much buffer should I add to a freelance quote?", "10–20% covers normal revisions and small surprises. Use more for clients who haven't given a clear brief."),
        ("Should I show the client the hourly breakdown?", "Usually no. Clients compare outcomes, not hours. Use the breakdown to set your price, and present the total with a clear scope."),
        ("How do I include Fiverr or Upwork fees in my quote?", "Tick “Add the platform fee to the quote”. The calculator divides by (1 − fee) so that after the platform takes its share, you keep your full amount."),
        ("Is my quote saved?", "Yes, in your browser only. Nothing is sent to a server. Use “Start over” to clear it."),
    ],
})

# ---------------------------------------------------------------- Margin
TOOLS.append({
    "slug": "profit-margin-calculator", "js": "margin", "cat": "pricing", "icon": I["pie"],
    "short": "Profit margin calculator", "blurb": "Margin, markup and the price for a target margin.",
    "title": "Profit Margin Calculator — Margin, Markup & Price (with Fees)",
    "desc": "Free profit margin calculator. Find your margin and markup from cost and price, or the price you need for a target margin. Includes platform fees for Fiverr and Upwork sellers.",
    "h1": "Profit margin calculator",
    "lede": "Check the margin on a price you're considering, or work out the price that hits the margin you want. Platform fees are included, so the answer matches what you actually keep.",
    "related": ["project-quote-calculator", "hourly-rate-calculator", "fiverr-reverse-fee-calculator", "fiverr-fee-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><span class="label" id="mode-l">I want to</span>
<div class="seg" id="mode-seg" role="group" aria-labelledby="mode-l"><input type="hidden" name="mode" value="margin"><button type="button" data-v="margin" aria-pressed="true">Check my margin</button><button type="button" data-v="price" aria-pressed="false">Find my price</button></div></div>
<div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
''' + money_field("cost", "cost", "Your cost", 60, "Outsourcing, assets, software and your own time at cost", "") + '''
<div id="price-box">''' + money_field("price", "price", "Selling price", 100, "", "") + '''</div>
<div id="target-box" hidden>''' + pct_field("target", "target", "Target profit margin", 40) + '''</div>
''' + pct_field("pfee", "pfee", "Platform fee", 0, "Enter 20 for Fiverr, or the fee Upwork shows on the job") + '''
</form>''' + OUT_SLIP_NORATE,
    "content": '''<h2>Margin vs markup</h2>
<p>They sound alike but measure different things, and mixing them up is one of the most common pricing mistakes.</p>
<ul>
<li><strong>Profit margin</strong> is profit as a share of the <em>price</em>: how much of each sale you keep.</li>
<li><strong>Markup</strong> is profit as a share of the <em>cost</em>: how much you add on top.</li>
</ul>
<p class="formula">Margin = (price − cost − fees) ÷ price &nbsp;·&nbsp; Markup = (price − cost) ÷ cost</p>
<p>If something costs $60 and you sell it for $100, the markup is 66.7% but the margin is 40%.</p>

<h2>Margin and markup equivalents</h2>
<div class="table-wrap"><table>
<thead><tr><th class="num">Margin</th><th class="num">Markup needed</th></tr></thead>
<tbody>
<tr><td class="num">20%</td><td class="num">25%</td></tr>
<tr><td class="num">25%</td><td class="num">33.3%</td></tr>
<tr><td class="num">33.3%</td><td class="num">50%</td></tr>
<tr><td class="num">40%</td><td class="num">66.7%</td></tr>
<tr><td class="num">50%</td><td class="num">100%</td></tr>
<tr><td class="num">60%</td><td class="num">150%</td></tr>
</tbody></table></div>

<h2>Finding a price with fees included</h2>
<p>When a platform takes a cut, the price has to cover the cost, the fee and your margin. With cost C, platform fee F and target margin M:</p>
<p class="formula">Price = C ÷ (1 − F − M)</p>
<p>A $60 cost with Fiverr's 20% fee and a 40% target margin needs a $150 price. Fee plus margin must stay under 100%, or no price works.</p>

<h2>Where freelancers use this</h2>
<ul>
<li>Reselling templates, themes or stock assets inside a service.</li>
<li>Agency work where you outsource part of a project.</li>
<li>Checking whether a discount still leaves you a healthy margin.</li>
</ul>''',
    "faq": [
        ("What's the difference between margin and markup?", "Margin is profit divided by price; markup is profit divided by cost. A 50% markup equals a 33.3% margin."),
        ("What is a good profit margin for freelancers?", "Service businesses often aim for 30–50% margins on outsourced or resold work. For your own time, use the hourly rate calculator instead."),
        ("How do platform fees affect my margin?", "They come out of the price before you profit. A 20% Fiverr fee on a $100 sale leaves $80 to cover your cost and profit."),
        ("Why does the calculator say no price works?", "If the platform fee plus your target margin is 100% or more, every extra dollar of price goes to the fee and margin, leaving nothing for cost. Lower the target margin."),
    ],
})

# ---------------------------------------------------------------- Invoice
TOOLS.append({
    "slug": "invoice-generator", "popular": True, "js": "invoice", "cat": "documents", "icon": I["doc"], "appcat": "BusinessApplication",
    "short": "Invoice generator", "blurb": "Professional PDF invoices in any currency, free.",
    "title": "Free Invoice Generator for Freelancers — Download PDF, No Sign-up",
    "desc": "Create a professional invoice in a minute. Add your logo, items, tax and discount in USD, PKR, GBP, EUR or any currency, then download a PDF. Free, no sign-up, nothing uploaded.",
    "h1": "Free invoice generator",
    "lede": "Fill in your details and items, and the invoice updates as you type. Download a clean PDF or print it. Your details stay in this browser, ready for your next invoice.",
    "related": ["project-quote-calculator", "freelancer-currency-converter", "hourly-rate-calculator", "payoneer-to-pkr-calculator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off" data-doc="invoice">
<div class="row-3"><div class="field"><label for="num">Invoice number</label><input class="input" id="num" name="num"></div>
<div class="field"><label for="issued">Issued</label><input class="input" type="date" id="issued" name="issued"></div>
<div class="field"><label for="due">Due</label><input class="input" type="date" id="due" name="due"></div></div>
<div class="row"><div class="field"><label for="from">From (you)</label><textarea class="input" id="from" name="from" rows="3"></textarea></div>
<div class="field"><label for="to">Bill to</label><textarea class="input" id="to" name="to" rows="3"></textarea></div></div>
<div class="row"><div class="field"><label for="cur">Currency</label><select class="input" id="cur" name="cur"></select></div>
<div class="field"><label for="logo">Logo (optional)</label><input class="input" type="file" id="logo" accept="image/*"><button type="button" class="btn btn-ghost btn-small" id="logo-clear" hidden>Remove logo</button></div></div>
<div class="field"><span class="label">Items</span>
<div class="item-row item-head" aria-hidden="true"><span>Description</span><span>Qty</span><span>Price</span><span></span></div>
<div class="items" id="items"></div>
<div><button type="button" class="btn btn-ghost btn-small" id="add-item">Add item</button></div></div>
<div class="row">''' + pct_field("taxp", "taxp", "Tax", 0) + pct_field("discp", "discp", "Discount", 0) + '''</div>
<div class="field"><label for="pay">Payment details</label><textarea class="input" id="pay" name="pay" rows="3"></textarea><p class="hint">Payoneer email, bank title and IBAN, or a payment link.</p></div>
<div class="field"><label for="notes">Notes</label><textarea class="input" id="notes" name="notes" rows="2"></textarea></div>
</form>
<div class="tool-out">
<div class="doc-paper" id="doc-print"></div>
<div class="res-actions">
<button type="button" class="btn" id="pdf-inv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>Download PDF</button>
<button type="button" class="btn btn-ghost" id="print-inv">Print</button>
<button type="button" class="btn btn-ghost" id="new-inv">New invoice</button></div>
<p class="hint" style="margin-top:12px">The PDF uses standard fonts. For text in Urdu, Hindi or other scripts, use Print and choose “Save as PDF”.</p>
</div>''',
    "content": '''<h2>How to make an invoice</h2>
<ol>
<li><strong>Number it.</strong> Use a sequence like INV-0001, INV-0002. “New invoice” bumps the number for you and keeps your details.</li>
<li><strong>Add both parties.</strong> Your name and contact details, and the client's name, company and email.</li>
<li><strong>Set the dates.</strong> Issue date and a due date — 7 or 14 days is standard for freelance work.</li>
<li><strong>List the work.</strong> One line per deliverable, with quantity and price. Clear descriptions get paid faster.</li>
<li><strong>Add tax or discount</strong> if they apply, and say how to pay you.</li>
<li><strong>Download the PDF</strong> and send it with a short message.</li>
</ol>

<h2>What a freelance invoice should include</h2>
<ul>
<li>The word “Invoice” and a unique invoice number</li>
<li>Your name or business name, and contact details</li>
<li>The client's name and company</li>
<li>Issue date and payment due date</li>
<li>Itemised services with quantities and prices</li>
<li>Subtotal, any tax or discount, and the total due, with the currency</li>
<li>How to pay: Payoneer, bank details or a payment link</li>
</ul>

<h2>Do I need an invoice if I work on Fiverr or Upwork?</h2>
<p>Not for the platform — Fiverr and Upwork generate their own records. But you need invoices for <strong>direct clients</strong>, for clients who ask for one for their accounts, and for your own tax records. If you're in Pakistan and receive payments through Payoneer or a bank, matching invoices alongside your bank's Proof of Remittance Certificate make it easy to show your income is IT export.</p>

<h2>Private by default</h2>
<p>Everything you type stays in your browser's storage on this device. Nothing is uploaded, and the PDF is created on your device. Clearing your browser data removes it.</p>''',
    "faq": [
        ("Is this invoice generator really free?", "Yes. There's no sign-up, watermark or limit. Make as many invoices as you need."),
        ("Can I add my logo?", "Yes. Choose an image under Logo. It's resized in your browser and placed at the top right of the invoice."),
        ("Which currencies can I invoice in?", "Any of 24 currencies, including USD, GBP, EUR, PKR, INR, PHP, BDT, NGN, AED and SAR."),
        ("Where is my invoice saved?", "In your browser's local storage on this device only. If you switch devices or clear browser data, start a new one."),
        ("Why does the PDF show a currency code instead of a symbol?", "Standard PDF fonts don't include symbols like ₨ or ₹, so the PDF uses codes such as PKR and INR, which are clearer for international clients anyway."),
    ],
})

# ---------------------------------------------------------------- Gig counter
TOOLS.append({
    "slug": "fiverr-gig-character-counter", "js": "gigcounter", "cat": "gig", "icon": I["text"], "appcat": "UtilitiesApplication",
    "short": "Gig title & description counter", "blurb": "Fiverr limits, keyword checks and rule warnings.",
    "title": "Fiverr Gig Title & Description Character Counter (80 / 1200)",
    "desc": "Check your Fiverr gig title (80 characters), description (1,200), search tags and profile description (600) against the limits. Keyword placement checks and contact-info warnings.",
    "h1": "Fiverr gig title & description counter",
    "lede": "Write your gig here and see the character count against Fiverr's limits as you type. Add your main keyword to check it's in the title, description and tags — and that nothing will get your gig flagged.",
    "related": ["fiverr-gig-image-resizer", "fiverr-fee-calculator", "fiverr-reverse-fee-calculator", "invoice-generator"],
    "ui": '''<form class="tool-panel" id="calc" autocomplete="off">
<div class="field"><label for="kw">Main keyword (optional)</label><input class="input" id="kw" name="kw" placeholder="e.g. wordpress website"></div>
<div class="field"><label for="title">Gig title</label>
<div class="input-money"><span class="sym" style="font-weight:600">I will</span><input class="input" id="title" name="title" style="padding-left:64px;font-size:1rem;font-weight:500" placeholder="design a modern wordpress website for your business"></div>
<div class="counter-meter" id="title-meter"><span></span></div><div class="count-row" id="title-count"></div></div>
<div class="field"><label for="desc">Gig description</label><textarea class="input" id="desc" name="desc" rows="8" placeholder="What you do, who it's for, what's included and why you."></textarea>
<div class="counter-meter" id="desc-meter"><span></span></div><div class="count-row" id="desc-count"></div></div>
<div class="field"><label for="tags">Search tags</label><input class="input" id="tags" name="tags" placeholder="wordpress, website design, landing page"><div class="count-row" id="tags-count"></div><p class="hint">Separate with commas.</p></div>
<div class="field"><label for="profile">Seller profile description</label><textarea class="input" id="profile" name="profile" rows="4"></textarea>
<div class="counter-meter" id="profile-meter"><span></span></div><div class="count-row" id="profile-count"></div></div>
<div class="res-actions"><button type="button" class="btn btn-ghost btn-small" id="copy-title">Copy title</button><button type="button" class="btn btn-ghost btn-small" id="copy-desc">Copy description</button><button type="button" class="btn btn-ghost btn-small" id="clear">Clear all</button></div>
</form>
<div class="tool-out"><div class="result"><div class="res-head"><span class="res-title">Gig check</span><span class="pill gold" id="score"></span></div>
<div class="score-ring"><p class="title-preview" id="title-preview"></p></div>
<ul class="checks" id="checks"></ul></div></div>''',
    "content": '''<h2>Fiverr gig character limits</h2>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th class="num">Limit</th></tr></thead>
<tbody>
<tr><td>Gig title (including “I will”)</td><td class="num">80 characters</td></tr>
<tr><td>Gig description</td><td class="num">1,200 characters (120 minimum)</td></tr>
<tr><td>Search tags</td><td class="num">Up to 5</td></tr>
<tr><td>Seller profile description</td><td class="num">150–600 characters</td></tr>
</tbody></table></div>
<p>Characters include spaces and punctuation. Fiverr counts the “I will” at the start of your title, which is why the counter includes it.</p>

<h2>How to write a gig title that ranks</h2>
<ul>
<li><strong>Lead with the keyword buyers type.</strong> “I will build a WordPress website” beats “I will be your expert web partner”.</li>
<li><strong>Be specific.</strong> Name the platform, format or outcome: Shopify store, YouTube thumbnail, SEO blog post.</li>
<li><strong>Don't stuff.</strong> One main keyword and one variation is enough. Titles that read like a list of tags look spammy to buyers.</li>
</ul>

<h2>Writing the description</h2>
<p>Use the 1,200 characters to answer what a buyer is wondering: what exactly do I get, how fast, and why you? A structure that works well:</p>
<ol>
<li>One sentence on the result you deliver.</li>
<li>A short bullet list of what's included.</li>
<li>Why you — experience, speed, a specific niche.</li>
<li>A clear next step: “Message me before ordering if your project is custom.”</li>
</ol>

<h2>What gets gigs flagged</h2>
<p>Fiverr doesn't allow contact details or ways to move the conversation off the platform. The checker warns you about emails, links, phone numbers and mentions of outside apps, so you can remove them before publishing. Pair this with a correctly sized gallery image from the <a href="/fiverr-gig-image-resizer/">gig image resizer</a>.</p>''',
    "faq": [
        ("What is the character limit for a Fiverr gig title?", "80 characters, including the “I will” that every title starts with."),
        ("How long can a Fiverr gig description be?", "Up to 1,200 characters, with a minimum of 120. Most strong descriptions use 800–1,200."),
        ("How many search tags can I add to a Fiverr gig?", "Up to 5. Use the phrases buyers actually search for, and keep each one short."),
        ("What is the Fiverr profile description limit?", "Between 150 and 600 characters."),
        ("Is my text saved?", "Yes, in your browser on this device only, so you can come back to a draft. Use “Clear all” to remove it."),
    ],
})

# ---------------------------------------------------------------- Gig image
TOOLS.append({
    "slug": "fiverr-gig-image-resizer", "js": "gigimage", "cat": "gig", "icon": I["image"], "appcat": "DesignApplication",
    "short": "Gig image resizer", "blurb": "Resize and crop to Fiverr's 1280 × 769 px, in your browser.",
    "title": "Fiverr Gig Image Resizer — 1280 × 769 px, Free & Private",
    "desc": "Resize and crop any image to Fiverr's recommended gig image size of 1280 × 769 px (or the 712 × 430 minimum). Drag to position, fit with a background, download JPG or PNG.",
    "h1": "Fiverr gig image resizer",
    "lede": "Drop in an image and get a gig gallery image at Fiverr's recommended 1280 × 769 px. Drag to choose the crop, or fit the whole image on a background. Nothing is uploaded.",
    "related": ["fiverr-gig-character-counter", "fiverr-fee-calculator", "fiverr-reverse-fee-calculator", "invoice-generator"],
    "ui": '''<div class="tool-panel">
<div class="drop" id="drop" role="button" tabindex="0" aria-label="Choose an image">
<span class="di"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 16V4M7 9l5-5 5 5M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg></span>
<strong>Choose an image or drop it here</strong><span class="hint">JPG, PNG or WebP. You can also paste from the clipboard.</span></div>
<input type="file" id="file" accept="image/*" hidden>
<div id="editor" hidden>
<div class="preview-box"><canvas id="canvas" width="1280" height="769" style="touch-action:none;cursor:grab" aria-label="Gig image preview"></canvas></div>
<p class="hint" id="drag-hint" style="margin-top:8px">Drag the image to choose what stays in the frame.</p>
<p class="hint" id="img-info"></p>
</div>
</div>
<form class="tool-out" id="calc" autocomplete="off">
<div class="field"><label for="size">Size</label><select class="input" id="size" name="size">
<option value="1280x769">Gig image, recommended (1280 × 769)</option><option value="712x430">Gig image, minimum (712 × 430)</option><option value="2560x1538">Gig image, high resolution (2560 × 1538)</option></select></div>
<div class="field"><label for="fit">Fit</label><select class="input" id="fit" name="fit"><option value="cover">Fill and crop</option><option value="contain">Fit whole image on a background</option></select></div>
<div class="field" id="zoom-box"><label for="zoom">Zoom</label><input type="range" id="zoom" name="zoom" min="100" max="300" value="100"></div>
<div class="field" id="bg-box" hidden><label for="bg">Background colour</label><input class="input" type="color" id="bg" name="bg" value="#ffffff"></div>
<div class="field"><label for="format">Format</label><select class="input" id="format" name="format"><option value="image/jpeg">JPG (smaller file)</option><option value="image/png">PNG (sharper text)</option></select></div>
<div class="res-actions"><button type="button" class="btn" id="download"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>Download image</button><button type="button" class="btn btn-ghost" id="change">Change image</button></div>
</form>''',
    "content": '''<h2>Fiverr gig image size</h2>
<p>Fiverr recommends gig gallery images of <strong>1280 × 769 pixels</strong> at 72 DPI. The minimum is 712 × 430 px and the maximum is 4000 × 2416 px. All of these share the same shape — roughly 5:3 — so an image made at any of them displays without stretching.</p>
<div class="table-wrap"><table>
<thead><tr><th>Use</th><th class="num">Size (px)</th></tr></thead>
<tbody>
<tr><td>Recommended gig image</td><td class="num">1280 × 769</td></tr>
<tr><td>Minimum</td><td class="num">712 × 430</td></tr>
<tr><td>Maximum</td><td class="num">4000 × 2416</td></tr>
</tbody></table></div>

<h2>Why your gig image looks cropped or blurry</h2>
<ul>
<li><strong>Wrong shape.</strong> A square or tall image gets cropped in search results. Resizing to 1280 × 769 here means you choose the crop, not Fiverr.</li>
<li><strong>Too small.</strong> If the original is smaller than the target size, it has to be enlarged and will look soft. The tool warns you when that happens.</li>
<li><strong>Text near the edges.</strong> Fiverr's search cards show a slightly trimmed version of your image. Keep text and faces away from the outer edges.</li>
</ul>

<h2>Tips for a gig image that gets clicks</h2>
<ul>
<li>Show the result: a finished website, a logo on a mockup, a before-and-after.</li>
<li>Use a few large words at most. Thumbnails are small on mobile.</li>
<li>Don't add Fiverr badges, levels or ratings — Fiverr adds those itself and may remove images that include them.</li>
<li>Use JPG for photos and PNG for designs with sharp text.</li>
</ul>
<p>Then check your title and description with the <a href="/fiverr-gig-character-counter/">gig character counter</a>.</p>''',
    "faq": [
        ("What size should a Fiverr gig image be?", "1280 × 769 pixels is Fiverr's recommended size. The minimum is 712 × 430 and the maximum is 4000 × 2416."),
        ("Is my image uploaded anywhere?", "No. The image is processed entirely in your browser using the canvas, and the download is created on your device."),
        ("Why does my image look blurry after resizing?", "The original is smaller than the target size, so it had to be enlarged. Start from a larger image or a design exported at 1280 × 769 or bigger."),
        ("Should I use JPG or PNG?", "JPG for photos — the file is smaller. PNG for graphics with text or flat colours, which stay sharper."),
    ],
})
