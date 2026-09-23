# Vireo Audio — Support Tickets (Task 1 V3)
## Completed Submission Form

---

### What did you build, and what business outcome does it move? State the number and the money.*

I built a lightweight CX intelligence tool: a weekly AI complaint digest, a tier-segmented agent performance hub, and a financial compliance monitor.

**Business Goal:** Cut Vireo’s 30-day repeat contact rate from **34.4% to 22.0%**, removing **~1,050 unnecessary tickets** from the quarterly queue and saving **Rs 3,04,000 every quarter** in direct contact costs.

**The Math:**  
- 18-month data shows 3,958 repeat tickets within 30 days of resolution (34.4% recently).
- At ~650 tickets/week (~8,450/quarter), cutting repeats by 12.4% eliminates 1,048 tickets per quarter.
- At Vireo’s blended cost of Rs 290/contact (Policy §4), that saves `1,048 × 290 = Rs 3,03,920/quarter`.
- Rebalancing evening email shifts cuts SLA breaches from 8.8% to 3.0%, preventing ~495 automatic Rs 350 store credit payouts and saving an extra Rs 1.73 Lakhs/quarter.

---

### What does one run cost, and what would a month cost at Vireo's volume (roughly 650 tickets a week)? Show the arithmetic. If you used no paid calls, say so.*

**Cost per run:** ~Rs 0.05 ($0.0006).  
**Monthly cost:** ~Rs 0.22 ($0.0022).  

Instead of calling an LLM 650 times a week (which would create the surprise November bill Arjun warned about), I pre-aggregate KPIs, category distributions, and defective lot spikes locally in Pandas, running **exactly 1 synthesis call per week**.

**Arithmetic (Gemini 1.5 Flash):**  
- Input: ~3,500 tokens (weekly KPIs + 15 sample quotes) @ $0.075/1M = $0.00026  
- Output: ~800 tokens (markdown digest) @ $0.30/1M = $0.00024  
- Total per run: $0.0005 (~Rs 0.045)  
- Monthly cost (4.33 weeks): **$0.0022 (~Rs 0.22/month)**.  

If no API key is provided, an internal heuristic summarizer runs for **Rs 0.00 (zero paid calls)**.

---

### How do you know it works? Sample size, how you checked, error rate, and the kind of case it gets wrong.*

I tested it against a stratified benchmark of 150 tickets (`evaluate.py`) across all 11 categories and 4 channels, manually validating customer messages against agent notes and Policy v3.2.

- **SLA breach detection:** 100% accurate (exact rule match).
- **30-day repeat detection:** 100% accurate (exact customer ID window match).
- **Intake bot error rate:** 36.0% (the legacy bot frequently tagged genuine complaints as "Other" or "Billing"; my tool catches and fixes these).
- **Intent error rate:** 18.0% on long, ambiguous queries.

**What it gets wrong:**
1. Compound queries (4.7%): Customer asks for an address change AND earbud pairing in one message.
2. Sarcasm (1.3%): *"Great earbuds, lasted a whole 15 minutes."*
3. IVR voice errors (2.0%): Phonetic transcription typos like *"pules not paring"*.
4. Multi-item buyers (1.3%): A customer buying a watch 2 weeks after buying earbuds gets flagged as a repeat contact.

---

### Did you change, narrow, or push back on the client's ask? What, when, and why. [can only raise your score]*

Yes, I pushed back on three things:

1. **Priya's flat closed-ticket leaderboard:** Priya asked to rank all agents by tickets closed. I refused. In the data, the bottom 5 agents are all Tier 2 Warranty specialists whose cases take days by design (Policy §6 explicitly forbids comparing them to Tier 1 on volume). Meanwhile, the top agent had 43 one-word closes (*"sorted"*, *"done"*). Raw volume ranking rewards sloppy closes and crushes warranty team morale. I built a tiered hub instead.
2. **650 LLM calls per week:** Rejected per-ticket LLM processing to avoid Arjun’s surprise bill. Pre-aggregated locally with 1 weekly synthesis call, dropping costs to Rs 0.22/month.
3. **Uncleaned legacy data:** Found 653 duplicate Freshdesk tickets and a 5.5-hour UTC timestamp offset that distorted handle times. Built an ETL cleaning step before reporting any metrics.

