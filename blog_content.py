# Blog posts. Body is HTML inside .prose. Use cta() for inline tool call-outs.

def cta(slug, title, text, btn="Open the tool"):
    return ('<div class="tool-cta"><div><b>' + title + '</b><p>' + text + '</p></div>'
            '<a class="btn btn-small" href="/' + slug + '/">' + btn + '</a></div>')


def takeaways(items):
    return '<div class="takeaways"><b>Key points</b><ul>' + "".join('<li>' + i + '</li>' for i in items) + '</ul></div>'


POSTS = []

# ------------------------------------------------------------------ 1
POSTS.append({
    "slug": "how-to-withdraw-from-fiverr-in-pakistan", "image": "/assets/img/blog/how-to-withdraw-from-fiverr-in-pakistan", "alt": "Gold coins flowing from a laptop through a glass pipe into a bank building",
    "title": "How to Withdraw Money from Fiverr in Pakistan (Payoneer Guide 2026)",
    "h1": "How to withdraw money from Fiverr in Pakistan",
    "desc": "Step-by-step guide to withdrawing Fiverr earnings in Pakistan through Payoneer: clearance period, the $3 withdrawal fee, converting to PKR, the bank PRC and how to keep more of every withdrawal.",
    "lede": "From a completed order to rupees in your bank account — every step, every fee, and the small habits that save you thousands of rupees a year.",
    "date": "2026-10-15", "cat": "Payments", "icon": "bank",
    "tools": ["fiverr-fee-calculator", "payoneer-to-pkr-calculator", "pakistan-freelancer-tax-calculator"],
    "body": takeaways([
        "In Pakistan, Fiverr pays out through <strong>Payoneer</strong>. Even the “bank transfer” option runs through Payoneer.",
        "Fiverr charges a flat <strong>$3 per withdrawal</strong>, not per order — so withdrawing in batches saves money.",
        "Payoneer converts dollars to rupees at a rate up to about <strong>2% below mid-market</strong>.",
        "Keep the bank's <strong>Proceeds Realisation Certificate (PRC)</strong> — it supports the low tax rate on IT exports.",
    ]) + '''
<h2>How the money moves</h2>
<p>Before the steps, it helps to see the whole journey. Your money passes through four stages, and each one has its own wait or fee:</p>
<ol>
<li><strong>Order completed.</strong> The buyer accepts your delivery (or it auto-completes). Fiverr keeps its 20% service fee.</li>
<li><strong>Pending clearance.</strong> Earnings are held for 14 days — 7 days for Top Rated sellers and Fiverr Pro — before you can withdraw them.</li>
<li><strong>Fiverr to Payoneer.</strong> You withdraw your available balance to Payoneer. Fiverr charges a flat fee per withdrawal.</li>
<li><strong>Payoneer to your bank.</strong> Payoneer converts the dollars to rupees and sends them to your local bank account, usually within one to three business days.</li>
</ol>
''' + cta("fiverr-fee-calculator", "See what an order really pays", "Enter your order price to see Fiverr’s cut and your earnings in PKR at today’s rate.", "Open Fiverr calculator") + '''
<h2>Step 1: Open and verify a Payoneer account</h2>
<p>If you don't have one yet, sign up for Payoneer — you can start from Fiverr's withdrawal page or from Payoneer's website. A few things save headaches later:</p>
<ul>
<li>Use your <strong>real name exactly as it appears on your CNIC</strong>. It must match your Fiverr account and your bank account title.</li>
<li>Complete identity verification straight away. Accounts under review can't withdraw.</li>
<li>Use an email and phone number you'll keep long-term. Payoneer sends verification codes to both.</li>
</ul>

<h2>Step 2: Add Payoneer as your Fiverr withdrawal method</h2>
<ol>
<li>On Fiverr, go to <strong>Earnings</strong> (from your profile menu, under Billing / Earnings).</li>
<li>Choose <strong>Payoneer</strong> as your withdrawal method and sign in to Payoneer when asked to link the accounts.</li>
<li>Wait for the link to be confirmed. After you add or change a Payoneer method, Fiverr makes you wait <strong>24 hours</strong> before your first withdrawal.</li>
</ol>

<h2>Step 3: Withdraw from Fiverr to Payoneer</h2>
<ol>
<li>In <strong>Earnings</strong>, check your <em>Available for withdrawal</em> balance. Pending earnings can't be withdrawn yet.</li>
<li>Click <strong>Withdraw</strong>, choose Payoneer and enter the amount.</li>
<li>Confirm through the email or two-factor prompt Fiverr sends you.</li>
</ol>
<p>Fiverr deducts a flat <strong>$3</strong> from each withdrawal. It's the same whether you withdraw $50 or $1,000, which is why the timing of your withdrawals matters (more on that below).</p>

<h2>Step 4: Withdraw from Payoneer to your bank in PKR</h2>
<ol>
<li>In Payoneer, add your Pakistani bank account: bank name, <strong>IBAN</strong> and an account title that matches your Payoneer name.</li>
<li>Go to <strong>Withdraw → To bank account</strong>, pick the bank and choose the amount.</li>
<li>Payoneer shows the exchange rate and the rupee amount <em>before</em> you confirm. Check it.</li>
<li>Confirm. Funds usually arrive in one to three business days.</li>
</ol>
''' + cta("payoneer-to-pkr-calculator", "How many rupees will you get?", "Convert your Payoneer balance to PKR with the live rate and Payoneer’s conversion fee.", "Open Payoneer to PKR") + '''
<h2>What it actually costs: a worked example</h2>
<p>Say you complete a <strong>$500</strong> order and withdraw it on its own, with a mid-market rate of Rs 277 per dollar:</p>
<div class="table-wrap"><table><tbody>
<tr><td>Order price</td><td class="num">$500.00</td></tr>
<tr><td>Fiverr service fee (20%)</td><td class="num">−$100.00</td></tr>
<tr><td>Fiverr withdrawal fee</td><td class="num">−$3.00</td></tr>
<tr><td>Arrives in Payoneer</td><td class="num">$397.00</td></tr>
<tr><td>At mid-market (Rs 277)</td><td class="num">Rs 1,09,969</td></tr>
<tr><td>Payoneer conversion (about 2%)</td><td class="num">−Rs 2,199</td></tr>
<tr><th>In your bank</th><th class="num">≈ Rs 1,07,770</th></tr>
</tbody></table></div>
<p>Rates change daily and your bank may handle tax deductions on remittances, so treat this as an illustration — the calculators above use today's rate.</p>

<h2>Five ways to keep more of every withdrawal</h2>
<ul>
<li><strong>Withdraw in batches.</strong> Five $100 withdrawals cost $15 in Fiverr fees; one $500 withdrawal costs $3.</li>
<li><strong>Check the rate before you confirm.</strong> Payoneer shows it on the confirmation screen. If you're not in a hurry, compare it with the day's mid-market rate.</li>
<li><strong>Keep every PRC.</strong> Ask your bank for the Proceeds Realisation Certificate for each transfer. It documents your income as an IT export, which is what lets you pay the reduced final tax.</li>
<li><strong>Register with PSEB.</strong> It cuts the tax on your remittances from 1% to 0.25%. Our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a> walks through it.</li>
<li><strong>Watch Payoneer's annual fee.</strong> Payoneer may charge an account fee if you receive less than a set amount in a year. Check the Fees page in your account.</li>
</ul>

<h2>Common problems and fixes</h2>
<h3>“Withdraw” button is greyed out</h3>
<p>Your earnings are probably still pending clearance, or you changed your withdrawal method less than 24 hours ago.</p>
<h3>Payoneer withdrawal rejected by the bank</h3>
<p>Almost always a name mismatch. The bank account title, Payoneer name and CNIC name must match. Fix it with your bank or Payoneer support.</p>
<h3>Money left Payoneer but hasn't arrived</h3>
<p>Allow three business days, then contact your bank with the Payoneer transaction details. Weekends and bank holidays add delays.</p>
''',
    "faq": [
        ("Can I withdraw from Fiverr directly to a Pakistani bank?", "In Pakistan, Fiverr's payouts go through Payoneer. You withdraw from Fiverr to Payoneer, then from Payoneer to your local bank in PKR."),
        ("How much does Fiverr charge to withdraw to Payoneer?", "A flat $3 per withdrawal, regardless of the amount. If your withdrawal screen shows a different fee, that's the one that applies to your account."),
        ("How long does Fiverr take to release my money?", "Earnings clear 14 days after an order completes, or 7 days for Top Rated sellers and Fiverr Pro. After that, Payoneer to your bank usually takes one to three business days."),
        ("Do I pay tax on Fiverr income in Pakistan?", "Yes. IT and IT-enabled service exports can be taxed at a reduced final rate on remittances — 0.25% if you're registered with PSEB, or 1% if you're not — provided you file your return."),
    ],
})

# ------------------------------------------------------------------ 2
POSTS.append({
    "slug": "pseb-registration-freelancers-tax-pakistan", "image": "/assets/img/blog/pseb-registration-freelancers-tax-pakistan", "alt": "Glass shield beside a stack of official documents and a stamp, with a percent symbol above",
    "title": "PSEB Registration for Freelancers: Pay 0.25% Tax Instead of 1% (2026-27)",
    "h1": "PSEB registration for freelancers: pay 0.25% tax instead of 1%",
    "desc": "How Pakistani freelancers can register with PSEB, which documents you need, the fee, renewal and how it cuts tax on foreign remittances from 1% to 0.25% for tax year 2026-27.",
    "lede": "One registration, done once a year, cuts the tax on your foreign earnings by three quarters. Here's who qualifies, what you need and exactly how to do it.",
    "date": "2026-10-15", "cat": "Tax", "icon": "moon",
    "tools": ["pakistan-freelancer-tax-calculator", "payoneer-to-pkr-calculator", "invoice-generator"],
    "body": takeaways([
        "Freelancers exporting IT and IT-enabled services can pay a <strong>final tax of 0.25%</strong> on foreign remittances if they're registered with PSEB — <strong>1%</strong> if they're not.",
        "You need a <strong>personal NTN</strong>, your CNIC and a bank account letter. Registration is done online.",
        "The low rate only applies if you <strong>file your income tax return</strong> and stay on the Active Taxpayers List.",
        "Registration is renewed every year.",
    ]) + '''
<h2>Why it's worth it</h2>
<p>The Pakistan Software Export Board (PSEB) registers freelancers who export IT and IT-enabled services. For tax year 2026-27, registered freelancers pay a <strong>0.25% final tax</strong> on their foreign remittances under section 154A of the Income Tax Ordinance, compared with <strong>1%</strong> for those who aren't registered. The 0.25% rate is set to apply for tax years 2026 to 2029.</p>
<div class="table-wrap"><table>
<thead><tr><th>Yearly foreign income</th><th class="num">Tax at 1%</th><th class="num">Tax at 0.25%</th><th class="num">You save</th></tr></thead>
<tbody>
<tr><td>$6,000 (Rs 16,62,000)</td><td class="num">Rs 16,620</td><td class="num">Rs 4,155</td><td class="num">Rs 12,465</td></tr>
<tr><td>$12,000 (Rs 33,24,000)</td><td class="num">Rs 33,240</td><td class="num">Rs 8,310</td><td class="num">Rs 24,930</td></tr>
<tr><td>$24,000 (Rs 66,48,000)</td><td class="num">Rs 66,480</td><td class="num">Rs 16,620</td><td class="num">Rs 49,860</td></tr>
</tbody></table></div>
<p class="hint">At Rs 277 per dollar. For most freelancers the saving is many times the registration fee.</p>
''' + cta("pakistan-freelancer-tax-calculator", "Calculate your tax", "See your tax at 0.25% and 1% using today’s dollar rate.", "Open tax calculator") + '''
<h2>Who can register</h2>
<p>PSEB registration is for individuals who provide <strong>computer software, IT or IT-enabled services</strong> to clients abroad. Most online freelancers — developers, designers, digital marketers and similar remote service providers — fall into this group. If your work is outside IT and IT-enabled services, check your category with PSEB or a tax adviser before relying on the reduced rate.</p>

<h2>Before you apply</h2>
<ol>
<li><strong>Get a personal NTN.</strong> Register on the FBR's IRIS portal if you don't have one. Use a personal NTN with no business name.</li>
<li><strong>Become a filer.</strong> File your income tax return so you appear on the Active Taxpayers List (ATL). The deadline for tax year 2026 returns was 30 September 2026.</li>
<li><strong>Prepare your documents</strong> as clear scans:
<ul>
<li>CNIC, both sides</li>
<li>Personal NTN</li>
<li>A letter or certificate from your bank for your personal account</li>
</ul></li>
</ol>

<h2>How to register, step by step</h2>
<p>PSEB handles freelancer registration online through its Tech Destination portal.</p>
<ol>
<li><strong>Create an account</strong> on the portal. Your login details arrive by email.</li>
<li><strong>Fill in the freelancer registration form</strong> and upload your documents. Incomplete forms are declined, so double-check every field.</li>
<li><strong>Wait for initial approval.</strong></li>
<li><strong>Pay the fee</strong> through the portal's payment gateway (or by pay order / demand draft to Pakistan Software Export Board), then upload the receipt. At the time of writing the fee for a new freelancer registration was Rs 1,000 — confirm the current amount on the portal.</li>
<li><strong>Submit for final approval.</strong> Your certificate is usually issued within two to five working days after the payment is verified.</li>
</ol>

<h2>Renewing each year</h2>
<p>Registration is renewed annually through the same portal. Renewal asks for a summary of your export revenue (with the State Bank's IT/ITeS purpose code) and your income tax return for the previous year, plus the renewal fee (Rs 2,000 at the time of writing). Put a reminder in your calendar a month before it expires.</p>

<h2>After you're registered: keep the low rate</h2>
<ul>
<li><strong>Receive money through banking channels.</strong> Payoneer withdrawals to your bank account count; cash and informal transfers don't.</li>
<li><strong>Collect a PRC for every remittance.</strong> The Proceeds Realisation Certificate from your bank is your evidence of export income.</li>
<li><strong>File your return every year</strong> and choose the final tax regime for your export income. If you don't file, the concession can be lost and your income taxed at normal slab rates.</li>
<li><strong>Keep invoices</strong> that match your remittances — a simple <a href="/invoice-generator/">invoice</a> for each direct client is enough.</li>
</ul>
<p class="disclaimer" style="margin-top:20px">This guide is general information based on published rules for tax year 2026-27, not tax advice. Rates and procedures change with each budget — confirm with FBR, PSEB or a tax adviser.</p>
''',
    "faq": [
        ("How much is the PSEB registration fee for freelancers?", "At the time of writing, Rs 1,000 for a new registration and Rs 2,000 for renewal, per year. Check the PSEB portal for the current fee."),
        ("Do I need an NTN to register with PSEB?", "Yes. You need a personal NTN from FBR, along with your CNIC and a letter from your bank."),
        ("How long does PSEB registration take?", "Once your payment is verified, the certificate is typically issued in two to five working days."),
        ("Is PSEB registration enough to pay 0.25%?", "No. You also need to file your income tax return, stay on the Active Taxpayers List and receive your income through banking channels."),
    ],
})

# ------------------------------------------------------------------ 3
POSTS.append({
    "slug": "how-to-price-freelance-services", "image": "/assets/img/blog/how-to-price-freelance-services", "alt": "Golden balance scale weighing an alarm clock against stacks of coins, with a blank price tag",
    "title": "How to Price Your Freelance Services: Hourly, Fixed and Value-Based",
    "h1": "How to price your freelance services",
    "desc": "A practical guide to freelance pricing: find your minimum rate, include platform fees properly, choose between hourly and fixed price, build packages and raise your rates with confidence.",
    "lede": "Most freelancers set prices by copying competitors. Here's a better method — start from what you need, add what platforms take, and charge for the value you create.",
    "date": "2026-10-15", "cat": "Pricing", "icon": "tag",
    "tools": ["hourly-rate-calculator", "fiverr-reverse-fee-calculator", "fixed-price-vs-hourly-calculator", "project-quote-calculator"],
    "body": takeaways([
        "Work out your <strong>minimum rate</strong> from your income goal, costs, tax and realistic billable hours.",
        "Include platform fees by <strong>dividing</strong>, not adding: price = what you want ÷ (1 − fee).",
        "Fixed price pays more when you're fast and the scope is clear; hourly protects you when it isn't.",
        "Your minimum is a floor. Price above it for skill, speed and results.",
    ]) + '''
<h2>Step 1: Find your floor</h2>
<p>Your floor is the lowest rate that still pays your life and your business. Below it, every project makes you poorer. To find it you need four numbers:</p>
<ul>
<li><strong>Your income goal</strong> — what you want to take home each month.</li>
<li><strong>Your business costs</strong> — internet, software, equipment, Connects, subscriptions.</li>
<li><strong>Tax</strong> — the share you'll pay on what you earn.</li>
<li><strong>Billable hours</strong> — the hours a client actually pays for.</li>
</ul>
<p>The last one is where most people go wrong. In a 40-hour week you also answer messages, fix your profile, write proposals and do revisions you don't charge for. For many freelancers only 60–75% of working time is billable.</p>
<p class="formula">Minimum hourly rate = (yearly goal ÷ (1 − tax) + yearly costs) ÷ (1 − platform fee) ÷ billable hours</p>
''' + cta("hourly-rate-calculator", "Find your minimum rate", "Enter your goal, costs and hours — the calculator does the rest.", "Open hourly rate calculator") + '''
<h2>Step 2: Price in the platform fee — correctly</h2>
<p>If you want $100 from a Fiverr order, charging $120 doesn't work: Fiverr takes 20% of $120, which is $24, and you get $96. Fees are a percentage of the final price, so divide instead:</p>
<p class="formula">Price = amount you want ÷ (1 − fee rate)</p>
<p>$100 ÷ 0.80 = <strong>$125</strong> on Fiverr. On Upwork at a 10% fee, $100 ÷ 0.90 = $111.11.</p>
''' + cta("fiverr-reverse-fee-calculator", "Price for the amount you want", "Works backwards from the money you want — in dollars or rupees — to the price you should list.", "Open reverse calculator") + '''
<h2>Step 3: Choose hourly or fixed price</h2>
<p>Both can be right. The question is who carries the risk if the work takes longer than planned.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Hourly</th><th>Fixed price</th></tr></thead>
<tbody>
<tr><td>Best for</td><td>Ongoing work, unclear scope</td><td>Clear deliverables you've done before</td></tr>
<tr><td>Who carries the risk</td><td>The client</td><td>You</td></tr>
<tr><td>How you earn more</td><td>More hours</td><td>Working faster</td></tr>
<tr><td>Main danger</td><td>Clients watch the clock</td><td>Scope creep</td></tr>
</tbody></table></div>
<p>Before accepting a fixed price, estimate the hours honestly and add a buffer for revisions. If the job would take longer than the <strong>break-even point</strong> — the fixed price after fees divided by your hourly rate after fees — you're better off hourly.</p>
''' + cta("fixed-price-vs-hourly-calculator", "Fixed or hourly?", "Compare an offer against your hourly rate, including the extra time projects usually take.", "Compare now") + '''
<h2>Step 4: Package your work</h2>
<p>On Fiverr, three packages (Basic, Standard, Premium) do more than offer choice: they anchor the buyer. Many buyers pick the middle option, so make Standard your main offer, Basic a lighter entry point, and Premium the full version with faster delivery or extras.</p>
<ul>
<li>Make the difference between packages <strong>obvious</strong>: pages, revisions, delivery time, source files.</li>
<li>Put your most common request in Standard.</li>
<li>Use gig extras (faster delivery, extra revision) to raise the order value without new clients.</li>
</ul>

<h2>Step 5: Charge for value, not just time</h2>
<p>A landing page that brings a client ten new customers a month is worth more than the hours it took. Once you have proof — results, reviews, a strong portfolio — start pricing on the outcome. Ask clients what the project is worth to them, and quote a price that's fair for that result.</p>

<h2>When and how to raise your rates</h2>
<ul>
<li>When you're consistently busy, your price is too low.</li>
<li>Raise rates for <strong>new clients first</strong>; give existing clients notice.</li>
<li>Increase in steps of 10–20% and watch how buyers respond.</li>
<li>Recheck your floor whenever your costs, tax or platform fees change.</li>
</ul>
''' + cta("project-quote-calculator", "Build a quote", "Turn tasks and hours into a client-ready price with buffer, rush fee and deposit.", "Open quote calculator"),
    "faq": [
        ("How do I calculate my freelance hourly rate?", "Add your yearly income goal (grossed up for tax) and yearly business costs, gross that up for platform fees, then divide by your realistic billable hours."),
        ("Should beginners charge low prices?", "Charge at or near your minimum rate to win early reviews, then raise prices as reviews and results build up. Don't go below your floor."),
        ("How much should I add for Fiverr's fee?", "Divide by 0.8 instead of adding 20%. To keep $100, charge $125."),
    ],
})

