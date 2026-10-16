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
    "desc": "Step-by-step guide to withdrawing Fiverr earnings in Pakistan through Payoneer: clearance period, the $3 withdrawal fee, converting to PKR, Proof of Remittance and how to keep more of every withdrawal.",
    "lede": "From a completed order to rupees in your bank account — every step, every fee, and the small habits that save you thousands of rupees a year.",
    "date": "2026-10-15", "cat": "Payments", "icon": "bank",
    "tools": ["fiverr-fee-calculator", "payoneer-to-pkr-calculator", "pakistan-freelancer-tax-calculator"],
    "body": takeaways([
        "In Pakistan, Fiverr pays out through <strong>Payoneer</strong>. Even the “bank transfer” option runs through Payoneer.",
        "Fiverr charges a flat <strong>$3 per withdrawal</strong>, not per order — so withdrawing in batches saves money.",
        "Payoneer converts dollars to rupees at a rate up to about <strong>2% below mid-market</strong>.",
        "Keep the bank's <strong>Proof of Remittance Certificate (PRC)</strong> — it supports the low tax rate on IT exports.",
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
<li><strong>Keep every PRC.</strong> Ask your bank for the Proof of Remittance Certificate for each transfer. It documents your income as an IT export, which is what lets you pay the reduced final tax.</li>
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
<li><strong>Collect a PRC for every remittance.</strong> The Proof of Remittance Certificate from your bank is your evidence of export income.</li>
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
<p>Keep a copy of every invoice alongside the matching payment record. In Pakistan, match each invoice to the bank's Proof of Remittance Certificate — together they show your income is IT export, which supports the reduced tax rate explained in our <a href="/blog/pseb-registration-freelancers-tax-pakistan/">PSEB guide</a>.</p>
''',
    "faq": [
        ("Do I need to send invoices for Fiverr or Upwork orders?", "Not for the platform — they create their own records. You need invoices for direct clients, and when a client asks for one."),
        ("What payment terms should freelancers use?", "Due within 7–14 days, with a 30–50% deposit upfront for new clients or larger projects."),
        ("What should I do if a client doesn't pay?", "Send polite reminders on the due date, at 7 days and at 14 days. Pause work if your agreement allows it, and keep all communication in writing."),
    ],
})
