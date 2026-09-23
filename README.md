# Vireo Audio — CX Intelligence & Performance Hub (Task 1 V3)

A professional, production-grade AI support intelligence engine and executive dashboard for **Vireo Audio Pvt. Ltd.**, built to transform 18 months of customer support tickets into actionable weekly digests, fair agent performance scorecards, and financial leakage prevention.

---

## ⚡ 60-Second Quickstart (Clean Machine)

### 1. Prerequisites
- Python 3.9+ installed.

### 2. Installation
Clone the repository and install the lightweight dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Web Dashboard
```bash
python app.py
```
Open your browser and navigate to:
👉 **`http://127.0.0.1:5000`**

---

## 💻 Command Line Interface (CLI) Usage

You can also run all analytics, audits, and digest generations directly in the terminal:

```bash
# 1. View the Quantified Business Goal & ROI arithmetic
python cli.py --business-goal

# 2. Run the Financial & Compliance Audit (Double-dipping, Goodwill cap breaches, SLA penalties)
python cli.py --audit

# 3. Generate the Weekly AI Digest for a specific week (e.g. 2026-W24)
python cli.py --week 2026-W24

# 4. View the Fair Tiered Agent Leaderboard
python cli.py --leaderboard --week 2026-W24
python cli.py --leaderboard --tier 2  # Tier 2 Warranty agents
```

---

## 🧪 Accuracy & Validation Benchmark

To verify system accuracy, classification precision, and documented failure cases against our 150-ticket ground-truth benchmark:
```bash
python evaluate.py
```

---

## 🎯 The Quantified Business Goal

> **"Cut Vireo's 30-day repeat contact rate from 34.4% to 22.0%, taking ~1,050 unnecessary contacts out of the quarterly queue and saving Rs 3,04,000 per quarter in direct contact costs (at Rs 290 blended contact cost)."**

- **Secondary Recovery:** Cutting First-Response SLA breaches from 8.85% to 3.0% halts ~495 automatic Rs 350 store credit payouts (§3), adding an extra **Rs 1,73,250 per quarter** in bottom-line recovery.
- **Total Combined Quarterly Opportunity:** **~Rs 4.77 Lakhs / quarter**.

---

## 💡 Architecture & Key Design Decisions

1. **Hybrid Deterministic-LLM Pipeline (Cost Discipline):**  
   Rather than running 650 costly model calls every week (risking Arjun Mehta's "surprise model bill in November"), the tool pre-aggregates KPIs, category distributions, and defective lot spikes deterministically via Pandas. It then executes **1 single LLM call per week** with 15–20 high-signal customer quotes.
   - **Cost per weekly run:** **~$0.0006 (Rs 0.05)**.
   - **Cost per month at 650 tickets/week:** **~$0.0022 (Rs 0.22 / month)**.
   - **Offline Mode:** If no API key is provided, the engine runs a built-in **Deterministic Heuristic Synthesizer** at **Rs 0.00 / month**.
2. **Pushback on Priya's Naive Closed-Ticket Leaderboard:**  
   Per **Policy §6**, Tier 2 Escalations & Warranty cases are multi-touch, multi-day hardware cases that must not be evaluated on weekly closed ticket counts. A flat ranking unfairly places all 5 Tier 2 agents at the bottom of the company, while rewarding agents with 1-word notes (*"sorted ~Diya"*). Our tool provides a **Tier- and Team-Segmented Intelligence Hub** that audits note completeness, FCR, and resolution days.
3. **Data Migration Correction:**  
   Automatically deduplicates the 653 Freshdesk re-imported tickets and corrects the **+5.5 hour UTC timestamp offset** in legacy `resolved_at` timestamps (Policy §9).

---

## 🔑 Optional API Keys

To use live Gemini or OpenAI generation, set your API key in your terminal or a `.env` file:
```bash
# Optional for Google Gemini:
export GEMINI_API_KEY="your-key-here"  # On Linux/macOS
set GEMINI_API_KEY="your-key-here"     # On Windows CMD
$env:GEMINI_API_KEY="your-key-here"    # On Windows PowerShell

# Optional for OpenAI:
export OPENAI_API_KEY="your-key-here"
```
*(If no key is supplied, the tool runs seamlessly with the offline deterministic synthesizer).*

---

## 📁 Repository Structure

```
├── app.py                      # Flask Web Dashboard (59 lines)
├── engine.py                   # Core Engine: ETL, Policy Audit & AI Digest (214 lines)
├── cli.py                      # Command Line Interface tool (49 lines)
├── evaluate.py                 # 150-ticket validation suite & failure modes (48 lines)
├── templates/
│   └── index.html              # Sleek, interactive dashboard template
├── requirements.txt            # Minimal dependencies (flask, pandas, numpy)
├── memo-to-priya.md            # 1-Page non-technical executive memo for Priya Raman
├── submission-form.md          # Completed submission form with quantified ROI, failure modes & audit
├── tickets.csv                 # Raw dataset: 18 months of tickets
├── agents.csv                  # Roster data
├── orders.csv                  # Orders & lot codes
├── customers.csv               # Customer profiles & Care+ status
├── products.csv                # Product catalog & pricing
└── support-policy.pdf          # Vireo Support Operating Policy v3.2
```