# ------------------------------------------------------------------ 4
POSTS.append({
    "slug": "how-to-write-upwork-proposal", "image": "/assets/img/blog/how-to-write-upwork-proposal", "alt": "Paper airplane flying out of a laptop towards a target with an arrow in the bullseye",
    "title": "How to Write an Upwork Proposal That Gets Replies (Template + Example)",
    "h1": "How to write an Upwork proposal that gets replies",
    "desc": "A simple structure for Upwork proposals that clients actually read: a strong first line, the client's real goal, one piece of proof, a short plan and a question. Includes a template and example.",
    "lede": "Clients often see your first couple of lines before deciding whether to open the rest. This is how to make those lines — and the rest of the proposal — count.",
    "date": "2026-10-15", "cat": "Winning work", "icon": "send",
    "tools": ["upwork-proposal-generator", "upwork-fee-calculator", "fixed-price-vs-hourly-calculator"],
    "body": takeaways([
        "Open with <strong>their project</strong>, not your name or a greeting template.",
        "Name the <strong>real goal</strong> behind the task, then show <strong>one relevant result</strong>.",
        "Give a short plan and end with <strong>one specific question</strong>.",
        "Aim for 120–200 words. Clients skim.",
    ]) + '''
<h2>Why most proposals get ignored</h2>
<p>A client posting a job may get dozens of proposals. Most start the same way — “Dear Sir, I am an expert with 5 years of experience…” — and say nothing about the client's project. The client can tell in one line that it's a copy-paste, and moves on.</p>
<p>The proposals that get replies do the opposite: they prove, in the first sentence, that the freelancer read the job post.</p>

<h2>The five-part structure</h2>
<ol>
<li><strong>Hook: their project.</strong> “I read your post about a mobile-friendly Shopify store — this is exactly the kind of project I do.”</li>
<li><strong>Their real goal.</strong> They asked for a Shopify store; what they want is more sales from mobile visitors. Say so.</li>
<li><strong>One piece of proof.</strong> A similar project with a result. “I rebuilt a skincare store and its mobile conversion rate rose 38% in two months.”</li>
<li><strong>A short plan.</strong> Three or four steps showing how you'd approach it.</li>
<li><strong>One question.</strong> Specific to their project. It invites a reply — and replies lead to interviews.</li>
</ol>

<h2>Template</h2>
<pre class="gen-out" style="margin-bottom:1.3em">Hi [name],

I read your post about [what they need] — [one line on why it fits you]. I understand the real goal is [their outcome], so that's what I'll focus on.

Relevant work: [similar project + result].

Here's how I'd approach it:
1. [step]
2. [step]
3. [step]

Timeline: [time]. Price: [if relevant].

One question before I start: [specific question]?

Thanks,
[your name]</pre>
''' + cta("upwork-proposal-generator", "Generate your proposal", "Fill in the client’s need, your proof and plan — get a focused proposal in three tones.", "Open proposal generator") + '''
<h2>Before and after</h2>
<h3>Before</h3>
<p><em>“Dear Sir/Madam, I am a professional web developer with 5+ years of experience in WordPress, Shopify, HTML, CSS, JavaScript, PHP and React. I have completed 300+ projects with 100% client satisfaction. I can do your job perfectly. Please check my portfolio. Waiting for your positive response.”</em></p>
<p>Nothing here is about the client. The skills list could be pasted into any job.</p>
<h3>After</h3>
<p><em>“Hi Sarah, I read your post about a fast, mobile-friendly Shopify store — this is exactly what I build. Since most of your traffic is mobile, I'll design mobile-first and keep the store light so pages load quickly. I recently rebuilt a skincare store on Shopify and its mobile conversion rate rose 38% in two months. My plan: audit your current store, design a clean mobile-first theme, set up products and payments, then test on real devices. Ten working days. Quick question: do you already have product photos ready?”</em></p>

<h2>Mistakes that cost you interviews</h2>
<ul>
<li><strong>Ignoring the client's questions.</strong> If the job post asks something, answer it in your first lines.</li>
<li><strong>Listing every skill you have.</strong> One relevant result beats ten technologies.</li>
<li><strong>Writing an essay.</strong> Long proposals rarely get read in full. Save detail for the interview.</li>
<li><strong>Applying late.</strong> Jobs posted in the last hour or two tend to have fewer proposals competing for attention.</li>
<li><strong>Bidding on everything.</strong> Each proposal costs Connects. Fewer, better proposals win more per Connect.</li>
</ul>

<h2>Check the numbers before you send</h2>
<p>Upwork shows the service fee for each job before you submit — anywhere from 0% to 15%. Factor it into your price so you know what you'll actually take home.</p>
''' + cta("upwork-fee-calculator", "What will you take home?", "Enter the job’s service fee, Connects and withdrawal method.", "Open Upwork calculator"),
    "faq": [
        ("How long should an Upwork proposal be?", "Usually 120–200 words: enough to show you understood the job and have a plan, short enough to read in under a minute."),
        ("Should I use a proposal template?", "Use a structure, not a copy-paste. Change the need, goal, proof and question for every job."),
        ("Should I include my price?", "If the job is fixed-price or the client asks, yes. Otherwise you can discuss it after they reply."),
    ],
})

# ------------------------------------------------------------------ 5
POSTS.append({
    "slug": "fiverr-gig-seo-guide", "image": "/assets/img/blog/fiverr-gig-seo-guide", "alt": "Magnifying glass over three glass cards, the middle card glowing with an upward arrow",
    "title": "Fiverr Gig SEO: How to Write Titles, Descriptions and Tags That Get Found",
    "h1": "Fiverr gig SEO: titles, descriptions and tags that get found",
    "desc": "How to optimise a Fiverr gig for search: find the keywords buyers use, write an 80-character title, a 1,200-character description and 5 tags, and avoid the mistakes that get gigs hidden or removed.",
    "lede": "A great service nobody finds doesn't sell. Here's how to put the right words in the right places so buyers searching for what you do actually see your gig.",
    "date": "2026-10-15", "cat": "Fiverr", "icon": "spark",
    "tools": ["fiverr-gig-character-counter", "fiverr-gig-image-resizer", "fiverr-profile-bio-generator"],
    "body": takeaways([
        "Find your keyword from <strong>Fiverr's own search suggestions</strong>, not guesswork.",
        "Put the main keyword <strong>early in the title</strong> — you have 80 characters including “I will”.",
        "Use the 1,200-character description to answer: what's included, how fast, why you.",
        "Never include emails, links or phone numbers — they can get a gig removed.",
    ]) + '''
<h2>Step 1: Find the words buyers actually type</h2>
<p>Start typing your service into Fiverr's search bar and note the suggestions that appear — those come from real searches. “WordPress website”, “WordPress website design” and “WordPress landing page” are different searches with different buyers.</p>
<ul>
<li>Pick <strong>one main keyword</strong> for each gig — specific enough to stand out, common enough that people search for it.</li>
<li>Look at the top gigs for that search. Note how they phrase their titles and what their packages include.</li>
<li>Make one gig per service. A gig that tries to rank for everything usually ranks for nothing.</li>
</ul>

<h2>Step 2: Write the title</h2>
<p>Your title starts with “I will” and has <strong>80 characters</strong> in total. A simple formula works well:</p>
<p class="formula">I will [main keyword as an action] + [specific detail or outcome]</p>
<ul>
<li>✔ <em>I will build a responsive WordPress website for your business</em></li>
<li>✔ <em>I will design a minimalist logo with unlimited revisions</em></li>
<li>✘ <em>I will be your best expert web designer and developer for anything</em></li>
</ul>
<p>Keep it readable. A title stuffed with keywords looks spammy to buyers, and buyers' clicks matter.</p>
''' + cta("fiverr-gig-character-counter", "Check your gig text", "Live character counts against Fiverr’s limits, keyword placement checks and contact-info warnings.", "Open gig counter") + '''
<h2>Step 3: Write the description</h2>
<p>You have up to <strong>1,200 characters</strong> (minimum 120). Use them to answer the buyer's questions in order:</p>
<ol>
<li><strong>The result</strong> in one sentence — what they get.</li>
<li><strong>What's included</strong> — a short bullet list.</li>
<li><strong>Why you</strong> — experience, speed, a niche you specialise in.</li>
<li><strong>A next step</strong> — “Message me before ordering if your project is custom.”</li>
</ol>
<p>Use your main keyword naturally once or twice. Break the text into short paragraphs or bullets — it's read on phones.</p>

<h2>Step 4: Choose your five tags</h2>
<p>You get up to <strong>5 search tags</strong>. Use your main keyword and close variations buyers search for: the platform (WordPress, Shopify), the type (landing page, e-commerce) and the use (business website). Skip generic words like “best” or “professional”.</p>

<h2>Step 5: Make the gig image work</h2>
<p>The recommended gig image size is <strong>1280 × 769 px</strong>. Show the result — a finished site on a laptop mockup, a logo on a business card — with a few large words at most. Don't add Fiverr badges, levels or ratings; Fiverr shows those itself and can remove images that include them.</p>
''' + cta("fiverr-gig-image-resizer", "Resize your gig image", "Crop any image to exactly 1280 × 769 px in your browser.", "Open image resizer") + '''
<h2>Things that hurt your gig</h2>
<ul>
<li><strong>Contact details.</strong> Emails, links, phone numbers or “contact me on WhatsApp” break Fiverr's rules.</li>
<li><strong>Copied descriptions.</strong> Write your own — duplicate text helps nobody.</li>
<li><strong>Slow replies.</strong> Response time is part of your seller performance. Answer messages quickly.</li>
<li><strong>Unclear packages.</strong> If buyers can't tell the difference between Basic and Standard, they message instead of ordering — or leave.</li>
</ul>

<h2>Don't forget your profile</h2>
<p>Buyers often check your profile before ordering. A focused description (150–600 characters) that says what you do, who you help and one result builds trust fast.</p>
''' + cta("fiverr-profile-bio-generator", "Write your profile bio", "Get a Fiverr description, Upwork overview and headline in your chosen tone.", "Open bio generator"),
    "faq": [
        ("How long can a Fiverr gig title be?", "80 characters, including the “I will” at the start."),
        ("How many tags can a Fiverr gig have?", "Up to 5 search tags."),
        ("What size should a Fiverr gig image be?", "1280 × 769 pixels is the recommended size."),
        ("How long should a Fiverr gig description be?", "Between 120 and 1,200 characters. Most strong descriptions use most of the space, broken into short sections."),
    ],
})

# ------------------------------------------------------------------ 6
POSTS.append({
    "slug": "how-to-invoice-clients-as-a-freelancer", "image": "/assets/img/blog/how-to-invoice-clients-as-a-freelancer", "alt": "Invoice sheet with a checkmark badge, a fountain pen, a calendar and gold coins",
    "title": "How to Invoice Clients as a Freelancer (and Get Paid On Time)",
    "h1": "How to invoice clients as a freelancer",
    "desc": "What to put on a freelance invoice, how to number it, which payment terms to use, how to handle currency, and polite follow-up messages for late payments. With free invoice, quote and contract tools.",
    "lede": "Fiverr and Upwork handle billing for you — direct clients don't. A clear invoice, sent on time with the right terms, is the simplest way to get paid faster.",
    "date": "2026-10-15", "cat": "Documents", "icon": "doc",
    "tools": ["invoice-generator", "quotation-generator", "freelance-contract-generator", "freelancer-currency-converter"],
    "body": takeaways([
        "Use the flow <strong>quote → agreement → invoice</strong> for every direct client.",
        "Every invoice needs a unique number, dates, itemised work, the total with currency, and how to pay you.",
        "Short payment terms (7–14 days) and an upfront deposit protect your cash flow.",
        "Follow up politely, on a schedule — most late payments are forgotten, not refused.",
    ]) + '''
<h2>The quote → agreement → invoice flow</h2>
<p>Getting paid starts before the work does. For every direct client:</p>
<ol>
<li><strong>Send a quotation</strong> with the price, what's included and how long it's valid.</li>
<li><strong>Agree the scope in writing</strong> — deliverables, timeline, payment schedule and revisions.</li>
<li><strong>Invoice</strong> the deposit at the start and the balance on delivery.</li>
</ol>
<p>When all three match, there's nothing to argue about when the invoice arrives.</p>
''' + cta("quotation-generator", "Send a professional quote", "Items, terms and a validity date — download as PDF.", "Open quotation generator") + '''
<h2>What every invoice must include</h2>
<ul>
<li>The word <strong>“Invoice”</strong> and a unique <strong>invoice number</strong></li>
<li>Your name or business name and contact details</li>
<li>The client's name and company</li>
<li><strong>Issue date</strong> and <strong>due date</strong></li>
<li>Itemised work: description, quantity and price for each line</li>
<li>Subtotal, any discount or tax, and the <strong>total with its currency</strong></li>
<li><strong>How to pay</strong>: Payoneer email, bank title and IBAN, or a payment link</li>
</ul>

<h2>Numbering your invoices</h2>
<p>Use a simple sequence — INV-0001, INV-0002 — and never reuse a number. Some freelancers add the year (INV-2026-014). Consistent numbering makes your records easy to match to bank remittances at tax time.</p>
''' + cta("invoice-generator", "Create an invoice in a minute", "Add your logo and items, pick a currency and download a PDF. Your details are saved for next time.", "Open invoice generator") + '''
<h2>Payment terms that protect you</h2>
<ul>
<li><strong>Short due dates.</strong> 7 or 14 days. “Net 30” is a long time to wait when you're a one-person business.</li>
<li><strong>Deposits.</strong> 30–50% upfront for new clients or larger projects.</li>
<li><strong>Milestones</strong> for long projects, so you're never owed weeks of work.</li>
<li><strong>Hand over final files after the final payment.</strong> Put this in your agreement.</li>
</ul>
''' + cta("freelance-contract-generator", "Put it in writing", "A plain-language agreement covering scope, payment, revisions and ownership.", "Open contract generator") + '''
<h2>Which currency to invoice in</h2>
<p>For international clients, invoicing in <strong>US dollars</strong> is usually simplest — most clients and payment services handle it easily. If a client insists on GBP or EUR, check how your provider converts it before agreeing, and quote the amount clearly with the currency code (for example, GBP 400.00).</p>
''' + cta("freelancer-currency-converter", "Check the conversion", "See any amount in PKR, INR, USD, GBP, EUR and 20 more currencies at live rates.", "Open currency converter") + '''
<h2>Following up on late payments</h2>
<p>Most late invoices are simply forgotten. A polite, scheduled follow-up gets most of them paid.</p>
<h3>On the due date</h3>
<p><em>“Hi [name], a quick reminder that invoice INV-0012 for [project] is due today. I've attached it again for convenience. Thanks!”</em></p>
<h3>Seven days late</h3>
<p><em>“Hi [name], invoice INV-0012 was due on [date] and is still open. Could you let me know when I can expect payment? Happy to resend payment details if needed.”</em></p>
<h3>Fourteen days or more</h3>
<p><em>“Hi [name], INV-0012 is now two weeks overdue. Per our agreement, further work is paused until it's settled. Please let me know by [date] how you'd like to proceed.”</em></p>

<h2>Keep records for tax</h2>
<p>Keep a copy of every invoice alongside the matching payment record. In Pakistan, match each invoice to the bank's Proceeds Realisation Certificate — together they show your income is IT export, which supports the reduced tax rate explained in our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a>.</p>
''',
    "faq": [
        ("Do I need to send invoices for Fiverr or Upwork orders?", "Not for the platform — they create their own records. You need invoices for direct clients, and when a client asks for one."),
        ("What payment terms should freelancers use?", "Due within 7–14 days, with a 30–50% deposit upfront for new clients or larger projects."),
        ("What should I do if a client doesn't pay?", "Send polite reminders on the due date, at 7 days and at 14 days. Pause work if your agreement allows it, and keep all communication in writing."),
    ],
})