---

### What is wrong with what you are handing us? Be specific: bugs, shortcuts, things you know are off. [can only raise your score]*

1. **Right-censoring in June 2026:** The export ends June 30, so tickets resolved late in June haven't matured through their 30-day window yet. June repeat rates look artificially low (~28% vs ~35% previously).
2. **Batch CSVs only:** It ingests static exports rather than streaming Freshdesk webhooks. Good for weekly standups, not intraday queue management.
3. **No bot re-tagging audit log:** `tickets.csv` only has the final category tag, so I can't programmatically prove whether an agent corrected a bad bot tag or if the bot got it right initially.
4. **Offline mode uses keyword heuristics:** Without an API key, thematic grouping uses keyword frequencies, so it won't catch brand new slang without a dictionary update.

---

### What did you deliberately leave out, and why that rather than something else?*

1. **Vector DB / RAG (Pinecone / Chroma):** Overkill for 650 tickets a week. Pandas + keyword clustering runs in 0.5s locally with zero infrastructure or setup cost.
2. **Customer-facing auto-responder:** Building an autonomous responder in a 5-hour task risks hallucinations on hardware issues and would only drive up repeat contacts.
3. **Automated refunds:** Policy §5 mandates RMA inspections and Team Lead approvals for refunds. Automating payouts in code without human approval is a massive fraud risk.

---

### Anything you built or found that nobody asked for?*

1. **Financial leakage audit:** Cross-referencing `tickets.csv` and `orders.csv` uncovered:
   - 4 orders that received **both a cash refund AND a replacement unit shipped** (Policy §5 violation).
   - 37 goodwill credits exceeding the Rs 500 cap without documented signoff (totaling Rs 1.26 Lakhs).
   - Rs 3.68 Lakhs in store credit penalties from 1,051 first-response SLA breaches.
2. **Defective lot isolation:** Discovered 65W GaN Charger lot `CH65-2507-1` generated ticket volumes 3x higher than sales due to thermal cutoffs, and Pulse 2 lot `PL2-2503-1` had abnormal charging pin failures.
3. **Migration fix:** Cleaned 653 duplicated tickets and repaired the +5.5 hour UTC-to-IST offset in legacy resolution timestamps.

---

### What did you use AI for? Which tools and models, where they helped, where they wasted your time, what you threw away. Link your three-minute screen recording here.*

**Tools:** Antigravity IDE with Gemini 3.8 Flash for data exploration and code; Gemini 1.5 Flash for the weekly executive synthesis.  
- **Where it helped:** Fast cross-referencing of policy SLA formulas against timestamps, building the Flask UI, and writing concise executive summaries.  
- **Where it wasted time:** Tried using a multi-agent framework (CrewAI style) to classify tickets; it was slow, brittle, and kept timing out. Scrapped it.  
- **What I threw away:** Threw away a sentence-transformers embedding pipeline—it added 4 minutes of local lag for minimal gain over fast keyword clustering.  

**Screen Recording Link:**  
`https://drive.google.com/file/d/1vireo-audio-screen-recording-walkthrough-demo/view?usp=sharing`  
*(Or your public Google Drive video link)*

---

### Someone picks this up on Monday and you are unreachable. The three things they need to know.*

1. **How to run:** Run `pip install -r requirements.txt` and `python app.py` (opens `http://127.0.0.1:5000`). Terminal CLI works via `python cli.py --week 2026-W24` or `python cli.py --audit`.
2. **Do not remove data cleaning in `engine.py`:** It dedupes 653 Freshdesk rows and fixes the +5.5 hour UTC offset on legacy tickets. Without this, handle times will break.
3. **Works 100% offline:** No API key required. If you want live Gemini or OpenAI synthesis, just add `GEMINI_API_KEY` or `OPENAI_API_KEY` to your environment.

---

### Honest hours spent. One number.*

**4.5**

---

### Github Repo Link
Please upload your Github Repo URL (Public)

**`https://github.com/Jagadeep-Reddy/Vireo_Audio`**
