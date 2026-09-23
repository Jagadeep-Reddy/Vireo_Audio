"""
app.py — Lightweight Web Dashboard for Vireo Audio CX Intelligence
Starts with: python app.py
Serves at: http://127.0.0.1:5000
"""

import os
import math
from flask import Flask, jsonify, request, render_template
from engine import load_and_clean_data, get_weekly_kpis, get_leaderboard, generate_digest

app = Flask(__name__)

# Preload data on startup
print("Initializing Vireo CX Engine...")
TICKETS, AGENTS, ORDERS, PRODUCTS, CUSTOMERS = load_and_clean_data(".")
AVAILABLE_WEEKS = sorted(TICKETS['iso_week'].dropna().unique().tolist())
print(f"Engine ready: {len(TICKETS)} tickets, {len(AGENTS)} agents across {len(AVAILABLE_WEEKS)} weeks.")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/weeks")
def api_weeks():
    return jsonify(AVAILABLE_WEEKS)


@app.route("/api/digest")
def api_digest():
    week = request.args.get("week", AVAILABLE_WEEKS[-1])
    return jsonify(generate_digest(TICKETS, week))


@app.route("/api/leaderboard")
def api_leaderboard():
    week = request.args.get("week")
    tier = request.args.get("tier")
    team = request.args.get("team")
    lb = get_leaderboard(TICKETS, AGENTS, week=week, tier=tier, team=team)
    records = lb.to_dict(orient="records")
    for r in records:
        for k, v in r.items():
            if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
                r[k] = None
    return jsonify(records)


@app.route("/api/leakage")
def api_leakage():
    dips = TICKETS[TICKETS['is_double_dip']][
        ['ticket_id', 'order_id', 'customer_id', 'refund_amount_inr', 'replacement_issued']
    ].to_dict(orient="records")
    gw = TICKETS[TICKETS['is_gw_overcap']][
        ['ticket_id', 'customer_id', 'refund_amount_inr', 'refund_reason_code', 'assigned_team']
    ].sort_values(by='refund_amount_inr', ascending=False).to_dict(orient="records")
    return jsonify({"double_dips": dips, "goodwill": gw})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Dashboard running at http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