# ------------------------------------------------------------------ 7
POSTS.append({
    "slug": "payoneer-fees-pakistan", "image": "/assets/img/blog/payoneer-fees-pakistan", "alt": "Glass tiles with a wallet, coins and a bank icon on a dark gradient background",
    "title": "Payoneer Fees in Pakistan Explained (2026): Every Charge, With Examples",
    "h1": "Payoneer fees in Pakistan explained",
    "desc": "Every Payoneer fee a Pakistani freelancer pays in 2026: receiving payments, withdrawing to PKR, the currency conversion fee, the annual account fee and transfers.",
    "lede": "Payoneer rarely shows one big fee. Instead, small charges appear at different steps. Here's each one, what it costs on a real withdrawal, and how to pay less.",
    "date": "2026-10-16", "cat": "Payments", "icon": "fx",
    "tools": ["payoneer-to-pkr-calculator", "wise-vs-payoneer-vs-bank", "fiverr-fee-calculator"],
    "body": takeaways([
        "Payoneer charges at three points: when money <strong>arrives</strong>, when it's <strong>converted to PKR</strong>, and once a year if your account is <strong>low-volume</strong>.",
        "Withdrawing to a PKR bank account costs a conversion fee — Payoneer's pricing lists a range, and around <strong>2%</strong> is typical. You see the exact rate before you confirm.",
        "Since February 2026, the <strong>$29.95 annual fee</strong> applies if your account receives less than <strong>$6,000</strong> in 12 months (where the rule applies).",
        "Fiverr's own <strong>$3 per withdrawal</strong> is separate and charged before the money reaches Payoneer.",
    ]) + '''
<h2>The short version</h2>
<div class="table-wrap"><table>
<thead><tr><th>When it happens</th><th>Fee</th></tr></thead>
<tbody>
<tr><td>Payment from a marketplace (Fiverr, Upwork…)</td><td>Depends on the marketplace — check its payout terms</td></tr>
<tr><td>Client pays you by bank transfer / ACH</td><td>1% (minimum $1)</td></tr>
<tr><td>Client pays you by card</td><td>Up to 3.99% + $0.49</td></tr>
<tr><td>Withdraw to a PKR bank account</td><td>Conversion fee, typically around 2%</td></tr>
<tr><td>Payment from another Payoneer user</td><td>Free to receive</td></tr>
<tr><td>Annual account fee</td><td>$29.95 if you receive under $6,000 in 12 months</td></tr>
</tbody></table></div>
<p class="hint">Based on Payoneer's published pricing and help centre at the time of writing. Your account's Fees page is the final word — Payoneer can set fees by country and account.</p>

<h2>1. Fees for receiving money</h2>
<h3>From Fiverr, Upwork and other marketplaces</h3>
<p>When a marketplace pays you, the marketplace usually takes its own withdrawal fee first. Fiverr, for example, deducts a flat <strong>$3 per withdrawal</strong> before the money lands in Payoneer — whether you withdraw $50 or $1,000. Payoneer says its side of marketplace payouts varies by marketplace, so check the fee shown on your Payoneer transaction.</p>
<h3>From direct clients</h3>
<p>If a client pays you through a Payoneer payment request, the fee depends on how they pay:</p>
<ul>
<li><strong>Bank transfer or US ACH:</strong> 1%, with a $1 minimum. A $500 payment costs you $5.</li>
<li><strong>Credit or debit card:</strong> up to 3.99% + $0.49. The same $500 could cost about $20.44.</li>
</ul>
<p>For direct clients, asking for a bank transfer instead of a card payment is the easiest saving in this whole article.</p>
''' + cta("fiverr-fee-calculator", "What does your Fiverr order really pay?", "See Fiverr’s 20% fee, the $3 withdrawal and your take-home in PKR.", "Open Fiverr calculator") + '''
<h2>2. The conversion fee when you withdraw to PKR</h2>
<p>This is the fee most freelancers never notice, because it isn't shown as a separate line. When you withdraw dollars to a Pakistani bank account in rupees, Payoneer converts them at its own rate, which is below the mid-market rate you see on Google. The difference is the conversion fee.</p>
<p>Payoneer's public pricing lists a range for withdrawals that involve conversion, and around <strong>2%</strong> is the commonly quoted figure for Pakistan. The good news: Payoneer shows the exact rate and rupee amount on the confirmation screen <em>before</em> you withdraw.</p>
<p class="formula">Rupees received ≈ dollars withdrawn × mid-market rate × (1 − conversion fee)</p>
''' + cta("payoneer-to-pkr-calculator", "Convert your balance to PKR", "Live mid-market rate, Payoneer’s conversion fee and the rupees that reach your bank.", "Open Payoneer to PKR") + '''
<h3>Withdrawing in dollars instead</h3>
<p>Some freelancers keep a USD account at a Pakistani bank to avoid Payoneer's conversion. Check the fee first: in 2025, Pakistani users reported a <strong>3% charge</strong> on withdrawals to non-PKR (foreign-currency) accounts and to third-party accounts. Payoneer's public pages don't list this separately, so confirm it on your account's Fees page — and remember your bank will apply its own rate when you later convert to rupees.</p>

<h2>3. The annual account fee</h2>
<p>Payoneer charges a <strong>$29.95</strong> annual account fee to low-volume accounts. From <strong>23 February 2026</strong>, in the countries where the new rule applies, the fee is charged if your account receives <strong>less than $6,000 in 12 months</strong> (the previous threshold was much lower). In other countries it applies only if the account has no transactions for 12 months.</p>
<p>If you're just starting out and receive a few hundred dollars a year, $29.95 can be a large share of your earnings — factor it in when you compare payout options.</p>

<h2>4. Payoneer-to-Payoneer transfers</h2>
<p>Receiving money from another Payoneer user is free. Sending can cost up to $4 within the same country, and up to 1% plus up to $4 to another country, according to Payoneer's pricing page. Pakistani users reported extra charges on these transfers in 2025, so check the amount shown before you send.</p>

<h2>Worked example: $1,000 from Fiverr to your bank</h2>
<div class="table-wrap"><table><tbody>
<tr><td>Withdrawn from your Fiverr balance</td><td class="num">$1,000.00</td></tr>
<tr><td>Fiverr withdrawal fee</td><td class="num">−$3.00</td></tr>
<tr><td>Arrives in Payoneer</td><td class="num">$997.00</td></tr>
<tr><td>Value at mid-market (Rs 277)</td><td class="num">Rs 2,76,169</td></tr>
<tr><td>Conversion fee (about 2%)</td><td class="num">−Rs 5,523</td></tr>
<tr><th>Reaches your bank</th><th class="num">≈ Rs 2,70,646</th></tr>
</tbody></table></div>
<p>Rates move daily; the calculators use today's rate. Your bank may also deduct tax on the remittance — see our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a> for how to keep that at 0.25%.</p>

<h2>Six ways to pay Payoneer less</h2>
<ul>
<li><strong>Withdraw in larger, less frequent amounts.</strong> Fixed fees like Fiverr's $3 shrink as a share of bigger withdrawals.</li>
<li><strong>Check the rate on the confirmation screen.</strong> If you're not in a hurry and the rate looks poor, wait a day.</li>
<li><strong>Ask direct clients for bank transfers, not cards.</strong> 1% versus up to 3.99% + $0.49.</li>
<li><strong>Know whether the annual fee applies to you.</strong> If you receive less than $6,000 a year, include $29.95 in your costs.</li>
<li><strong>Compare routes once in a while.</strong> Fees change; a quick comparison tells you whether Payoneer is still your cheapest option.</li>
<li><strong>Read the Fees page in your account.</strong> It's updated before changes take effect and is the only figure that's guaranteed for your account.</li>
</ul>
''' + cta("wise-vs-payoneer-vs-bank", "Is Payoneer still your cheapest route?", "Compare Payoneer, Wise and a bank wire side by side with your own fees.", "Compare routes") + '''
<p class="hint">Sources checked for this guide: Payoneer's pricing page and help centre (annual account fee), and reporting on Payoneer's 2025 fee changes for Pakistan by The Express Tribune. Fees can change at any time — confirm in your account before relying on them.</p>
''',
    "faq": [
        ("How much does Payoneer charge to withdraw to a Pakistani bank?", "Withdrawing in PKR costs a currency conversion fee built into the exchange rate — around 2% is typical. Payoneer shows the exact rate and rupee amount before you confirm."),
        ("What is Payoneer's annual fee in 2026?", "$29.95. Since 23 February 2026, in countries where the new rule applies, it's charged if your account receives less than $6,000 in 12 months."),
        ("Does Payoneer charge for receiving money from Fiverr?", "Fiverr deducts its own $3 per withdrawal. Payoneer says its fee for marketplace payouts varies by marketplace, so check the transaction details in your account."),
        ("Is it cheaper to withdraw in USD?", "Not always. Pakistani users reported a 3% fee on withdrawals to foreign-currency accounts in 2025, and your bank applies its own rate when you convert. Compare both before switching."),
    ],
})

# ------------------------------------------------------------------ 8
POSTS.append({
    "slug": "fiverr-vs-upwork-fees-take-home", "image": "/assets/img/blog/fiverr-vs-upwork-fees-take-home", "alt": "Glass tiles with a balance scale between a briefcase and a wallet on a dark gradient background",
    "title": "Fiverr vs Upwork Fees (2026): Which Leaves You More Money?",
    "h1": "Fiverr vs Upwork: which platform leaves you more money?",
    "desc": "Fiverr vs Upwork fees in 2026 compared on real jobs: service fees, Connects, withdrawals and payout times, plus a break-even rule for Pakistani freelancers.",
    "lede": "Fiverr takes a flat 20%. Upwork takes 0–15% but charges you to apply. Which one leaves more in your pocket depends on your job size and how many proposals you send. Here's the maths.",
    "date": "2026-10-19", "cat": "Payments", "icon": "scale",
    "tools": ["fiverr-fee-calculator", "upwork-fee-calculator", "fiverr-reverse-fee-calculator", "payoneer-to-pkr-calculator"],
    "body": takeaways([
        "Fiverr keeps a flat <strong>20%</strong> of every order and charges <strong>$3 per withdrawal</strong> (per withdrawal, not per order). Winning work costs nothing extra.",
        "Upwork keeps a <strong>variable 0–15%</strong> per contract, shown before you apply, but every proposal costs <strong>Connects</strong> at $0.15 each.",
        "On a single job Upwork's lower fee usually wins on <strong>bigger projects</strong>; Connects can make Upwork the more expensive platform on <strong>small jobs</strong>.",
        "Upwork releases money faster (5 days after a fixed-price milestone is approved) than Fiverr's 14-day clearance for most sellers.",
    ]) + '''
<h2>The fees side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Fiverr</th><th>Upwork</th></tr></thead>
<tbody>
<tr><td>Service fee on your earnings</td><td>Flat 20% (including tips and extras)</td><td>0–15%, set per contract and shown before you apply</td></tr>
<tr><td>Cost to win work</td><td>None — buyers find your gig</td><td>Connects, $0.15 each; 10 free per month on the Basic plan</td></tr>
<tr><td>Withdrawal from Pakistan</td><td>Through Payoneer, $3 per withdrawal</td><td>Direct to Local Bank (PKR) $0.99, Payoneer (small fee shown in your account) or USD wire $50</td></tr>
<tr><td>When money becomes available</td><td>14 days after completion (7 days for Seller Plus, Top Rated and Pro)</td><td>Fixed price: 5 days after milestone approval. Hourly: about 10 days after the work week ends</td></tr>
<tr><td>Optional membership</td><td>—</td><td>Freelancer Plus, $19.99/month with 100 Connects</td></tr>
</tbody></table></div>
<p class="hint">Checked on 19 October 2026 against Fiverr's and Upwork's help centres. Fees change — confirm on each platform before you rely on them.</p>
<p>Clients pay their own fees on both platforms (Fiverr buyers pay a 5.5% service fee, for example). Those don't come out of your earnings, but they do affect how price-sensitive your clients are.</p>

<h2>How Fiverr's fees work</h2>
<p>Fiverr is the simplest to calculate. Whatever the order value — $5 or $5,000 — Fiverr keeps 20% and you keep 80%. Your seller level doesn't change the rate.</p>
<p>After the order clears, you withdraw. In Pakistan, Fiverr pays out through <strong>Payoneer</strong>, and Fiverr charges a flat <strong>$3 per withdrawal</strong>, whatever the amount. Withdraw ten orders together and you pay $3 once, not ten times. Payoneer then converts your dollars to rupees at a rate typically around 2% below mid-market — see our <a href="/blog/payoneer-fees-pakistan/">Payoneer fees guide</a>.</p>
<p class="formula">Fiverr take-home = order value × 0.80 − $3 per withdrawal</p>
''' + cta("fiverr-fee-calculator", "Check a Fiverr order", "Enter your gig price to see the 20% fee, the $3 withdrawal and your take-home in PKR.", "Open Fiverr calculator") + '''
<h2>How Upwork's fees work</h2>
<p>Since May 2025, Upwork charges a <strong>variable freelancer service fee between 0% and 15%</strong>. The rate depends on factors such as the job and your history with the client. Upwork shows it before you submit a proposal, and it stays fixed for that contract, bonuses included.</p>
<p>The cost Fiverr doesn't have is <strong>Connects</strong>. Every proposal uses some, the number is shown on each job post, and they cost $0.15 each (sold in bundles of at least 10). Basic accounts get 10 free Connects a month; Freelancer Plus costs $19.99 a month and includes 100.</p>
<p>Withdrawing to Pakistan is cheap: Upwork's <strong>Direct to Local Bank</strong> option supports PKR accounts for $0.99 per withdrawal (personal accounts only — Upwork says it can't accept company registrations for PKR accounts). You can also withdraw to Payoneer, or by USD wire for $50. Upwork's banking provider sets the PKR exchange rate and doesn't publish its margin, so compare the quoted rupee amount with the mid-market rate before confirming.</p>
<p class="formula">Upwork take-home = payment × (1 − service fee) − Connects spent × $0.15 − withdrawal fee</p>

<h2>Worked example: a $500 project</h2>
<p>Assume you send 10 proposals at 15 Connects each to win one $500 job on Upwork. That's 150 Connects, or <strong>$22.50</strong>. On Fiverr, assume the order came to your gig and you withdraw it on its own.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th class="num">Fiverr</th><th class="num">Upwork at 10%</th><th class="num">Upwork at 15%</th></tr></thead>
<tbody>
<tr><td>Job value</td><td class="num">$500.00</td><td class="num">$500.00</td><td class="num">$500.00</td></tr>
<tr><td>Service fee</td><td class="num">−$100.00</td><td class="num">−$50.00</td><td class="num">−$75.00</td></tr>
<tr><td>Cost to win the job</td><td class="num">$0.00</td><td class="num">−$22.50</td><td class="num">−$22.50</td></tr>
<tr><td>Withdrawal</td><td class="num">−$3.00</td><td class="num">−$0.99</td><td class="num">−$0.99</td></tr>
<tr><th>You keep (before conversion)</th><th class="num">$397.00</th><th class="num">$426.51</th><th class="num">$401.51</th></tr>
</tbody></table></div>
<p>At a 10% fee, Upwork leaves you about $30 more. At 15%, the gap almost disappears. Your own numbers will differ — the Connects figure is an example, not an average.</p>

<h2>Worked example: a $50 job</h2>
<p>Small jobs flip the result. With the same 150 Connects spent to win a $50 job:</p>
<ul>
<li><strong>Fiverr:</strong> $50 − $10 fee − $3 withdrawal = <strong>$37.00</strong> (and less than $3 of fee per order if you batch withdrawals).</li>
<li><strong>Upwork at 10%:</strong> $50 − $5 fee − $22.50 Connects − $0.99 = <strong>$21.51</strong>.</li>
</ul>
<p>The fee rate matters less than the cost of winning the work. That's why many freelancers use Upwork for larger projects and Fiverr for small, repeatable services.</p>
''' + cta("upwork-fee-calculator", "Check an Upwork contract", "Set the service fee shown on the job, add your Connects and withdrawal method, and see your take-home.", "Open Upwork calculator") + '''
<h2>A simple break-even rule</h2>
<p>Upwork leaves you more than Fiverr on a job when:</p>
<p class="formula">job value × (20% − Upwork fee) &gt; Connects cost + Upwork withdrawal fee − $3</p>
<p>With $22.50 of Connects and a $0.99 withdrawal, that works out to:</p>
<div class="table-wrap"><table>
<thead><tr><th>Upwork service fee</th><th class="num">Upwork wins above about</th></tr></thead>
<tbody>
<tr><td>5%</td><td class="num">$137</td></tr>
<tr><td>10%</td><td class="num">$205</td></tr>
<tr><td>15%</td><td class="num">$410</td></tr>
</tbody></table></div>
<p>Spend fewer Connects per win — because your proposals are sharper — and those thresholds fall fast. Our guide to <a href="/blog/how-to-write-upwork-proposal/">writing Upwork proposals that get replies</a> helps with exactly that.</p>

<h2>It's not only about fees</h2>
<ul>
<li><strong>Cash flow.</strong> Upwork's 5-day security period on fixed-price milestones gets money to you faster than Fiverr's 14-day clearance, unless you're Seller Plus, Top Rated or Pro on Fiverr (7 days).</li>
<li><strong>Effort to get work.</strong> On Fiverr, buyers come to your gig, so your time goes into gig SEO and delivery. On Upwork, you spend time writing proposals — time that has a cost even when the Connects are free.</li>
<li><strong>Project size.</strong> Long, custom or hourly projects fit Upwork's contract model. Packaged, fixed-scope services fit Fiverr's gig model.</li>
<li><strong>Exchange rate.</strong> Fiverr money reaches you through Payoneer's rate; Upwork's Direct to Local Bank uses its provider's rate. Compare the rupee amount each one quotes for the same dollars.</li>
</ul>
''' + cta("fiverr-reverse-fee-calculator", "Price to keep what you need", "Work back from the amount you want to keep to the price you should quote on either platform.", "Open reverse calculator") + '''
<h2>So which one should you choose?</h2>
<p>If most of your work is under about $200 and buyers can order it as a package, Fiverr usually leaves you more money and less admin. If you take on larger custom projects, or you can win work with few proposals, Upwork's lower fee usually wins. Plenty of freelancers run both: the fees are only one part of the decision, and both platforms let you raise your price to cover them.</p>
<p class="hint">Sources checked for this guide: Fiverr Help Center (order process and clearance, buyer service fees), Upwork Help Center (how to get paid, Direct to Local Bank fees, wire transfers, Payoneer withdrawals) and Upwork's pricing page. The $3 per-withdrawal Fiverr fee in Pakistan is as confirmed for this site. Fees can change at any time.</p>
''',
    "faq": [
        ("Does Fiverr or Upwork take a bigger cut?", "Fiverr takes a flat 20%. Upwork takes 0–15% depending on the contract, but you also pay for Connects to send proposals, so on small jobs Upwork can cost more overall."),
        ("How much does it cost to withdraw from Upwork to Pakistan?", "Direct to Local Bank to a personal PKR account costs $0.99 per withdrawal. A USD wire costs $50. Payoneer withdrawals carry a small Upwork fee shown in your account, plus Payoneer's conversion."),
        ("Is the Fiverr $3 withdrawal fee charged on every order?", "No. It's $3 per withdrawal, whatever the amount. Withdrawing several orders together means you pay it once."),
        ("Which platform pays faster?", "Upwork releases fixed-price earnings five days after the client approves a milestone. Fiverr holds earnings for 14 days after an order completes, or 7 days for Seller Plus, Top Rated and Pro sellers."),
        ("Are Upwork Connects worth buying?", "Only if your proposals win often enough. Divide the Connects you spend by the jobs you win to find your real cost per job, and include it when you compare platforms."),
    ],
})

# =================================================================== SCHEDULED QUEUE (written 2026-10-20)
# Each post goes live automatically on its date (GitHub Actions rebuilds daily).

# ------------------------------------------------------------------ 2026-10-22
POSTS.append({
    "slug": "file-income-tax-return-freelancer-pakistan", "image": "/assets/img/blog/file-income-tax-return-freelancer-pakistan",
    "alt": "Glass tiles with a document, a landmark and a calendar icon on a dark gradient background",
    "title": "How to File Your Tax Return as a Freelancer in Pakistan (IRIS Guide)",
    "h1": "How to file your tax return as a freelancer in Pakistan",
    "desc": "A plain-language guide for Pakistani freelancers: why filing matters, documents to gather, filing your return and wealth statement on FBR IRIS, deadlines and late-filing costs.",
    "lede": "Filing once a year is what unlocks the low final tax on your foreign earnings and keeps you on the Active Taxpayers List. Here's the whole process, start to finish.",
    "date": "2026-10-22", "cat": "Tax", "icon": "doc",
    "tools": ["pakistan-freelancer-tax-calculator", "payoneer-to-pkr-calculator", "invoice-generator"],
    "body": takeaways([
        "Filing your return is what keeps you on the <strong>Active Taxpayers List (ATL)</strong> — and the reduced 0.25% / 1% final tax on IT exports depends on it.",
        "The tax year runs <strong>1 July to 30 June</strong>. Returns are normally due by <strong>30 September</strong>.",
        "You file two things on FBR's IRIS portal: the <strong>return of income</strong> and the <strong>wealth statement</strong>.",
        "Filing late now costs more: from tax year 2026, joining the ATL late carries a <strong>Rs 25,000</strong> surcharge.",
    ]) + '''
<h2>Why filing matters for freelancers</h2>
<p>Many freelancers assume that because their bank already deducts tax on foreign remittances, there's nothing else to do. That's the most expensive misunderstanding in Pakistani freelancing.</p>
<ul>
<li><strong>The low rate depends on it.</strong> Export earnings from IT and IT-enabled services can be taxed under the final tax regime — 0.25% with PSEB registration, 1% without — but only if you file your return and meet the other conditions. Our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a> explains the rates.</li>
<li><strong>Non-filers pay more everywhere.</strong> People not on the ATL face higher withholding tax on many transactions, from bank withdrawals to property and vehicles.</li>
<li><strong>Your income becomes provable.</strong> A filed return, bank statements and PRCs together show where your money came from — useful for visas, loans and large purchases.</li>
</ul>
''' + cta("pakistan-freelancer-tax-calculator", "How much tax will you pay?", "See your tax at 0.25% (PSEB) and 1% on a year of foreign income.", "Open tax calculator") + '''
<h2>Key dates</h2>
<div class="table-wrap"><table><tbody>
<tr><td>Tax year</td><td>1 July – 30 June (tax year 2026 = July 2025 to June 2026)</td></tr>
<tr><td>Normal filing deadline</td><td>30 September after the tax year ends</td></tr>
<tr><td>Extensions</td><td>The government sometimes extends the deadline — but don't plan around it</td></tr>
</tbody></table></div>

<h2>Before you start: what to gather</h2>
<ul>
<li><strong>CNIC</strong>, and a <strong>mobile number and email</strong> registered in your own name (IRIS sends codes to both).</li>
<li><strong>Bank statements</strong> for the full tax year, for every account.</li>
<li><strong>Payoneer (or other provider) statements</strong> showing what you received and withdrew.</li>
<li><strong>PRCs</strong> — the bank's Proceeds Realisation Certificates for your foreign remittances.</li>
<li><strong>Tax deduction certificates</strong> — the tax your bank withheld on remittances or other transactions.</li>
<li><strong>Invoices or platform earnings reports</strong> that match your remittances.</li>
<li><strong>Details of assets and liabilities</strong> on 30 June: bank balances, cash, property, vehicles, loans — needed for the wealth statement.</li>
</ul>

<h2>Step 1: Register on IRIS (first time only)</h2>
<p>If you've never filed, register as a taxpayer on FBR's IRIS portal with your CNIC. Your CNIC number becomes your NTN as an individual. You'll verify your mobile number and email with one-time codes and set a password.</p>

<h2>Step 2: Open the return for the right tax year</h2>
<p>Log in, start a new <strong>return of income</strong> for the individual and choose the correct tax year — tax year 2026 for income earned from July 2025 to June 2026. IRIS menus change between versions, so look for the option to file the annual return for individuals.</p>

<h2>Step 3: Declare your freelance income</h2>
<ul>
<li>Declare your foreign freelance earnings as <strong>export of IT / IT-enabled services</strong>, so they fall under the final tax regime rather than normal slab rates.</li>
<li>Use the <strong>PKR amounts</strong> your bank credited, which match your PRCs.</li>
<li>Declare any other income separately — a salary, local clients, profit on savings.</li>
</ul>

<h2>Step 4: Enter the tax already deducted</h2>
<p>Add the tax your bank withheld on your remittances (and any other withholding taxes) in the tax deductions or adjustable / final tax section. Your bank's tax certificate shows these amounts. If the tax already deducted equals the final tax on that income, there's usually nothing extra to pay on it.</p>

<h2>Step 5: Complete the wealth statement</h2>
<p>Every individual who files must also submit a <strong>wealth statement</strong>: your assets and liabilities on 30 June, and a reconciliation showing how your wealth changed during the year (income in, personal expenses out). Your net assets at the end should be explained by last year's figure plus your income minus your spending.</p>
<p>Take care here. Unexplained increases in wealth are the most common reason for questions from FBR.</p>

<h2>Step 6: Submit and keep the acknowledgement</h2>
<p>Review everything, submit both the return and the wealth statement, and save the acknowledgement receipt. Your name should appear on the ATL once FBR updates the list.</p>
''' + cta("payoneer-to-pkr-calculator", "Check your rupee figures", "Convert your Payoneer withdrawals to PKR at the day’s rate to sanity-check your records.", "Open Payoneer to PKR") + '''
<h2>What happens if you file late</h2>
<p>From tax year 2026, an individual who files after the deadline and wants to be on the ATL faces a <strong>Rs 25,000 surcharge</strong> — up from Rs 1,000 before. In October 2026 FBR published a draft rule that would let late filers join the ATL without the surcharge by signing an undertaking not to buy property for six months; at the time of writing it was a proposal, not law. Either way, filing on time is far cheaper.</p>

<h2>Mistakes to avoid</h2>
<ul>
<li><strong>Declaring export income as ordinary business income</strong> — it can push you onto slab rates.</li>
<li><strong>Using dollar figures instead of the PKR amounts</strong> your bank actually credited.</li>
<li><strong>Skipping the wealth statement</strong> or leaving the reconciliation unbalanced.</li>
<li><strong>Losing PRCs</strong> — request them as you go, not in September.</li>
<li><strong>Waiting until the last week</strong> — IRIS is slowest just before the deadline.</li>
</ul>
<p>If your situation is more complex — several income sources, property, a registered business — a tax practitioner is worth the fee.</p>
<p class="hint">General information based on rules published for tax year 2026, not tax advice. Procedures and rates change with each budget; confirm with FBR or a tax practitioner. Sources checked: FBR guidance via IRIS, reporting by ProPakistani on the Rs 25,000 ATL surcharge (June 2026) and FBR's draft Rule 81B amendment (October 2026).</p>
''',
    "faq": [
        ("When is the deadline to file a tax return in Pakistan?", "Normally 30 September after the tax year ends (the tax year runs July to June). The government sometimes extends it, but you shouldn't rely on that."),
        ("Do freelancers need to file a return if the bank already deducted tax?", "Yes. Filing keeps you on the Active Taxpayers List, and the reduced final tax on IT exports depends on it."),
        ("What is the penalty for filing late?", "From tax year 2026, joining the ATL after filing late carries a Rs 25,000 surcharge. FBR has proposed an alternative undertaking route, but it wasn't in force at the time of writing."),
        ("Do I need to file a wealth statement?", "Yes. Individuals filing a return also submit a wealth statement listing assets and liabilities on 30 June, with a reconciliation of how wealth changed during the year."),
    ],
})

# ------------------------------------------------------------------ 2026-10-25
POSTS.append({
    "slug": "prc-proceeds-realisation-certificate-pakistan", "image": "/assets/img/blog/prc-proceeds-realisation-certificate-pakistan",
    "alt": "Glass tiles with a file-check document, a bank and a stamp icon on a dark gradient background",
    "title": "PRC for Freelancers in Pakistan: What It Is and How to Get One",
    "h1": "PRC for freelancers in Pakistan: what it is and how to get one",
    "desc": "What a Proceeds Realisation Certificate (PRC) is, why Pakistani freelancers need one for every foreign payment, what it shows, and how to request it from your bank or app.",
    "lede": "A small bank document does a big job: it proves your foreign income is IT export income. Here's what a PRC shows, why it matters at tax time, and how to collect them without stress.",
    "date": "2026-10-25", "cat": "Tax", "icon": "doc",
    "tools": ["pakistan-freelancer-tax-calculator", "payoneer-to-pkr-calculator", "invoice-generator"],
    "body": takeaways([
        "A <strong>PRC (Proceeds Realisation Certificate)</strong> is issued by your Pakistani bank and confirms that foreign currency arrived and was converted to rupees through official channels.",
        "It records the <strong>purpose code</strong> — and the code decides whether the payment is treated as an IT services export.",
        "PRCs are your main evidence for the reduced <strong>0.25% / 1%</strong> final tax on freelance export income.",
        "Request them as payments arrive, not in September. Some banks and apps issue them automatically; others need a request.",
    ]) + '''
<h2>What a PRC is</h2>
<p>When money from abroad lands in your Pakistani account — a Payoneer withdrawal, a direct wire from a client — your bank processes it as an inward remittance. A <strong>Proceeds Realisation Certificate</strong> is the bank's official confirmation of that remittance: who received it, how much arrived in foreign currency, what it became in rupees, on what date, and for what purpose.</p>
<p>You'll sometimes see it called a “remittance certificate”. The name matters less than what's on it.</p>

<h2>What's on it — and why the purpose code matters</h2>
<p>A PRC typically shows:</p>
<ul>
<li>Your name and account number (the beneficiary)</li>
<li>The amount in foreign currency and the amount credited in PKR</li>
<li>The date the funds were credited and a transaction reference</li>
<li>The <strong>purpose code</strong> — the State Bank category the payment was recorded under</li>
</ul>
<p>The purpose code is the important part. A payment recorded as an <strong>export of computer / IT-enabled services</strong> supports the reduced final tax for freelancers. Payment providers commonly cite code <strong>9186</strong> for IT and ITeS exports. A payment recorded as a <strong>home remittance</strong> (money from family abroad) doesn't carry the same treatment.</p>
''' + cta("pakistan-freelancer-tax-calculator", "What will the tax be?", "Estimate tax on your remittances at 0.25% or 1%.", "Open tax calculator") + '''
<h2>Why freelancers need PRCs</h2>
<ul>
<li><strong>They prove export income.</strong> When you file your return, PRCs back up the figures you declare as IT export income. Our <a href="/blog/file-income-tax-return-freelancer-pakistan/">tax return guide</a> shows where that income goes.</li>
<li><strong>They match your records.</strong> Each PRC lines up with an invoice or platform earnings report, so your income story is consistent.</li>
<li><strong>They protect the low rate.</strong> Without evidence that income is IT export, it can end up taxed at normal slab rates.</li>
<li><strong>They help with PSEB renewal.</strong> Renewal asks for a summary of your export revenue; PRCs are the easiest source.</li>
</ul>

<h2>How to get a PRC</h2>
<p>Every bank and app handles this a little differently. The common routes are:</p>
<ol>
<li><strong>Automatic e-PRC.</strong> Some banks email or show an electronic PRC soon after the remittance arrives. Check your email and the bank app first.</li>
<li><strong>Request in the app or by email.</strong> Digital banks often take PRC requests through in-app chat. SadaPay, for example, asks for the beneficiary name, account number, bank, PKR and foreign-currency amounts, credit date, transfer number and purpose code, and says to allow up to three working days. It charges a small fee for transactions more than a year old.</li>
<li><strong>Branch visit.</strong> Some banks issue PRCs only at the branch, which can take a week or more. Bring your CNIC and the transaction details.</li>
</ol>
''' + cta("payoneer-to-pkr-calculator", "Know what should arrive", "Convert your Payoneer withdrawal to PKR so you can check the credited amount on your PRC.", "Open Payoneer to PKR") + '''
<h2>If the purpose code is wrong</h2>
<p>If your freelance payment was recorded as a home remittance or a general transfer, contact your bank quickly and ask whether it can be corrected. The longer you wait, the harder it gets. To prevent it:</p>
<ul>
<li>Tell your bank you're a freelancer receiving <strong>IT / IT-enabled service export</strong> payments.</li>
<li>Consider a <strong>freelancer digital account</strong> or an exporter's foreign currency account, which banks offer specifically for export proceeds.</li>
<li>Check the first PRC from any new payment route before relying on it.</li>
</ul>

<h2>A simple monthly routine</h2>
<ol>
<li>At the end of each month, list every foreign payment that arrived.</li>
<li>Download or request a PRC for each one.</li>
<li>Save it next to the matching <a href="/invoice-generator/">invoice</a> or platform report, named by date.</li>
<li>Note the PKR amount and tax deducted in a simple sheet — your tax return will thank you.</li>
</ol>
<p class="hint">General information, not tax advice. Bank procedures vary; ask your bank for its PRC process. Sources checked: SadaPay help centre (remittance certificate requests), Elevate Pay's guide to PRCs and purpose codes, and State Bank of Pakistan publications.</p>
''',
    "faq": [
        ("What does PRC stand for?", "Proceeds Realisation Certificate — the bank's confirmation that foreign currency was received and converted to rupees through official channels."),
        ("Do I need a PRC for every payment?", "It's best to have one for every foreign remittance you declare as export income. Together they back up the income on your tax return."),
        ("Which purpose code should a freelance payment have?", "It should be recorded as an export of IT or IT-enabled services. Payment providers commonly cite purpose code 9186 for this."),
        ("How long does it take to get a PRC?", "Some banks issue e-PRCs automatically. Others take a few working days through the app, or longer if you need a branch visit."),
    ],
})

# ------------------------------------------------------------------ 2026-10-28
POSTS.append({
    "slug": "how-to-get-first-order-on-fiverr", "image": "/assets/img/blog/how-to-get-first-order-on-fiverr",
    "alt": "Glass tiles with a rocket, a star and a message icon on a dark gradient background",
    "title": "How to Get Your First Order on Fiverr: A Practical 2026 Checklist",
    "h1": "How to get your first order on Fiverr",
    "desc": "A practical checklist for new Fiverr sellers: choose a narrow gig, write a title buyers search for, price to win, answer fast and deliver so well your first review sells the next order.",
    "lede": "The first order is the hardest one. Once you have a review, buyers trust you more and Fiverr shows your gig more. Here's how to get that first one without gaming the system.",
    "date": "2026-10-28", "cat": "Fiverr", "icon": "spark",
    "tools": ["fiverr-gig-character-counter", "fiverr-gig-image-resizer", "fiverr-profile-bio-generator", "fiverr-reverse-fee-calculator"],
    "body": takeaways([
        "Go <strong>narrow</strong>: a specific gig beats a general one when you have no reviews.",
        "Write the title around words buyers <strong>actually search</strong> for.",
        "Price to win the first few orders — but never below your floor after Fiverr's 20%.",
        "Reply fast, deliver early, and over-communicate. Your first review is your best marketing.",
    ]) + '''
<h2>Why the first order is so hard</h2>
<p>Buyers on Fiverr choose between dozens of gigs that look similar. With no reviews, you have no proof — so everything else on your gig has to work harder: the title, the image, the price, the packages and how quickly you reply. The steps below fix each one.</p>

<h2>1. Pick a narrow service</h2>
<p>“I will do web development” competes with thousands of established sellers. “I will fix WordPress speed issues and pass Core Web Vitals” competes with far fewer — and buyers searching for that exact problem find you.</p>
<ul>
<li>Choose one problem you can solve well and quickly.</li>
<li>Search it on Fiverr. If the first page is full of sellers with thousands of reviews, go one step narrower.</li>
<li>Create one gig per service rather than one gig for everything.</li>
</ul>

<h2>2. Write a title and description buyers search for</h2>
<p>Type your service into Fiverr's search bar and note the suggestions — they come from real searches. Put the main phrase early in your title, within the 80-character limit, and use the 1,200-character description to explain exactly what's included. Our <a href="/blog/fiverr-gig-seo-guide/">gig SEO guide</a> covers this step by step.</p>
''' + cta("fiverr-gig-character-counter", "Check your gig text", "Character counts against Fiverr’s limits, keyword checks and contact-info warnings.", "Open gig counter") + '''
<h2>3. Make the gig image do the selling</h2>
<p>Your image is the first thing buyers see in search. Show the result — a finished site, a before-and-after, a mock-up — at Fiverr's recommended <strong>1280 × 769 px</strong>, with a few large words at most.</p>
''' + cta("fiverr-gig-image-resizer", "Resize your gig image", "Crop any image to exactly 1280 × 769 px in your browser.", "Open image resizer") + '''
<h2>4. Price to win — without working for free</h2>
<p>A slightly lower starting price helps you win the first few orders. But remember Fiverr keeps 20%: a $10 gig pays you $8. Work out the lowest price that still pays you fairly, start there, and raise prices after five to ten good reviews.</p>
<ul>
<li>Make <strong>Basic</strong> a small, fast job — easy to say yes to.</li>
<li>Make <strong>Standard</strong> your real offer.</li>
<li>Add gig extras (faster delivery, extra revision) to lift the order value.</li>
</ul>
''' + cta("fiverr-reverse-fee-calculator", "Find your minimum price", "Work back from what you want to keep to the price you should list.", "Open reverse calculator") + '''
<h2>5. Complete your profile</h2>
<p>Buyers check your profile before ordering a new seller. Use a clear photo of yourself, list your skills, and write a short description that says what you do, who you help and one result you've achieved.</p>
''' + cta("fiverr-profile-bio-generator", "Write your profile", "Generate a focused Fiverr description in the tone you want.", "Open bio generator") + '''
<h2>6. Reply fast and be available</h2>
<p>New sellers win orders in the inbox. Reply to messages quickly, ask one or two smart questions about the buyer's project, and send a <strong>custom offer</strong> when the request doesn't fit your packages. Keep the Fiverr app on your phone so you see messages promptly.</p>

<h2>7. Share your gig outside Fiverr</h2>
<p>Share your gig link on your LinkedIn, in relevant groups where self-promotion is allowed, and with past clients or contacts. One real buyer from outside Fiverr can give you the first review that unlocks the rest.</p>

<h2>8. Deliver an outstanding first order</h2>
<ul>
<li>Confirm the requirements in writing before you start.</li>
<li>Send a short progress update.</li>
<li>Deliver early if you can, and explain what you did.</li>
<li>Politely ask the buyer to leave a review if they're happy.</li>
</ul>

<h2>What not to do</h2>
<ul>
<li><strong>Don't buy fake reviews or orders.</strong> It breaks Fiverr's rules and can get your account removed.</li>
<li><strong>Don't share contact details</strong> or ask to move the conversation off Fiverr.</li>
<li><strong>Don't copy other sellers' descriptions or images.</strong></li>
<li><strong>Don't keep changing your gig every day.</strong> Give changes a week or two to show results.</li>
</ul>
''',
    "faq": [
        ("How long does it take to get the first order on Fiverr?", "It varies widely by niche and gig quality. A narrow gig, a strong image and fast replies shorten the wait more than anything else."),
        ("Should I lower my price to get the first order?", "A slightly lower starting price helps, but stay above your minimum after Fiverr's 20% fee and raise prices once you have reviews."),
        ("Can I share my Fiverr gig on social media?", "Yes. Sharing your gig link is allowed and can bring your first buyers. Just don't ask buyers to pay you outside Fiverr."),
    ],
})

# ------------------------------------------------------------------ 2026-10-31
POSTS.append({
    "slug": "upwork-connects-explained", "image": "/assets/img/blog/upwork-connects-explained",
    "alt": "Glass tiles with a ticket, coins and a send icon on a dark gradient background",
    "title": "Upwork Connects Explained: What They Cost and How to Spend Them",
    "h1": "Upwork Connects explained: what they cost and how to spend them",
    "desc": "How Upwork Connects work: the $0.15 price, how many a proposal costs, boosted proposals, free monthly Connects, refunds, and a simple way to spend fewer Connects per job won.",
    "lede": "Every Upwork proposal costs Connects, and Connects cost money. Treat them like an ad budget and you'll win more work for less.",
    "date": "2026-10-31", "cat": "Upwork", "icon": "send",
    "tools": ["upwork-fee-calculator", "upwork-proposal-generator", "fixed-price-vs-hourly-calculator"],
    "body": takeaways([
        "Connects cost <strong>$0.15 each</strong>. The number a proposal needs is shown on each job before you apply.",
        "<strong>Boosted proposals</strong> let you bid extra Connects for a higher spot in the client's list.",
        "Connects are refunded in limited cases, such as when a client closes a job without hiring.",
        "Track your <strong>cost per job won</strong>, not cost per proposal.",
    ]) + '''
<h2>What Connects are</h2>
<p>Connects are Upwork's tokens for applying to jobs. Each proposal you send costs a number of Connects, which Upwork shows on the job post before you apply. You can buy more at <strong>$0.15 each</strong>, and some plans include a monthly allowance.</p>
<p>That makes every proposal a small investment. A proposal that costs 16 Connects is $2.40 — trivial once, but real when you send dozens a week.</p>

<h2>How many Connects a proposal costs</h2>
<p>The cost varies by job. Upwork sets it per posting, taking into account things like the job's size and type. Always check the number before writing your proposal, and ask yourself whether this job is worth that spend.</p>

<h2>Boosted proposals</h2>
<p>When you apply, you can choose to <strong>boost</strong> your proposal by bidding extra Connects. The highest bids are shown at the top of the client's proposal list. If you're outbid, you only spend the Connects for a normal proposal.</p>
<ul>
<li>Boost selectively — on jobs that are a strong fit and worth enough to justify the extra cost.</li>
<li>Boosting doesn't fix a weak proposal. The first two lines still decide whether the client opens it.</li>
</ul>
''' + cta("upwork-proposal-generator", "Write a proposal worth the Connects", "Answer the brief, show proof, give a plan and ask one smart question.", "Open proposal generator") + '''
<h2>Free and included Connects</h2>
<p>Upwork gives freelancers some Connects without buying them — for example a monthly allowance on the basic plan, extra Connects with paid membership plans and as rewards for strong profiles. Amounts and plan prices change, so check the Membership & Connects page in your account for your current allowance.</p>

<h2>When Connects are refunded</h2>
<p>Connects are generally returned if the client closes the job without hiring anyone, or if Upwork removes the job. They're not returned just because another freelancer was hired. Applying to a job you were invited to doesn't cost Connects.</p>

<h2>The number that matters: cost per job won</h2>
<p>Instead of worrying about each proposal, measure what it costs you to win a job:</p>
<p class="formula">Cost per win = (Connects spent ÷ jobs won) × $0.15</p>
<p>If you spend 160 Connects to win one job, that job cost you $24 in Connects — on top of Upwork's service fee. Include both when you decide what to charge.</p>
''' + cta("upwork-fee-calculator", "What will you take home?", "Include the job’s service fee and the Connects you spent.", "Open Upwork calculator") + '''
<h2>Seven ways to spend fewer Connects per win</h2>
<ol>
<li><strong>Apply early.</strong> Jobs posted in the last hour or two have fewer proposals competing.</li>
<li><strong>Read the client's history.</strong> Payment verified, past hires and fair reviews mean a real chance of hiring.</li>
<li><strong>Skip vague posts.</strong> One-line briefs with no budget rarely lead to hires.</li>
<li><strong>Answer the client's questions</strong> in your first lines.</li>
<li><strong>Specialise.</strong> Fewer, better-matched proposals win more often.</li>
<li><strong>Boost only when it's worth it.</strong></li>
<li><strong>Reuse structure, not text.</strong> A <a href="/blog/how-to-write-upwork-proposal/">proven proposal structure</a> saves time without sounding copy-pasted.</li>
</ol>
<p>Comparing platforms? See how Upwork's costs stack up in our <a href="/blog/fiverr-vs-upwork-fees-take-home/">Fiverr vs Upwork fees guide</a>.</p>
<p class="hint">Sources checked: Upwork's help pages on Connects and boosted proposals, and Upwork's pricing pages. Plan prices and allowances change — check your account for current figures.</p>
''',
    "faq": [
        ("How much do Upwork Connects cost?", "$0.15 each when you buy them. Some membership plans include a monthly allowance."),
        ("How many Connects does a proposal cost?", "It varies by job. Upwork shows the number on each job post before you apply."),
        ("Do I get my Connects back if I'm not hired?", "Generally only if the client closes the job without hiring anyone or Upwork removes the job — not when another freelancer is hired."),
        ("Is boosting a proposal worth it?", "Sometimes. Boost on high-value jobs that fit you well; for most jobs, a strong early proposal matters more."),
    ],
})

# ------------------------------------------------------------------ 2026-11-03
POSTS.append({
    "slug": "fiverr-seller-levels-explained", "image": "/assets/img/blog/fiverr-seller-levels-explained",
    "alt": "Glass tiles with a trophy, a star and a trending-up icon on a dark gradient background",
    "title": "Fiverr Seller Levels Explained: Requirements and How to Level Up",
    "h1": "Fiverr seller levels explained",
    "desc": "Fiverr's seller levels — Level 1, Level 2 and Top Rated: the success score, rating, orders, buyers and earnings each needs, what you gain, and practical ways to level up faster.",
    "lede": "Levels bring more gig slots, more trust and, at the top, faster access to your money. Here's what each level asks for and what actually moves the numbers.",
    "date": "2026-11-03", "cat": "Fiverr", "icon": "spark",
    "tools": ["fiverr-fee-calculator", "fiverr-gig-character-counter", "fiverr-profile-bio-generator"],
    "body": takeaways([
        "Fiverr has three levels above new seller: <strong>Level 1, Level 2 and Top Rated</strong>. Top Rated also needs a manual review.",
        "Each level has minimums for <strong>success score, rating, response rate, completed orders, unique buyers and earnings</strong>.",
        "The <strong>success score</strong> reflects buyer satisfaction and order outcomes — not just your star rating.",
        "Fiverr can change thresholds. Your <strong>Levels page</strong> in Fiverr shows exactly where you stand.",
    ]) + '''
<h2>The levels at a glance</h2>
<p>These are the requirements Fiverr's help centre lists at the time of writing. Fiverr updates its level system from time to time, so treat your own Levels dashboard as the final word.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th class="num">Level 1</th><th class="num">Level 2</th><th class="num">Top Rated</th></tr></thead>
<tbody>
<tr><td>Success score</td><td class="num">5+</td><td class="num">7+</td><td class="num">9+</td></tr>
<tr><td>Rating</td><td class="num">4.4+</td><td class="num">4.6+</td><td class="num">4.7+</td></tr>
<tr><td>Response rate</td><td class="num">80%</td><td class="num">90%</td><td class="num">90%</td></tr>
<tr><td>Completed orders</td><td class="num">5</td><td class="num">20</td><td class="num">40</td></tr>
<tr><td>Unique buyers</td><td class="num">3</td><td class="num">10</td><td class="num">20</td></tr>
<tr><td>Earnings</td><td class="num">$400</td><td class="num">$2,000</td><td class="num">$10,000</td></tr>
<tr><td>Manual review</td><td class="num">No</td><td class="num">No</td><td class="num">Yes</td></tr>
</tbody></table></div>

<h2>What the success score is</h2>
<p>The success score is Fiverr's measure of how well your orders go, on a scale up to 10. It looks beyond star ratings at things like buyer satisfaction, communication, order cancellations and how orders conclude. A seller with a 4.9 rating but frequent cancellations can still have a low score.</p>

<h2>What each level gets you</h2>
<ul>
<li><strong>More active gigs and gig extras</strong>, so you can cover more services and raise order values.</li>
<li><strong>More trust in search results</strong> — a badge buyers recognise.</li>
<li><strong>Faster access to earnings at the top.</strong> Top Rated sellers' earnings clear in 7 days instead of the usual 14.</li>
<li><strong>Better support</strong> at higher levels.</li>
</ul>
''' + cta("fiverr-fee-calculator", "See what your orders really pay", "Fiverr’s 20% fee, the $3 withdrawal and your take-home in PKR.", "Open Fiverr calculator") + '''
<h2>How to level up faster</h2>
<h3>Protect your success score</h3>
<ul>
<li><strong>Clarify requirements before you start.</strong> Most cancellations and bad reviews come from mismatched expectations.</li>
<li><strong>Don't accept orders you can't deliver well.</strong> Politely decline or suggest a custom offer instead.</li>
<li><strong>Send updates</strong> on longer orders so buyers never wonder what's happening.</li>
<li><strong>Resolve issues in the conversation</strong> before they become disputes.</li>
</ul>
<h3>Hit the order and buyer counts</h3>
<ul>
<li>Offer a small, fast <strong>Basic</strong> package that new buyers can say yes to easily.</li>
<li>Unique buyers matter: repeat orders from one client help your earnings but count as one buyer.</li>
</ul>
<h3>Keep your response rate high</h3>
<ul>
<li>Reply to every new message within 24 hours — even a short “thanks, I'll review this today” counts.</li>
<li>Use the Fiverr mobile app so messages don't wait until you're at your desk.</li>
</ul>
<h3>Grow earnings, not just order count</h3>
<ul>
<li>Use Standard and Premium packages and gig extras to raise the average order.</li>
<li>Write gigs buyers can find — see our <a href="/blog/fiverr-gig-seo-guide/">gig SEO guide</a>.</li>
</ul>
''' + cta("fiverr-gig-character-counter", "Tune your gig text", "Check titles, descriptions and tags against Fiverr’s limits.", "Open gig counter") + '''
<h2>If you drop a level</h2>
<p>Levels are reviewed regularly, and falling below a requirement can move you down. Don't panic: look at which metric slipped on your Levels page, fix the cause (often response time or a run of cancellations), and focus on a few smooth orders.</p>
<p class="hint">Requirements as listed in Fiverr's help centre article “Understanding Fiverr's freelancer levels” at the time of writing. Fiverr may change them — check your Levels page.</p>
''',
    "faq": [
        ("How many orders do I need for Level 1 on Fiverr?", "Fiverr's help centre lists 5 completed orders from at least 3 unique buyers and $400 in earnings, along with a success score of 5+, a 4.4+ rating and an 80% response rate."),
        ("How do I become Top Rated on Fiverr?", "Meet the Top Rated thresholds — including a 9+ success score, 40 orders, 20 unique buyers and $10,000 in earnings — and pass Fiverr's manual review."),
        ("Do higher levels pay lower Fiverr fees?", "No. The 20% seller fee is the same for every level."),
        ("What is the Fiverr success score?", "A score up to 10 reflecting buyer satisfaction and how your orders conclude, including cancellations — not just your star rating."),
    ],
})

# ------------------------------------------------------------------ 2026-11-06
POSTS.append({
    "slug": "how-to-raise-freelance-rates", "image": "/assets/img/blog/how-to-raise-freelance-rates",
    "alt": "Glass tiles with a trending-up arrow, a tag and a handshake icon on a dark gradient background",
    "title": "How to Raise Your Freelance Rates Without Losing Clients",
    "h1": "How to raise your freelance rates without losing clients",
    "desc": "When to raise your freelance rates, how much to increase, how to tell existing clients (with a message template), and how to raise prices on Fiverr and Upwork safely.",
    "lede": "If you're always busy, your prices are telling you something. Here's how to raise them with confidence — and keep the clients you want.",
    "date": "2026-11-06", "cat": "Pricing", "icon": "tag",
    "tools": ["hourly-rate-calculator", "fiverr-reverse-fee-calculator", "project-quote-calculator"],
    "body": takeaways([
        "Signs it's time: you're fully booked, clients accept quotes instantly, or your costs and fees have gone up.",
        "Raise in steps of <strong>10–20%</strong>, starting with <strong>new clients</strong>.",
        "Give existing clients <strong>notice</strong> — 30 days is common — and a clear date.",
        "Re-check your <strong>minimum rate</strong> first, so the new price covers fees, tax and time.",
    ]) + '''
<h2>Signs your rates are too low</h2>
<ul>
<li><strong>You're always fully booked</strong> and turning work away.</li>
<li><strong>Clients say yes immediately</strong> — no questions, no negotiation.</li>
<li><strong>Your costs have risen</strong>: software, internet, platform fees, inflation.</li>
<li><strong>Your skills have grown</strong> — better results, faster delivery, a stronger portfolio.</li>
<li><strong>You haven't raised prices in a year</strong> or more.</li>
</ul>

<h2>Step 1: Recalculate your floor</h2>
<p>Before deciding the new price, work out the minimum your work must earn. Include your income goal, business costs, tax and platform fees, and be honest about billable hours.</p>
''' + cta("hourly-rate-calculator", "Find your minimum rate", "From income goal, costs, tax and realistic hours to an hourly floor.", "Open hourly rate calculator") + '''
<h2>Step 2: Decide how much to raise</h2>
<p>For most freelancers, <strong>10–20%</strong> at a time is a comfortable step: noticeable for your income, small enough that good clients rarely leave. If you're far below your floor, raise in two steps a few months apart rather than one big jump.</p>
<p>On Fiverr or Upwork, remember fees are taken from the new price too. To keep $50 more per order on Fiverr, the list price must rise by $62.50.</p>
''' + cta("fiverr-reverse-fee-calculator", "Price for what you want to keep", "Works backwards from your target take-home to the price to list.", "Open reverse calculator") + '''
<h2>Step 3: Start with new clients</h2>
<p>New clients only ever see your new price, so there's nothing to explain. Update your gig packages, rate card and quotes first. If new clients accept the higher price, you've confirmed the market supports it.</p>

<h2>Step 4: Tell existing clients — kindly and clearly</h2>
<p>Good clients expect prices to rise over time. What they dislike is surprise. Give notice, a date and a reason in one or two sentences.</p>
<pre class="gen-out" style="margin-bottom:1.3em">Hi [name],

I've really enjoyed working with you on [project / ongoing work]. I'm writing to let you know that from [date, about 30 days away] my rate will be [new rate], up from [old rate].

Any work booked before that date stays at the current rate. Thank you for your continued trust — I'm looking forward to the next project.

Best,
[your name]</pre>
<ul>
<li><strong>Don't over-apologise</strong> or justify at length.</li>
<li><strong>Offer a grace period</strong> for work already planned.</li>
<li>For your best long-term clients, you might keep their rate a little longer — that's your choice, not an obligation.</li>
</ul>

<h2>Raising prices on Fiverr</h2>
<ul>
<li>Change one package at a time and watch orders for a couple of weeks.</li>
<li>Add value as you raise: faster delivery, an extra revision, source files.</li>
<li>Use your strongest reviews and portfolio in the gig to justify the new price.</li>
</ul>

<h2>Raising prices on Upwork</h2>
<ul>
<li>Update your profile rate for new proposals.</li>
<li>For ongoing hourly contracts, message the client with notice before changing the rate.</li>
<li>For fixed-price work, simply quote the new price for the next milestone or project.</li>
</ul>

<h2>What if a client leaves?</h2>
<p>Some will — usually the most price-sensitive ones, who are often the hardest to work with. Losing one low-paying client frees time for better-paying work. If you're worried, raise rates for new clients first and existing clients a few months later.</p>
''' + cta("project-quote-calculator", "Quote the next project", "Turn hours and your new rate into a client-ready quote.", "Open quote calculator"),
    "faq": [
        ("How much should I raise my freelance rates?", "10–20% at a time is a common, comfortable step. If you're well below your minimum rate, raise in two steps a few months apart."),
        ("How much notice should I give clients?", "About 30 days is common. Include the date and keep work already booked at the old rate."),
        ("Will I lose clients if I raise my rates?", "You may lose a few price-sensitive clients, but most good clients expect gradual increases, and the time you free up can go to better-paying work."),
    ],
})

# ------------------------------------------------------------------ 2026-11-09
POSTS.append({
    "slug": "scope-creep-freelancers", "image": "/assets/img/blog/scope-creep-freelancers",
    "alt": "Glass tiles with a shield, a document and a clock icon on a dark gradient background",
    "title": "Scope Creep: How Freelancers Can Spot It and Stop It",
    "h1": "Scope creep: how to spot it and stop it",
    "desc": "What scope creep is, the early warning signs, contract wording that prevents it, and polite scripts for handling extra requests — so you get paid for the work you actually do.",
    "lede": "“Just one small change” is how a $300 project turns into $300 for twice the work. Here's how to set limits up front and handle extra requests without awkwardness.",
    "date": "2026-11-09", "cat": "Winning work", "icon": "pen",
    "tools": ["freelance-contract-generator", "fixed-price-vs-hourly-calculator", "quotation-generator"],
    "body": takeaways([
        "Scope creep is <strong>work added after the price was agreed</strong>, without more time or money.",
        "Prevent it with a written scope: <strong>deliverables, revision rounds and a rate for extras</strong>.",
        "When a new request arrives, <strong>name it, price it, and let the client choose</strong>.",
        "Fixed-price projects are most at risk — know your break-even hours.",
    ]) + '''
<h2>What scope creep looks like</h2>
<ul>
<li>“Can you also add a blog page?” on a five-page website.</li>
<li>A fourth and fifth round of revisions on a logo quoted with two.</li>
<li>Feedback that changes the brief: “Actually, we want it to look completely different.”</li>
<li>“While you're at it, can you set up our email too?”</li>
</ul>
<p>None of these requests is unreasonable. The problem is doing them for free, quietly, until the project costs you more than it pays.</p>

<h2>Why it hurts most on fixed-price work</h2>
<p>On hourly contracts, extra work means extra pay. On fixed price, every extra hour lowers your effective rate. Know your <strong>break-even point</strong> — the number of hours at which the fixed price stops being better than billing hourly.</p>
''' + cta("fixed-price-vs-hourly-calculator", "Know your break-even hours", "Compare a fixed price with your hourly rate, including overruns.", "Compare now") + '''
<h2>Prevent it before you start</h2>
<p>Most scope creep is prevented in writing, before work begins. Your quote or agreement should cover:</p>
<ol>
<li><strong>Deliverables</strong> — a specific list. “Five pages: Home, About, Services, Blog, Contact.”</li>
<li><strong>What's not included</strong> — “Copywriting, hosting and email setup are not included.”</li>
<li><strong>Revision rounds</strong> — “Two rounds of revisions on the agreed design.”</li>
<li><strong>Extra work</strong> — “Work outside this scope is quoted separately at $X per hour and starts after written approval.”</li>
<li><strong>Feedback timing</strong> — “Delays in feedback move the delivery date by the same amount.”</li>
</ol>
''' + cta("freelance-contract-generator", "Put the scope in writing", "A plain-language agreement with deliverables, revisions and a rate for extra work.", "Open contract generator") + '''
<h2>Contract wording you can use</h2>
<pre class="gen-out" style="margin-bottom:1.3em">The fee covers the deliverables listed above and [two] rounds of revisions.
Anything not listed — including new pages, features or a change of direction — is outside the scope.
Extra work will be quoted separately at [rate] per hour and will only begin after written approval.</pre>

<h2>How to handle a new request</h2>
<p>Use a simple three-step reply: acknowledge, name it, offer a choice.</p>
<pre class="gen-out" style="margin-bottom:1.3em">Happy to help with that! Adding [request] is outside our original scope, so here are two options:

1. I add it now for [price], and delivery moves to [date].
2. We finish the current scope first and handle this as a follow-up project.

Which would you prefer?</pre>
<ul>
<li><strong>Stay friendly.</strong> The client usually doesn't realise it's extra.</li>
<li><strong>Be specific</strong> about price and time — vague answers invite “so you'll do it for free?”</li>
<li><strong>Get approval in writing</strong> before starting the extra work.</li>
</ul>

<h2>Small favours: when it's fine</h2>
<p>A five-minute fix for a good client can be worth doing free — it builds goodwill. The rule: make it a conscious choice, and say so (“I've included this as a small extra at no charge”). That keeps it a favour, not a new expectation.</p>

<h2>On Fiverr and Upwork</h2>
<ul>
<li><strong>Fiverr:</strong> handle extra requests with a <strong>custom offer</strong> or gig extras, so the work and payment stay on the platform.</li>
<li><strong>Upwork:</strong> add a <strong>new milestone</strong> for fixed-price contracts, or agree extra hours on hourly ones.</li>
</ul>
''' + cta("quotation-generator", "Quote the extra work", "Send a quick, professional quote for the new request.", "Open quotation generator"),
    "faq": [
        ("What is scope creep?", "Extra work added to a project after the price and deliverables were agreed, without extra time or payment."),
        ("How do I stop scope creep without upsetting the client?", "Acknowledge the request, explain it's outside the agreed scope, and offer a choice: add it for a price and new date, or do it later as a separate project."),
        ("What should a contract include to prevent scope creep?", "A specific list of deliverables, what's excluded, the number of revision rounds and a rate for extra work."),
    ],
})

# ------------------------------------------------------------------ 2026-11-12
POSTS.append({
    "slug": "how-to-price-a-website-project", "image": "/assets/img/blog/how-to-price-a-website-project",
    "alt": "Glass tiles with a monitor, a calculator and a tag icon on a dark gradient background",
    "title": "How to Price a Website Project: A Step-by-Step Method for Freelancers",
    "h1": "How to price a website project",
    "desc": "A step-by-step method to price a website: break it into parts, estimate hours, add buffer and platform fees, separate client costs like hosting, and offer maintenance as recurring income.",
    "lede": "“How much for a website?” has no single answer — but there is a reliable way to work out yours. Here's the method, with a worked example.",
    "date": "2026-11-12", "cat": "Pricing", "icon": "tag",
    "tools": ["project-quote-calculator", "hourly-rate-calculator", "quotation-generator", "fiverr-reverse-fee-calculator"],
    "body": takeaways([
        "Break the website into <strong>parts</strong> and estimate hours for each.",
        "Multiply by your rate, then add a <strong>revision buffer</strong> and, on a platform, the <strong>platform fee</strong>.",
        "Keep <strong>client costs</strong> — domain, hosting, premium plugins — separate from your fee.",
        "Offer <strong>maintenance</strong> as a monthly service for recurring income.",
    ]) + '''
<h2>Step 1: Ask the right questions</h2>
<p>Before any number, understand the project. A short list of questions saves hours later:</p>
<ul>
<li>How many pages, and which ones?</li>
<li>Who provides the text and images?</li>
<li>Any features: contact forms, booking, online payments, a shop, multiple languages?</li>
<li>Platform preference: WordPress, Shopify, custom code?</li>
<li>Deadline, and who gives feedback?</li>
<li>Do they already have a domain, hosting and branding?</li>
</ul>

<h2>Step 2: Break it into parts and estimate hours</h2>
<p>Estimate each part separately. Your own past projects are the best guide; if you don't track hours yet, start now.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th class="num">Hours (example)</th></tr></thead>
<tbody>
<tr><td>Discovery and planning</td><td class="num">3</td></tr>
<tr><td>Design (home + inner page templates)</td><td class="num">10</td></tr>
<tr><td>Build five pages</td><td class="num">16</td></tr>
<tr><td>Contact form and integrations</td><td class="num">3</td></tr>
<tr><td>Mobile testing and speed</td><td class="num">4</td></tr>
<tr><td>Launch and handover</td><td class="num">2</td></tr>
<tr><th>Total</th><th class="num">38</th></tr>
</tbody></table></div>

<h2>Step 3: Apply your rate</h2>
<p>Use a rate that covers your income goal, costs and unbilled time — not a guess. If you don't know it, calculate it first.</p>
''' + cta("hourly-rate-calculator", "Know your rate", "Find the minimum hourly rate that pays your goal, costs and tax.", "Open hourly rate calculator") + '''
<h2>Step 4: Add buffer and fees</h2>
<p>Projects almost always take longer than planned. Add a <strong>revision buffer</strong> of 10–20%. If you sell through Fiverr or Upwork, gross up the total so the platform's cut doesn't come out of your pocket.</p>
<p class="formula">Quote = hours × rate × (1 + buffer) ÷ (1 − platform fee)</p>
<p>For the example: 38 hours × $25 = $950. Add a 15% buffer: $1,092.50. On Fiverr (20%): $1,092.50 ÷ 0.8 ≈ <strong>$1,366</strong>.</p>
''' + cta("project-quote-calculator", "Build the quote", "Line-by-line tasks, buffer, rush fee, platform fee and deposit.", "Open quote calculator") + '''
<h2>Step 5: Separate client costs</h2>
<p>Domains, hosting, premium themes and plugins, paid fonts and stock photos belong to the client. List them separately — either the client buys them directly, or you buy them and pass on the cost. Keeping them out of your fee keeps your price comparable and avoids paying for renewals yourself.</p>

<h2>Step 6: Offer packages</h2>
<p>Giving two or three options lets the client choose instead of haggling:</p>
<ul>
<li><strong>Starter</strong> — fewer pages, template-based design.</li>
<li><strong>Business</strong> — your main offer, custom design, the common features.</li>
<li><strong>Premium</strong> — extra features, faster delivery, training session.</li>
</ul>

<h2>Step 7: Add maintenance as recurring income</h2>
<p>After launch, many clients need updates, backups, security checks and small edits. A monthly maintenance plan with a clear hours limit gives them peace of mind and gives you predictable income.</p>

<h2>Put it in writing</h2>
<p>Send a <a href="/quotation-generator/">quotation</a> listing pages, features, revisions, timeline and payment terms (for example 50% upfront), and agree the scope before starting. Our guide to <a href="/blog/scope-creep-freelancers/">stopping scope creep</a> shows what to include.</p>
''',
    "faq": [
        ("How do freelancers price a website?", "Break it into parts, estimate hours for each, multiply by your rate, add a revision buffer and any platform fee, and list client costs like hosting separately."),
        ("Should hosting and domain be included in my price?", "Usually keep them separate. They're the client's ongoing costs and renew every year."),
        ("Should I charge hourly or fixed price for a website?", "Most clients prefer fixed price for a clearly defined site. Use hourly for open-ended changes and ongoing work."),
    ],
})

# ------------------------------------------------------------------ 2026-11-15
POSTS.append({
    "slug": "mid-market-exchange-rate-explained", "image": "/assets/img/blog/mid-market-exchange-rate-explained",
    "alt": "Glass tiles with an arrows-exchange icon, a globe and coins on a dark gradient background",
    "title": "Mid-Market Exchange Rate Explained: Why You Get Less Than Google's Rate",
    "h1": "The mid-market rate: why you get less than Google's rate",
    "desc": "What the mid-market exchange rate is, why Payoneer, banks and apps pay you less, how to work out the hidden fee as a percentage, and simple ways to lose less when converting.",
    "lede": "You search “USD to PKR”, see one rate, then withdraw and get fewer rupees. The gap isn't an error — it's a fee hidden inside the rate. Here's how to measure it.",
    "date": "2026-11-15", "cat": "Money", "icon": "fx",
    "tools": ["freelancer-currency-converter", "payoneer-to-pkr-calculator", "wise-vs-payoneer-vs-bank"],
    "body": takeaways([
        "The <strong>mid-market rate</strong> is the midpoint between buy and sell prices — the rate you see on Google or XE.",
        "Most providers pay you a <strong>lower rate</strong> and keep the difference. That's a fee, even if it's not labelled one.",
        "Measure it: <strong>(mid-market − your rate) ÷ mid-market × 100</strong> gives the hidden fee in %.",
        "Compare providers on <strong>final rupees received</strong>, not on “zero fees” claims.",
    ]) + '''
<h2>What the mid-market rate is</h2>
<p>In currency markets, there are always two prices: what buyers will pay and what sellers will accept. The <strong>mid-market rate</strong> is the point exactly between them. It's the rate you see on Google, XE and most currency converters, and it's the fairest reference for “what my dollars are worth right now”.</p>
<p>Individuals almost never get it directly. Banks, Payoneer and money apps buy at one price and pay you another, keeping the difference — called the <strong>spread</strong> or <strong>markup</strong>.</p>

<h2>Why your rate is lower</h2>
<ul>
<li><strong>The conversion markup.</strong> A provider might pay you a rate a percent or two below mid-market. On Payoneer withdrawals to PKR, a markup of around 2% is typical; the exact rate is shown before you confirm.</li>
<li><strong>Timing.</strong> Rates move all day. Google updates frequently; your provider may refresh on its own schedule.</li>
<li><strong>Bank-side rates.</strong> If dollars arrive in a PKR account, your bank converts at its own buying rate.</li>
</ul>

<h2>How to work out the hidden fee</h2>
<p class="formula">Hidden fee % = (mid-market rate − rate you got) ÷ mid-market rate × 100</p>
<p><strong>Example (illustrative numbers):</strong> mid-market is Rs 280 per dollar and you receive Rs 274.40. The difference is Rs 5.60, so the hidden fee is 5.60 ÷ 280 × 100 = <strong>2%</strong>. On a $500 withdrawal, that's Rs 2,800 — before any visible fee.</p>
''' + cta("freelancer-currency-converter", "Check today's mid-market rate", "Live reference rates for USD, GBP, EUR, PKR and more.", "Open currency converter") + '''
<h2>The total cost of a withdrawal</h2>
<p>Add up everything between “money in my account” and “rupees in my bank”:</p>
<ol>
<li>Any <strong>receiving fee</strong> (for example, when a client pays you directly into Payoneer).</li>
<li>Any <strong>flat withdrawal fee</strong> (Fiverr charges $3 per withdrawal to Payoneer).</li>
<li>The <strong>conversion markup</strong> hidden in the rate.</li>
</ol>
<p>Then compare what you actually received with “amount × mid-market rate”. That gap is your true total cost.</p>
''' + cta("payoneer-to-pkr-calculator", "See the rupees you'll get", "Live rate, conversion markup and fees — the final PKR amount.", "Open Payoneer to PKR") + '''
<h2>Ways to lose less</h2>
<ul>
<li><strong>Withdraw less often, in bigger amounts</strong>, so flat fees are spread across more money. The percentage markup still applies to the whole amount.</li>
<li><strong>Compare routes</strong> using the final rupee amount, not advertised fees.</li>
<li><strong>Check the rate before confirming.</strong> Payoneer shows the rate and amount on the confirmation screen.</li>
<li><strong>Keep dollars where it makes sense.</strong> If you pay for software or services in dollars, paying from your USD balance avoids converting twice.</li>
</ul>
<p>Our guide to <a href="/blog/payoneer-fees-pakistan/">Payoneer fees in Pakistan</a> covers each Payoneer charge in detail.</p>
''' + cta("wise-vs-payoneer-vs-bank", "Compare the routes", "Side by side: fees, rates and what you actually receive.", "Compare now") + '''
<h2>“Zero fee” offers</h2>
<p>When a service says “no fees”, check the rate. A transfer with no visible fee but a 3% worse rate costs more than one with a small fee and a near-mid-market rate. Final amount received is the only fair comparison.</p>
''',
    "faq": [
        ("What is the mid-market exchange rate?", "The midpoint between the buying and selling price of a currency — the rate shown on Google and XE."),
        ("Why does Payoneer give me less than Google's rate?", "Payoneer, like most providers, applies a conversion markup to the rate. The difference between its rate and mid-market is effectively a fee."),
        ("How do I calculate the hidden exchange rate fee?", "Subtract the rate you got from the mid-market rate, divide by the mid-market rate and multiply by 100."),
        ("Can I get the mid-market rate?", "Some providers convert at or very close to it and charge a visible fee instead. Compare the final amount you receive."),
    ],
})

# ------------------------------------------------------------------ 2026-11-18
POSTS.append({
    "slug": "budgeting-irregular-freelance-income", "image": "/assets/img/blog/budgeting-irregular-freelance-income",
    "alt": "Glass tiles with a piggy bank, a calendar and a chart icon on a dark gradient background",
    "title": "Budgeting on Irregular Freelance Income: A Simple System",
    "h1": "Budgeting on irregular freelance income",
    "desc": "A simple system for budgeting irregular freelance income: find your baseline, pay yourself a fixed salary, keep a buffer and tax pot, and handle big months and slow months calmly.",
    "lede": "One month you earn double, the next almost nothing. A simple system turns that rollercoaster into a steady monthly income you can plan around.",
    "date": "2026-11-18", "cat": "Money", "icon": "pie",
    "tools": ["hourly-rate-calculator", "profit-margin-calculator", "payoneer-to-pkr-calculator"],
    "body": takeaways([
        "Work out your <strong>baseline</strong>: the minimum you need each month for essentials.",
        "Send all income to one <strong>business pot</strong>, then pay yourself a <strong>fixed monthly salary</strong> from it.",
        "Set aside a <strong>tax pot</strong> and build a <strong>buffer</strong> of a few months' baseline.",
        "In big months, top up the buffer; in slow months, the buffer pays your salary.",
    ]) + '''
<h2>Why normal budgeting fails freelancers</h2>
<p>Most budgeting advice assumes the same salary every month. Freelance income doesn't work like that — orders bunch up, clients pay late, platforms hold funds for clearance. If you spend based on a good month, a slow month becomes a crisis.</p>
<p>The fix is to separate <strong>earning</strong> from <strong>paying yourself</strong>.</p>

<h2>Step 1: Find your baseline</h2>
<p>List your essential monthly costs: rent, food, utilities, internet, transport, family support, loan repayments, school fees. That total is your <strong>baseline</strong> — the amount you must have every month.</p>
<p>Then look at your last 6–12 months of income. If your lowest months are below your baseline, the buffer in step 4 matters even more.</p>

<h2>Step 2: Use separate pots</h2>
<p>Separate pots make the system visible. They can be different bank accounts, or one account plus a simple spreadsheet.</p>
<ul>
<li><strong>Business pot</strong> — all freelance income lands here (or is withdrawn here from Payoneer).</li>
<li><strong>Tax pot</strong> — a fixed percentage of every payment.</li>
<li><strong>Buffer pot</strong> — your safety net.</li>
<li><strong>Personal account</strong> — receives your monthly salary; this is what you spend.</li>
</ul>

<h2>Step 3: Pay yourself a fixed salary</h2>
<p>On the same day each month, move a fixed amount from the business pot to your personal account. Start with your baseline plus a modest amount for savings and personal spending. Raise the salary only when your buffer is full and your income has stayed higher for several months.</p>

<h2>Step 4: Build a buffer</h2>
<p>A common target is <strong>three to six months of baseline</strong>. Build it gradually: in every month where income exceeds your salary plus tax, the extra goes to the buffer first. Once it's full, extra income can go to savings, investments or equipment.</p>

<h2>Step 5: Set aside tax as you go</h2>
<p>Move a percentage of every payment into the tax pot so the bill is never a surprise. In Pakistan, freelancers registered with PSEB can pay a much lower final tax on export remittances — see our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a>. In the US and UK, set aside more because income tax and self-employment tax or National Insurance apply.</p>
''' + cta("payoneer-to-pkr-calculator", "Know what reaches your bank", "Turn a dollar balance into the rupees you'll actually receive.", "Open Payoneer to PKR") + '''
<h2>Step 6: Make your rates support the system</h2>
<p>If your average month can't cover your salary, tax and buffer, the problem isn't the budget — it's the rate or the volume of work. Calculate the hourly rate your goals need, and check your profit after costs.</p>
''' + cta("hourly-rate-calculator", "Find the rate your budget needs", "Income goal, costs, tax and real billable hours to an hourly rate.", "Open hourly rate calculator") + '''
<h2>A worked example (illustrative)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Month</th><th class="num">Income</th><th class="num">Tax pot (10%)</th><th class="num">Salary</th><th class="num">To / from buffer</th></tr></thead>
<tbody>
<tr><td>1</td><td class="num">Rs 2,40,000</td><td class="num">Rs 24,000</td><td class="num">Rs 1,50,000</td><td class="num">+Rs 66,000</td></tr>
<tr><td>2</td><td class="num">Rs 1,10,000</td><td class="num">Rs 11,000</td><td class="num">Rs 1,50,000</td><td class="num">−Rs 51,000</td></tr>
<tr><td>3</td><td class="num">Rs 1,90,000</td><td class="num">Rs 19,000</td><td class="num">Rs 1,50,000</td><td class="num">+Rs 21,000</td></tr>
</tbody></table></div>
<p>Income swung from Rs 1.1 lakh to Rs 2.4 lakh, but your salary stayed at Rs 1.5 lakh every month. The tax percentage here is only an example — use the rate that applies to you.</p>

<h2>Habits that help</h2>
<ul>
<li><strong>Invoice promptly</strong> and follow up on late payments.</li>
<li><strong>Know platform clearance times</strong> — Fiverr funds aren't available the day you deliver.</li>
<li><strong>Review monthly</strong>: income, salary, buffer level, upcoming big costs.</li>
</ul>
''' + cta("profit-margin-calculator", "Check your real profit", "Revenue, costs and fees to profit and margin.", "Open profit calculator") + '''
<p class="hint">General information, not financial advice.</p>
''',
    "faq": [
        ("How do freelancers budget with irregular income?", "Put all income in a business pot, pay yourself a fixed monthly salary from it, set aside tax, and keep a buffer to cover slow months."),
        ("How big should a freelancer's emergency buffer be?", "Three to six months of essential expenses is a common target. Build it gradually from good months."),
        ("How much should I pay myself as a freelancer?", "Start with your essential monthly costs plus a modest amount for savings, and only raise it when your buffer is full and income has stayed higher for several months."),
    ],
})

# ------------------------------------------------------------------ 2026-11-21
POSTS.append({
    "slug": "quarterly-estimated-taxes-freelancers", "image": "/assets/img/blog/quarterly-estimated-taxes-freelancers",
    "alt": "Glass tiles with a calendar, a landmark building and a calculator icon on a dark gradient background",
    "title": "Quarterly Estimated Taxes for US Freelancers: Dates and How to Pay",
    "h1": "Quarterly estimated taxes for US freelancers",
    "desc": "Who must pay US quarterly estimated taxes, the 2026 due dates, how to calculate each payment, the safe harbor rules that avoid penalties, and how to pay the IRS online.",
    "lede": "No employer withholds tax from freelance income, so the IRS expects you to pay during the year. Here's who has to, when, and how much.",
    "date": "2026-11-21", "cat": "Tax", "icon": "flag",
    "tools": ["self-employment-tax-calculator", "hourly-rate-calculator", "profit-margin-calculator"],
    "body": takeaways([
        "You generally must pay estimated tax if you expect to owe <strong>$1,000 or more</strong> for the year after withholding and credits.",
        "2026 tax year due dates: <strong>15 April, 15 June, 15 September 2026 and 15 January 2027</strong>.",
        "Payments cover <strong>income tax and self-employment tax</strong>.",
        "Safe harbor: pay <strong>90% of this year's tax</strong> or <strong>100% of last year's</strong> (110% if your AGI was over $150,000) to avoid the underpayment penalty.",
    ]) + '''
<h2>Who needs to pay estimated taxes</h2>
<p>According to the IRS, individuals — including sole proprietors and freelancers — generally need to make estimated tax payments if they expect to owe <strong>$1,000 or more</strong> when they file their return. If you have a day job with withholding, you can sometimes increase withholding instead.</p>

<h2>2026 due dates</h2>
<div class="table-wrap"><table>
<thead><tr><th>Income earned</th><th>Payment due</th></tr></thead>
<tbody>
<tr><td>1 January – 31 March 2026</td><td>15 April 2026</td></tr>
<tr><td>1 April – 31 May 2026</td><td>15 June 2026</td></tr>
<tr><td>1 June – 31 August 2026</td><td>15 September 2026</td></tr>
<tr><td>1 September – 31 December 2026</td><td>15 January 2027</td></tr>
</tbody></table></div>
<p>The “quarters” aren't equal. If a date falls on a weekend or holiday, the deadline moves to the next business day.</p>

<h2>What the payments cover</h2>
<ul>
<li><strong>Self-employment tax</strong> — Social Security and Medicare, 15.3% on 92.35% of net earnings (the Social Security part stops at the annual wage base).</li>
<li><strong>Federal income tax</strong> on your profit, after the deduction for half of self-employment tax and your standard or itemised deduction.</li>
</ul>
''' + cta("self-employment-tax-calculator", "Estimate your annual tax", "Self-employment tax plus federal income tax on your freelance profit.", "Open SE tax calculator") + '''
<h2>How to calculate each payment</h2>
<ol>
<li>Estimate your <strong>net profit</strong> for the year (income minus business expenses).</li>
<li>Estimate the <strong>total tax</strong> on it — self-employment tax plus income tax.</li>
<li>Subtract any withholding and credits you expect.</li>
<li>Divide by four for each payment, or use the safe harbor amount below.</li>
</ol>
<p>The IRS Form 1040-ES includes a worksheet for this. If your income is uneven — a quiet first half and a busy second half — the <strong>annualised income installment method</strong> (Form 2210, Schedule AI) can lower earlier payments.</p>

<h2>Safe harbor: how to avoid the penalty</h2>
<p>You generally won't owe an underpayment penalty if your total payments on time are at least the smaller of:</p>
<ul>
<li><strong>90%</strong> of the tax for the current year, or</li>
<li><strong>100%</strong> of the tax on last year's return (<strong>110%</strong> if last year's adjusted gross income was more than $150,000, or $75,000 if married filing separately).</li>
</ul>
<p>The prior-year rule is the simplest for many freelancers: take last year's total tax, divide by four, and pay that each quarter. You settle any difference when you file.</p>

<h2>How to pay</h2>
<ul>
<li><strong>IRS Direct Pay</strong> — free, from a bank account.</li>
<li><strong>Your IRS Online Account.</strong></li>
<li><strong>EFTPS</strong> — the Treasury's free payment system.</li>
<li>Debit or credit card through approved processors (they charge a fee).</li>
<li>Check or money order with a Form 1040-ES voucher.</li>
</ul>
<p>Most states with an income tax have their own estimated payment system — check your state's revenue department.</p>

<h2>Practical tips</h2>
<ul>
<li><strong>Set aside a percentage of every payment</strong> in a separate account so the money is there on the due date.</li>
<li><strong>Put the four dates in your calendar</strong> with a reminder a week before.</li>
<li><strong>Price for tax.</strong> Your rate needs to cover it — our <a href="/blog/how-to-price-freelance-services/">pricing guide</a> shows how.</li>
</ul>
''' + cta("hourly-rate-calculator", "Price with tax included", "Find the hourly rate that covers your goal, costs and taxes.", "Open hourly rate calculator") + '''
<p class="hint">Dates and rules from IRS guidance on estimated taxes and Form 1040-ES for tax year 2026. General information, not tax advice — confirm with the IRS or a tax professional for your situation.</p>
''',
    "faq": [
        ("When are quarterly estimated taxes due for 2026?", "15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027. Dates on weekends or holidays move to the next business day."),
        ("Do I have to pay estimated taxes as a freelancer?", "Generally yes if you expect to owe $1,000 or more for the year after withholding and credits."),
        ("How do I avoid the estimated tax penalty?", "Pay on time at least 90% of this year's tax or 100% of last year's tax (110% if last year's AGI was over $150,000)."),
        ("How do I pay estimated taxes online?", "Use IRS Direct Pay, your IRS Online Account or EFTPS, all free from a bank account."),
    ],
})

# ------------------------------------------------------------------ 2026-11-24
POSTS.append({
    "slug": "uk-self-assessment-freelancers", "image": "/assets/img/blog/uk-self-assessment-freelancers",
    "alt": "Glass tiles with a pound sign, a calendar and a file icon on a dark gradient background",
    "title": "UK Self Assessment for Freelancers: Deadlines and Payments on Account",
    "h1": "UK Self Assessment for freelancers",
    "desc": "UK Self Assessment for freelancers and sole traders: registration and filing deadlines, payments on account explained with an example, penalties, and how Making Tax Digital changes things from 2026.",
    "lede": "As a UK freelancer you report your own income to HMRC and pay tax in instalments. Here are the dates, how payments on account work, and what's changing with Making Tax Digital.",
    "date": "2026-11-24", "cat": "Tax", "icon": "pound",
    "tools": ["uk-freelancer-tax-calculator", "hourly-rate-calculator", "invoice-generator"],
    "body": takeaways([
        "Tax year: <strong>6 April to 5 April</strong>. The 2025–26 online return and balancing payment are due <strong>31 January 2027</strong>.",
        "<strong>Payments on account</strong> — two advance payments towards next year's bill — apply if your bill is over £1,000.",
        "Missing the deadline means an immediate <strong>£100 penalty</strong>, with more for longer delays.",
        "<strong>Making Tax Digital</strong> for Income Tax starts from April 2026 for higher earners, with quarterly updates.",
    ]) + '''
<h2>Who needs to file</h2>
<p>You generally need to file a Self Assessment tax return if you're self-employed as a sole trader and earned more than £1,000 from self-employment in the tax year (the trading allowance), or if you have other untaxed income. Check HMRC's “Check if you need to send a Self Assessment tax return” tool if you're unsure.</p>

<h2>Key deadlines for the 2025–26 tax year</h2>
<div class="table-wrap"><table>
<thead><tr><th>Date</th><th>What's due</th></tr></thead>
<tbody>
<tr><td>5 October 2026</td><td>Register for Self Assessment if you're new to it</td></tr>
<tr><td>31 October 2026</td><td>Paper tax return</td></tr>
<tr><td>31 January 2027</td><td>Online return; pay the balance for 2025–26; first payment on account for 2026–27</td></tr>
<tr><td>31 July 2027</td><td>Second payment on account for 2026–27</td></tr>
</tbody></table></div>

<h2>Payments on account explained</h2>
<p>If your Self Assessment bill is more than <strong>£1,000</strong> (and less than 80% of your tax was already taken at source), HMRC asks for two advance payments towards next year's bill, each half of this year's bill. They're due on <strong>31 January</strong> and <strong>31 July</strong>.</p>
<h3>Example (illustrative)</h3>
<p>Your bill for 2025–26 is £6,000, and it's your first year with payments on account.</p>
<ul>
<li><strong>31 January 2027:</strong> £6,000 for 2025–26 + £3,000 first payment on account for 2026–27 = <strong>£9,000</strong>.</li>
<li><strong>31 July 2027:</strong> £3,000 second payment on account.</li>
<li><strong>31 January 2028:</strong> any balance for 2026–27 (if the actual bill was higher) plus the first payment on account for 2027–28.</li>
</ul>
<p>That first January surprises many new freelancers — it can be up to one and a half times the year's bill. If you expect lower profits, you can ask HMRC to reduce payments on account, but if you reduce them too far you'll pay interest on the shortfall.</p>
''' + cta("uk-freelancer-tax-calculator", "Estimate your UK tax bill", "Income tax and Class 4 National Insurance on your profit.", "Open UK tax calculator") + '''
<h2>Penalties and interest</h2>
<ul>
<li><strong>£100</strong> if your return is up to three months late, even if you owe no tax.</li>
<li>Further daily and percentage-based penalties for longer delays.</li>
<li>Interest and late-payment penalties on tax paid late.</li>
</ul>

<h2>Making Tax Digital for Income Tax</h2>
<p>HMRC is phasing in Making Tax Digital (MTD) for Income Tax. Sole traders and landlords with qualifying income above a threshold must keep digital records and send <strong>quarterly updates</strong> using compatible software:</p>
<ul>
<li>From <strong>6 April 2026</strong>: qualifying income over <strong>£50,000</strong>.</li>
<li>From <strong>April 2027</strong>: over <strong>£30,000</strong>.</li>
<li>From <strong>April 2028</strong>: over <strong>£20,000</strong>.</li>
</ul>
<p>Qualifying income is your total self-employment and property income before expenses, and the threshold is based on an earlier tax year's return. Quarterly updates are due on <strong>7 August, 7 November, 7 February and 7 May</strong>. You still make a final declaration after the year ends, and tax payment dates stay the same.</p>

<h2>Practical tips</h2>
<ul>
<li><strong>Keep records as you go</strong>: invoices, receipts and platform statements.</li>
<li><strong>Set aside tax from every payment</strong>, including for payments on account.</li>
<li><strong>File early</strong> — filing in, say, May doesn't mean paying early, but you'll know your bill months in advance.</li>
<li><strong>Price for tax and National Insurance</strong> — see our <a href="/blog/how-to-price-freelance-services/">pricing guide</a>.</li>
</ul>
''' + cta("invoice-generator", "Keep tidy records", "Create professional invoices with sequential numbers.", "Open invoice generator") + '''
<p class="hint">Dates and thresholds from GOV.UK guidance on Self Assessment, payments on account and Making Tax Digital for Income Tax. General information, not tax advice — check GOV.UK or an accountant for your situation.</p>
''',
    "faq": [
        ("When is the UK Self Assessment deadline?", "For the 2025–26 tax year: 31 October 2026 for paper returns and 31 January 2027 for online returns and payment."),
        ("What are payments on account?", "Two advance payments towards next year's tax bill, each half of this year's bill, due 31 January and 31 July. They apply if your bill is over £1,000 and less than 80% was taxed at source."),
        ("What is the penalty for filing Self Assessment late?", "£100 for up to three months late, with further penalties for longer delays, plus interest on tax paid late."),
        ("Does Making Tax Digital apply to me?", "From 6 April 2026 it applies to sole traders and landlords with qualifying income over £50,000, then over £30,000 from April 2027 and over £20,000 from April 2028."),
    ],
})

# ------------------------------------------------------------------ 2026-11-27
POSTS.append({
    "slug": "how-to-get-repeat-clients", "image": "/assets/img/blog/how-to-get-repeat-clients",
    "alt": "Glass tiles with a handshake, a repeat-arrows icon and a heart on a dark gradient background",
    "title": "How to Turn One-Off Freelance Clients into Repeat Clients",
    "h1": "How to turn one-off clients into repeat clients",
    "desc": "Practical ways to turn one-off freelance clients into repeat clients: deliver a smooth experience, follow up at the right time, suggest the next project and offer retainers.",
    "lede": "Winning a new client takes proposals, pitches and luck. Winning the same client again takes a good experience and one well-timed message. Here's how to make it happen.",
    "date": "2026-11-27", "cat": "Winning work", "icon": "people",
    "tools": ["invoice-generator", "quotation-generator", "freelance-contract-generator"],
    "body": takeaways([
        "Repeat clients cost less time to win, already trust you, and often pay more.",
        "The work matters, but so does the <strong>experience</strong>: clear updates, on-time delivery, easy communication.",
        "Follow up after delivery with a <strong>specific next idea</strong>, not just “let me know if you need anything”.",
        "For regular work, offer a <strong>monthly retainer</strong> with a clear scope.",
    ]) + '''
<h2>Why repeat clients matter</h2>
<p>With a repeat client there's no proposal to write, no trust to build and no long briefing. Projects start faster, misunderstandings are rarer, and many clients are happy to pay more for someone they know delivers. On platforms there are extra benefits: PeoplePerHour's fee falls as you bill the same client more, and repeat buyers on Fiverr signal to buyers that you're reliable.</p>

<h2>1. Make the first project easy</h2>
<ul>
<li><strong>Confirm the brief in writing</strong> before you start, so expectations match.</li>
<li><strong>Send updates</strong> without being asked, especially on longer projects.</li>
<li><strong>Deliver on time</strong> — or a little early. If something slips, say so early.</li>
<li><strong>Make feedback easy</strong>: clear previews, numbered questions, one place for comments.</li>
</ul>

<h2>2. Finish professionally</h2>
<p>The end of a project is when clients decide whether to come back.</p>
<ul>
<li>Deliver files <strong>organised and labelled</strong>, with short instructions if needed.</li>
<li>Send a <strong>clear invoice</strong> promptly — see our guide to <a href="/blog/how-to-invoice-clients-as-a-freelancer/">invoicing clients</a>.</li>
<li>Thank them, and ask if everything works as expected.</li>
</ul>
''' + cta("invoice-generator", "Send a polished invoice", "Professional invoices with your logo, terms and totals.", "Open invoice generator") + '''
<h2>3. Follow up at the right time</h2>
<p>Most clients don't come back simply because they forget. A short message at the right moment fixes that:</p>
<ul>
<li><strong>One to two weeks after delivery:</strong> check how the work is performing.</li>
<li><strong>When something relevant happens:</strong> a new season, a product launch, a platform change that affects them.</li>
<li><strong>Every few months:</strong> a brief, useful idea — not a generic “any work for me?”.</li>
</ul>
<pre class="gen-out" style="margin-bottom:1.3em">Hi [name], hope the new [website / logo / videos] is working well for you.

I noticed [specific observation — e.g. the blog page has no newsletter sign-up]. I could [specific improvement] in about [time] for [price].

Happy to send details if useful.</pre>

<h2>4. Suggest the next project</h2>
<p>You know the client's business better than a stranger would. Use that to suggest a natural next step:</p>
<ul>
<li>Logo done → social media templates or a brand guide.</li>
<li>Website built → monthly maintenance, speed improvements or new landing pages.</li>
<li>Article written → a content calendar or a series.</li>
</ul>
''' + cta("quotation-generator", "Quote the next project", "A clear, professional quote you can send in minutes.", "Open quotation generator") + '''
<h2>5. Offer a retainer</h2>
<p>If a client needs regular work, a <strong>monthly retainer</strong> gives them priority and gives you predictable income. Define it clearly:</p>
<ul>
<li>What's included (for example, up to 10 hours or 8 social posts per month).</li>
<li>What happens to unused hours (usually they don't roll over).</li>
<li>Your rate for work beyond the retainer.</li>
<li>Notice period to end it — 30 days is common.</li>
</ul>
<p>Put it in writing, and keep the scope tight — see our guide to <a href="/blog/scope-creep-freelancers/">stopping scope creep</a>.</p>
''' + cta("freelance-contract-generator", "Write the retainer agreement", "Scope, payment terms and notice in a plain-language agreement.", "Open contract generator") + '''
<h2>6. Reward loyalty — carefully</h2>
<p>Small gestures work better than discounts: priority scheduling, faster turnaround, a quick fix included. If you do offer a returning-client discount, keep it modest so it doesn't undercut your rates.</p>

<h2>On Fiverr and Upwork</h2>
<ul>
<li>Keep communication and payments <strong>on the platform</strong>, as their terms require for clients you met there.</li>
<li>On Fiverr, use <strong>custom offers</strong> for follow-up work.</li>
<li>On Upwork, ask the client to start a <strong>new contract</strong> or add milestones to an existing one.</li>
</ul>
''',
    "faq": [
        ("How do I get repeat clients as a freelancer?", "Make the first project smooth, finish professionally, follow up with a specific idea for the next project, and offer a retainer for regular work."),
        ("When should I follow up with a past client?", "About one to two weeks after delivery to check results, then every few months or whenever you have a relevant, specific idea."),
        ("What is a freelance retainer?", "A monthly agreement where the client pays a fixed fee for a defined amount of work or availability, giving you predictable income."),
    ],
})

# ------------------------------------------------------------------ 2026-11-30
POSTS.append({
    "slug": "freelancer-com-vs-peopleperhour", "image": "/assets/img/blog/freelancer-com-vs-peopleperhour",
    "alt": "Glass tiles with a scale, a briefcase and a users icon on a dark gradient background",
    "title": "Freelancer.com vs PeoplePerHour: Fees, Clients and Which to Choose",
    "h1": "Freelancer.com vs PeoplePerHour",
    "desc": "Freelancer.com vs PeoplePerHour compared for freelancers: project fees, PPH's tiered per-client fee, worked examples on $/£ jobs, client markets and which platform suits your work.",
    "lede": "Both platforms connect you with clients worldwide, but their fees work very differently. Here's what you actually keep on each — and where each one fits.",
    "date": "2026-11-30", "cat": "Fees", "icon": "people",
    "tools": ["freelancer-peopleperhour-fee-calculator", "fiverr-fee-calculator", "upwork-fee-calculator"],
    "body": takeaways([
        "<strong>Freelancer.com:</strong> 10% or $5 (whichever is greater) on fixed-price projects; 10% on hourly.",
        "<strong>PeoplePerHour:</strong> a tiered fee per client — 20% on the first £250, 7.5% up to £5,000, then 3.5%.",
        "Small one-off jobs: Freelancer.com usually leaves you more. Long-term clients: PeoplePerHour wins.",
        "Fees change — check each platform's current fee page before relying on numbers.",
    ]) + '''
<h2>Freelancer.com fees</h2>
<ul>
<li><strong>Fixed-price projects:</strong> 10% of the project value or $5, whichever is greater.</li>
<li><strong>Hourly projects:</strong> 10% of each payment.</li>
<li><strong>Bids:</strong> a limited number of free bids each month on the free plan; paid memberships add more bids and features.</li>
<li><strong>Clients</strong> also pay a fee (3% or $3) on top.</li>
</ul>
<p>The $5 minimum matters for small jobs: on a $20 project, $5 is 25%.</p>

<h2>PeoplePerHour fees</h2>
<p>PeoplePerHour charges a <strong>service fee based on your total billing with each client</strong>:</p>
<div class="table-wrap"><table>
<thead><tr><th>Lifetime billing with one client</th><th class="num">Fee</th></tr></thead>
<tbody>
<tr><td>First £250</td><td class="num">20%</td></tr>
<tr><td>£250 to £5,000</td><td class="num">7.5%</td></tr>
<tr><td>Above £5,000</td><td class="num">3.5%</td></tr>
</tbody></table></div>
<p>There's also a small minimum fee per invoice, and UK and EU freelancers pay VAT on the fee. A new client always starts at the 20% tier. Sources disagree on the exact thresholds, so confirm in your account.</p>
''' + cta("freelancer-peopleperhour-fee-calculator", "Calculate your take-home", "Freelancer.com’s 10%/$5 and PeoplePerHour’s tiers on any job.", "Open the calculator") + '''
<h2>Worked examples</h2>
<p>For simplicity these treat £ and $ amounts separately and ignore VAT and withdrawal fees.</p>
<div class="table-wrap"><table>
<thead><tr><th>Job</th><th class="num">Freelancer.com fee</th><th class="num">PPH fee (new client)</th></tr></thead>
<tbody>
<tr><td>Small job: 40</td><td class="num">5 (12.5%)</td><td class="num">8 (20%)</td></tr>
<tr><td>Medium job: 400</td><td class="num">40 (10%)</td><td class="num">61.25 (15.3%)</td></tr>
<tr><td>Repeat client, next 1,000</td><td class="num">100 (10%)</td><td class="num">75 (7.5%)</td></tr>
</tbody></table></div>
<p>On the second and later projects with the same client, PeoplePerHour's lower tiers pull ahead.</p>

<h2>Beyond fees</h2>
<h3>Freelancer.com</h3>
<ul>
<li>Large, global marketplace with contests as well as projects.</li>
<li>Competitive bidding — many bids per project, often on price.</li>
<li>Works well for quick technical jobs and building an initial track record.</li>
</ul>
<h3>PeoplePerHour</h3>
<ul>
<li>Strong presence with UK and European small businesses.</li>
<li>Offers (fixed-price packages, similar to Fiverr gigs) plus project proposals.</li>
<li>Rewards long-term client relationships through lower fees.</li>
</ul>

<h2>How they compare with Fiverr and Upwork</h2>
<p>Fiverr keeps a flat 20%, and Upwork's fee varies by contract. For the full comparison of those two, see <a href="/blog/fiverr-vs-upwork-fees-take-home/">Fiverr vs Upwork fees</a>. Many freelancers use more than one platform: one for steady small orders, another for longer client relationships.</p>
''' + cta("upwork-fee-calculator", "Compare with Upwork", "See what you keep on an Upwork contract.", "Open Upwork calculator") + '''
<h2>Which should you choose?</h2>
<ul>
<li><strong>Freelancer.com</strong> if you take many small, one-off jobs and are happy to bid competitively.</li>
<li><strong>PeoplePerHour</strong> if you target UK/European clients and want long-term relationships.</li>
<li><strong>Both</strong> while you're building a client base — then focus on the one that sends you better clients.</li>
</ul>
<p class="hint">Fees as published by each platform at the time of writing. Check Freelancer.com's “Fees and charges” page and PeoplePerHour's fee information for current numbers.</p>
''',
    "faq": [
        ("What are Freelancer.com fees for freelancers?", "10% or $5, whichever is greater, on fixed-price projects, and 10% on hourly projects."),
        ("What are PeoplePerHour fees?", "A tiered fee based on lifetime billing with each client: 20% on the first £250, 7.5% up to £5,000 and 3.5% above, plus a small minimum fee and VAT for UK/EU freelancers."),
        ("Is Freelancer.com or PeoplePerHour cheaper?", "Freelancer.com is usually cheaper for small one-off jobs; PeoplePerHour is cheaper for ongoing work with the same client."),
    ],
})

# ------------------------------------------------------------------ 2026-12-03
POSTS.append({
    "slug": "how-to-write-a-winning-quotation", "image": "/assets/img/blog/how-to-write-a-winning-quotation",
    "alt": "Glass tiles with a clipboard, a check badge and a pen icon on a dark gradient background",
    "title": "How to Write a Quotation That Wins the Job (With Template)",
    "h1": "How to write a quotation that wins the job",
    "desc": "What a winning freelance quotation includes, how to present price and options, payment terms, validity and follow-up — with a simple template you can copy.",
    "lede": "A quote isn't just a number. It's a short document that shows you understood the problem and makes it easy for the client to say yes.",
    "date": "2026-12-03", "cat": "Winning work", "icon": "doc",
    "tools": ["quotation-generator", "project-quote-calculator", "freelance-contract-generator"],
    "body": takeaways([
        "Open with the <strong>client's goal</strong>, not your price.",
        "List <strong>deliverables, timeline, revisions and exclusions</strong> clearly.",
        "Offer <strong>two or three options</strong> so the client chooses between yeses.",
        "Add <strong>payment terms</strong> and a <strong>validity date</strong>, then follow up.",
    ]) + '''
<h2>Quote vs estimate</h2>
<p>An <strong>estimate</strong> is a rough guide that may change. A <strong>quotation</strong> is a fixed offer: if the client accepts within the validity period, that's the price for that scope. Clients prefer quotes because they know what they'll pay — which is exactly why the scope must be clear.</p>

<h2>What a winning quote includes</h2>
<ol>
<li><strong>The client's goal</strong> in one or two sentences, in their words.</li>
<li><strong>Your approach</strong> — briefly, how you'll get there.</li>
<li><strong>Deliverables</strong> — a specific list.</li>
<li><strong>Timeline</strong> — start date, milestones, delivery date.</li>
<li><strong>Revisions</strong> — how many rounds are included.</li>
<li><strong>Exclusions</strong> — what's not included.</li>
<li><strong>Price</strong> — total, or per option.</li>
<li><strong>Payment terms</strong> — deposit, schedule, accepted methods.</li>
<li><strong>Validity</strong> — for example, “valid for 14 days”.</li>
<li><strong>Next step</strong> — “Reply to accept and I'll send the agreement and deposit invoice.”</li>
</ol>
''' + cta("quotation-generator", "Create a quote in minutes", "Your details, line items, terms and validity — ready to send.", "Open quotation generator") + '''
<h2>Get the price right first</h2>
<p>A beautiful quote with the wrong number still loses — either the job or your profit. Break the work into tasks, estimate hours, apply your rate and add a buffer. Our guide to <a href="/blog/how-to-price-a-website-project/">pricing a website project</a> walks through the method with an example.</p>
''' + cta("project-quote-calculator", "Calculate the price", "Tasks, hours, buffer, rush fee and deposit in one place.", "Open quote calculator") + '''
<h2>Offer options</h2>
<p>A single price invites a yes-or-no decision. Three options invite a choice:</p>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>What's included</th></tr></thead>
<tbody>
<tr><td>Essential</td><td>The core deliverable, standard timeline</td></tr>
<tr><td>Recommended</td><td>Core + the extras most clients need</td></tr>
<tr><td>Complete</td><td>Everything, plus priority delivery or support</td></tr>
</tbody></table></div>
<p>Most clients pick the middle option, so make it the one you'd most like to do.</p>

<h2>A simple template</h2>
<pre class="gen-out" style="margin-bottom:1.3em">Quotation for [client] — [project name]
Date: [date]   Valid until: [date + 14 days]

Your goal
[One or two sentences in the client's words.]

What I'll deliver
- [Deliverable 1]
- [Deliverable 2]
- [Two rounds of revisions]

Not included
- [Hosting / copywriting / printing]

Timeline
Start [date] · first draft [date] · final delivery [date]

Investment
Option A — [price]   Option B — [price]   Option C — [price]

Payment terms
50% to start, 50% on delivery. Bank transfer / Payoneer.

Next step
Reply “approved” with your chosen option and I'll send the agreement and first invoice.</pre>

<h2>Common mistakes</h2>
<ul>
<li><strong>Vague scope</strong> — the main cause of <a href="/blog/scope-creep-freelancers/">scope creep</a>.</li>
<li><strong>No validity date</strong> — a six-month-old quote at last year's price.</li>
<li><strong>Hiding the price</strong> at the bottom of long text.</li>
<li><strong>Too many options</strong> — more than three makes choosing harder.</li>
</ul>

<h2>Follow up</h2>
<p>If you don't hear back in three to five days, send a short note: “Just checking whether you had any questions about the quote — happy to adjust the scope if needed.” Many deals close on the follow-up.</p>
''' + cta("freelance-contract-generator", "Turn the quote into an agreement", "Scope, payment and revisions in plain language.", "Open contract generator"),
    "faq": [
        ("What should a freelance quotation include?", "The client's goal, deliverables, timeline, revisions, exclusions, price or options, payment terms, a validity date and the next step."),
        ("What is the difference between a quote and an estimate?", "A quote is a fixed offer for a defined scope; an estimate is an approximate figure that may change."),
        ("How long should a quote be valid?", "Fourteen to thirty days is common. A validity date protects you if costs or your availability change."),
        ("How do I follow up on a quote?", "After three to five days, send a short, friendly message asking if they have questions and offering to adjust the scope."),
    ],
})

# ------------------------------------------------------------------ 2026-12-06
POSTS.append({
    "slug": "fiverr-gig-packages-guide", "image": "/assets/img/blog/fiverr-gig-packages-guide",
    "alt": "Glass tiles with stacked layers, a package box and a tag icon on a dark gradient background",
    "title": "Fiverr Gig Packages: How to Structure Basic, Standard and Premium",
    "h1": "Fiverr gig packages: Basic, Standard and Premium",
    "desc": "How to structure Fiverr gig packages: what goes in Basic, Standard and Premium, how to price each after Fiverr's 20% fee, using gig extras, and mistakes that cost sellers orders.",
    "lede": "Three packages turn one gig into three price points — and nudge buyers towards the middle. Here's how to build them so each one makes sense and pays you properly.",
    "date": "2026-12-06", "cat": "Fiverr", "icon": "list",
    "tools": ["fiverr-reverse-fee-calculator", "fiverr-fee-calculator", "fiverr-gig-character-counter"],
    "body": takeaways([
        "<strong>Basic</strong> lowers the barrier, <strong>Standard</strong> is the one you want most buyers to pick, <strong>Premium</strong> is for buyers who want everything.",
        "Each step up should add <strong>clear, visible value</strong>: more units, more revisions, faster delivery, source files.",
        "Price from your <strong>take-home</strong>: Fiverr keeps 20% of every package and extra.",
        "Use <strong>gig extras</strong> for add-ons that don't fit every buyer.",
    ]) + '''
<h2>Why three packages work</h2>
<p>With one price, buyers decide yes or no. With three, they compare — and many pick the middle option as a safe choice. A strong Premium also makes Standard look like good value, and the Basic package lets new buyers try you with low risk.</p>

<h2>What goes in each package</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Basic</th><th>Standard</th><th>Premium</th></tr></thead>
<tbody>
<tr><td>Purpose</td><td>Entry point</td><td>Best value — your main package</td><td>Everything, fastest</td></tr>
<tr><td>Example: logo design</td><td>1 concept, PNG</td><td>3 concepts, PNG + SVG, social kit</td><td>5 concepts, full source files, brand guide</td></tr>
<tr><td>Revisions</td><td>1</td><td>3</td><td>Unlimited within scope</td></tr>
<tr><td>Delivery</td><td>Standard</td><td>Standard</td><td>Faster</td></tr>
</tbody></table></div>
<p>Make the differences easy to see at a glance. If buyers can't tell why Standard costs more than Basic, they'll choose Basic.</p>

<h2>Pricing the packages</h2>
<p>Start with what you want to <strong>keep</strong> for each package, then gross up for Fiverr's 20% fee:</p>
<p class="formula">Package price = target take-home ÷ 0.80</p>
<p>For example, to keep $40, $100 and $200, price the packages at $50, $125 and $250. Remember the <strong>$3 Payoneer withdrawal fee</strong> is charged per withdrawal, not per order — so it matters less the more you withdraw at once.</p>
''' + cta("fiverr-reverse-fee-calculator", "Price each package", "Enter what you want to keep — get the price to list.", "Open reverse calculator") + '''
<h3>Spacing the prices</h3>
<ul>
<li>A common pattern is roughly <strong>1× : 2–3× : 4–6×</strong> from Basic to Premium.</li>
<li>Don't make Basic so cheap that it attracts buyers who want Premium work for Basic money.</li>
<li>Make sure every package pays your <strong>minimum hourly rate</strong> for the time it really takes.</li>
</ul>

<h2>Use gig extras</h2>
<p>Gig extras are add-ons buyers can pick with any package: faster delivery, extra revisions, source files, additional pages or words. Use them for things only some buyers need, so your packages stay simple. Extras are fee'd at 20% too, so price them the same way.</p>
''' + cta("fiverr-fee-calculator", "Check an order with extras", "Package plus extras, minus Fiverr's fee — your real earnings.", "Open Fiverr calculator") + '''
<h2>Package titles and descriptions</h2>
<ul>
<li>Give each package a <strong>short, descriptive name</strong> (“Starter logo”, “Brand kit”, “Full identity”) rather than repeating Basic/Standard/Premium.</li>
<li>Describe the <strong>outcome</strong>, not just the features.</li>
<li>Keep within Fiverr's character limits — check before you publish.</li>
</ul>
''' + cta("fiverr-gig-character-counter", "Check the character limits", "Titles, descriptions, package names and tags.", "Open gig counter") + '''
<h2>Mistakes to avoid</h2>
<ul>
<li><strong>Three nearly identical packages</strong> with only delivery time different.</li>
<li><strong>Unlimited revisions on Basic</strong> — an open invitation to endless changes.</li>
<li><strong>Prices that ignore the fee</strong>, leaving you working for 80% of what you meant to charge.</li>
<li><strong>Never reviewing them.</strong> Watch which package sells and adjust every few months.</li>
</ul>
<p>Packages that sell well also help you reach the order and earnings thresholds for <a href="/blog/fiverr-seller-levels-explained/">Fiverr seller levels</a>.</p>
''',
    "faq": [
        ("How should I price Fiverr gig packages?", "Decide what you want to keep for each package and divide by 0.8 to cover Fiverr's 20% fee. A spacing of roughly 1× : 2–3× : 4–6× is common."),
        ("What should go in the Basic package on Fiverr?", "A small, clearly defined version of your service that lets new buyers try you, with limited revisions."),
        ("Does Fiverr take a fee on gig extras?", "Yes. The 20% seller fee applies to the full order, including extras and tips."),
    ],
})

# ------------------------------------------------------------------ 2026-12-09
POSTS.append({
    "slug": "freelancer-profile-that-gets-hired", "image": "/assets/img/blog/freelancer-profile-that-gets-hired",
    "alt": "Glass tiles with a user badge, a star and a briefcase icon on a dark gradient background",
    "title": "How to Write a Freelancer Profile That Gets Hired",
    "h1": "How to write a freelancer profile that gets hired",
    "desc": "How to write a freelancer profile that gets hired on Fiverr, Upwork and similar sites: a specific headline, a client-focused bio, portfolio proof, a professional photo and a clear call to action.",
    "lede": "Clients scan dozens of profiles. The ones that win answer three questions fast: what do you do, for whom, and why should I trust you?",
    "date": "2026-12-09", "cat": "Winning work", "icon": "user",
    "tools": ["fiverr-profile-bio-generator", "upwork-proposal-generator", "fiverr-gig-character-counter"],
    "body": takeaways([
        "Use a <strong>specific headline</strong>: the service, the client type and the result.",
        "Write the bio about the <strong>client's problem</strong>, then how you solve it.",
        "Show <strong>proof</strong>: portfolio pieces, results and reviews.",
        "End with a <strong>clear next step</strong> — what to send you to get started.",
    ]) + '''
<h2>1. A headline that says exactly what you do</h2>
<p>“Graphic designer” competes with thousands of profiles. “Logo and brand designer for restaurants and cafés” stands out to the right client.</p>
<ul>
<li><strong>Weak:</strong> Web developer | Hardworking | Available 24/7</li>
<li><strong>Strong:</strong> WordPress developer for small businesses — fast, mobile-friendly sites</li>
</ul>
<p>On Upwork the title is especially important because clients see it in search results next to your rate.</p>

<h2>2. A bio that starts with the client</h2>
<p>Most bios start with “I am…” and a list of skills. Clients care more about their own problem. A simple structure:</p>
<ol>
<li><strong>The problem</strong> your ideal client has.</li>
<li><strong>What you do</strong> about it, and how.</li>
<li><strong>Proof</strong>: experience, results, notable clients (only with permission).</li>
<li><strong>How you work</strong>: communication, timelines, what makes working with you easy.</li>
<li><strong>Call to action</strong>: what to send you to get started.</li>
</ol>
''' + cta("fiverr-profile-bio-generator", "Draft your bio", "Answer a few questions — get a client-focused profile description.", "Open bio generator") + '''
<h2>3. Proof beats claims</h2>
<ul>
<li><strong>Portfolio:</strong> your best 3–6 pieces, closely related to the work you want more of.</li>
<li><strong>Results:</strong> real outcomes you can stand behind — for example, a page that loads faster, a design that was approved first time.</li>
<li><strong>Reviews:</strong> on a new profile, a few smooth small orders build reviews quickly — see <a href="/blog/how-to-get-first-order-on-fiverr/">getting your first Fiverr order</a>.</li>
</ul>
<p>Never use work you didn't do or claim results you can't support. Clients do check.</p>

<h2>4. Photo and details</h2>
<ul>
<li>A clear, friendly <strong>photo of your face</strong> with good light and a plain background.</li>
<li><strong>Skills and tags</strong> that match what clients search for.</li>
<li><strong>Languages</strong> with honest proficiency levels.</li>
<li>Complete every section — incomplete profiles look inactive.</li>
</ul>

<h2>5. Fiverr vs Upwork profiles</h2>
<h3>Fiverr</h3>
<p>Buyers mostly find you through gigs, so your profile supports them. Keep the description short and trustworthy, and let the gigs do the selling. Check the character limits for each field.</p>
<h3>Upwork</h3>
<p>Your profile is read alongside every proposal. Use the overview to show the specific value you bring, and consider specialised profiles if you offer two distinct services. Your proposals should match the profile's focus — our <a href="/blog/how-to-write-upwork-proposal/">Upwork proposal guide</a> shows how.</p>
''' + cta("upwork-proposal-generator", "Write a matching proposal", "A short, specific proposal that mirrors the client's brief.", "Open proposal generator") + '''
<h2>A short example</h2>
<pre class="gen-out" style="margin-bottom:1.3em">Your website should bring you customers — not just look nice.

I build fast, mobile-friendly WordPress sites for small businesses: restaurants, clinics, shops and consultants. Every site is set up for search engines, loads quickly on phones, and is easy for you to update.

You'll get clear updates at every step and a site delivered on the date we agree.

Send me your current website (if any) and two sites you like, and I'll reply with a plan and price within a day.</pre>

<h2>Review it every few months</h2>
<p>As your skills, portfolio and ideal client change, update your headline, bio and samples. A profile that matches the work you want attracts more of that work.</p>
''' + cta("fiverr-gig-character-counter", "Check your text fits", "Character counts for Fiverr profile and gig fields.", "Open gig counter"),
    "faq": [
        ("What should I write in my freelancer profile?", "A specific headline, a bio that starts with the client's problem and how you solve it, proof such as portfolio and reviews, and a clear next step."),
        ("How long should a freelancer bio be?", "Long enough to answer what you do, for whom and why to trust you — usually a few short paragraphs. Keep within each platform's character limits."),
        ("Should I use a real photo on my freelance profile?", "Yes. A clear, friendly photo of your face builds trust with clients."),
    ],
})

# ------------------------------------------------------------------ 2026-12-12
POSTS.append({
    "slug": "receive-international-payments-pakistan", "image": "/assets/img/blog/receive-international-payments-pakistan",
    "alt": "Glass tiles with a globe, a landmark bank building and a wallet icon on a dark gradient background",
    "title": "How to Receive International Payments in Pakistan: Options Compared",
    "h1": "Ways to receive international payments in Pakistan, compared",
    "desc": "Payoneer, direct bank transfer, freelancer foreign-currency accounts and Wise compared for Pakistani freelancers: fees, exchange rates, PRCs and which to use for platform and direct clients.",
    "lede": "PayPal isn't available for Pakistani accounts, so freelancers rely on other routes. Here's how each works, what it costs and when to use it.",
    "date": "2026-12-12", "cat": "Payments", "icon": "globe",
    "tools": ["wise-vs-payoneer-vs-bank", "payoneer-to-pkr-calculator", "pakistan-freelancer-tax-calculator", "freelancer-currency-converter"],
    "body": takeaways([
        "<strong>Payoneer</strong> is the main route for Fiverr (flat <strong>$3 per withdrawal</strong>) and other platforms, and can receive direct client payments.",
        "<strong>Direct bank transfer (SWIFT)</strong> to a Pakistani bank works for larger direct clients; intermediary charges can apply.",
        "SBP rules let freelancers keep part of their export income in a <strong>foreign currency account</strong>.",
        "Always use the right <strong>purpose code</strong> and keep your <strong>PRCs</strong> for tax.",
    ]) + '''
<h2>The main options</h2>
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>Best for</th><th>Main costs</th></tr></thead>
<tbody>
<tr><td>Payoneer → Pakistani bank</td><td>Fiverr, Upwork and other platforms; small and medium direct payments</td><td>Platform withdrawal fee, conversion markup, receiving fees on some direct payments, annual fee if inactive/low volume</td></tr>
<tr><td>Direct bank transfer (SWIFT)</td><td>Larger payments from direct clients</td><td>Sender's bank fee, possible intermediary deductions, your bank's exchange rate</td></tr>
<tr><td>Freelancer foreign-currency account</td><td>Keeping part of your income in dollars</td><td>Bank-specific charges</td></tr>
<tr><td>Wise</td><td>Clients sending to your PKR bank account</td><td>Wise's fee to the sender; limited for Pakistan residents (see below)</td></tr>
</tbody></table></div>

<h2>Payoneer</h2>
<p>For most Pakistani freelancers, Payoneer is the default. Fiverr pays out to Payoneer with a <strong>flat $3 per withdrawal</strong>; Upwork and other platforms also support it. Payoneer can also give you receiving account details so direct clients can pay you.</p>
<p>When you withdraw to a Pakistani bank, Payoneer converts to PKR with a markup on the exchange rate. Our guide to <a href="/blog/payoneer-fees-pakistan/">Payoneer fees in Pakistan</a> covers every charge, including the annual fee.</p>
''' + cta("payoneer-to-pkr-calculator", "See your rupees", "Payoneer balance to the PKR that reaches your bank.", "Open Payoneer to PKR") + '''
<h2>Direct bank transfer (SWIFT)</h2>
<p>Direct clients can send money by international wire to your Pakistani bank account using your IBAN and the bank's SWIFT code. It's often good value for larger amounts, but:</p>
<ul>
<li>The sender's bank charges a fee, and <strong>intermediary banks</strong> may deduct charges along the way.</li>
<li>Your bank converts at its own buying rate unless you hold a foreign currency account.</li>
<li>Ask the client to mark the payment as payment for services so it's classified correctly.</li>
</ul>

<h2>Freelancer foreign-currency accounts</h2>
<p>The State Bank of Pakistan has introduced rules that let IT and freelance exporters keep part of their export proceeds in foreign currency. Under SBP's 2023 changes, freelancers can retain the higher of 50% of their proceeds or USD 5,000 per month in a foreign currency account, and banks offer digital accounts for freelancers that can be opened online. Holding dollars helps if you pay for software in dollars or want to choose when to convert. Ask your bank about its freelancer account, limits and charges.</p>

<h2>Wise</h2>
<p>At the time of writing (October 2026), Wise does <strong>not</strong> offer full multi-currency accounts to Pakistan residents — you can't hold USD balances or get Wise account details. Clients abroad can still use Wise to <strong>send PKR to your Pakistani bank account</strong>.</p>
<p>In August 2026, PSEB's CEO told TechJuice that Wise accounts for Pakistani freelancers were expected within weeks, but Wise had not confirmed it. Check Wise's own website for current availability before relying on it.</p>
''' + cta("wise-vs-payoneer-vs-bank", "Compare the routes", "Fees and exchange rates side by side on your amount.", "Compare now") + '''
<h2>Purpose codes and PRCs</h2>
<p>When foreign money arrives, your bank records a <strong>purpose code</strong> describing the payment. For IT and IT-enabled services exports, code <strong>9186</strong> is commonly used. The correct code matters because it's how your income is recognised as an export of services for tax purposes.</p>
<p>Your bank can issue a <strong>Proceeds Realisation Certificate (PRC)</strong> for these remittances. Keep them with your tax records — see our <a href="/blog/prc-proceeds-realisation-certificate-pakistan/">PRC guide</a>.</p>
''' + cta("pakistan-freelancer-tax-calculator", "Estimate tax on remittances", "0.25% with PSEB registration vs 1% without.", "Open tax calculator") + '''
<h2>Which should you use?</h2>
<ul>
<li><strong>Selling on Fiverr or Upwork:</strong> Payoneer. Withdraw in larger amounts to spread the $3 fee.</li>
<li><strong>Large direct client payments:</strong> compare Payoneer receiving with a direct bank transfer on the final rupees received.</li>
<li><strong>Want to keep some dollars:</strong> open a freelancer foreign currency account with your bank.</li>
<li><strong>Client already uses Wise:</strong> they can send PKR to your bank.</li>
</ul>
<p>Whatever you choose, compare on the <strong>final amount received</strong> — see our explainer on the <a href="/blog/mid-market-exchange-rate-explained/">mid-market rate</a>.</p>
<p class="hint">General information as of October 2026, not financial advice. Availability, fees and SBP rules change — confirm with your bank, Payoneer, Wise and SBP before deciding.</p>
''',
    "faq": [
        ("Can I use PayPal in Pakistan to receive payments?", "No. PayPal doesn't offer accounts to Pakistan residents, so freelancers use Payoneer, bank transfers and other routes."),
        ("What is the best way to receive payments from Fiverr in Pakistan?", "Payoneer. Fiverr charges a flat $3 per withdrawal to Payoneer, and you can then withdraw to a Pakistani bank account."),
        ("Can Pakistani freelancers keep income in dollars?", "Yes, partly. SBP rules let freelancers retain the higher of 50% of export proceeds or USD 5,000 per month in a foreign currency account."),
        ("Is Wise available in Pakistan?", "At the time of writing, Wise doesn't offer full accounts to Pakistan residents, though clients can send PKR to Pakistani bank accounts through Wise. Check Wise's website for updates."),
        ("Which purpose code should freelancers use?", "Code 9186 is commonly used for IT and IT-enabled services exports. Confirm with your bank."),
    ],
})
