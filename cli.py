"""
cli.py — Command Line Interface wrapper for Vireo Audio Intelligence
Usage:
  python cli.py --week 2026-W24
  python cli.py --business-goal
  python cli.py --audit
  python cli.py --leaderboard
"""
import sys
from engine import (
    load_and_clean_data, get_weekly_kpis, get_leaderboard,
    generate_digest
)

if __name__ == "__main__":
    import engine
    # Directly invoke engine's CLI
    import argparse
    parser = argparse.ArgumentParser(description="Vireo CX Engine CLI")
    parser.add_argument("--week", type=str, help="ISO week (e.g. 2026-W24)")
    parser.add_argument("--audit", action="store_true", help="Audit double dipping & goodwill overcaps")
    parser.add_argument("--business-goal", action="store_true", help="Display quantified business goal")
    parser.add_argument("--leaderboard", action="store_true", help="Display agent leaderboard")
    parser.add_argument("--tier", type=int, choices=[1, 2], help="Filter leaderboard by Tier")
    args = parser.parse_args()

    tickets, agents, orders, products, customers = load_and_clean_data(".")
    available_weeks = sorted(tickets['iso_week'].dropna().unique())
    selected_week = args.week if args.week else available_weeks[-1]

    if args.audit:
        print("\n=== FINANCIAL COMPLIANCE AUDIT (Policy §5) ===")
        dips = tickets[tickets['is_double_dip']][['ticket_id', 'order_id', 'refund_amount_inr', 'replacement_issued']]
        print(f"\n[VIOLATION] Double-Dipping: {len(dips)} occurrences")
        print(dips.to_string(index=False))
        gw = tickets[tickets['is_gw_overcap']]
        print(f"\n[VIOLATION] Goodwill Over Rs 500: {len(gw)} tickets (Rs {gw['refund_amount_inr'].sum():,})")
        print(gw[['ticket_id', 'refund_amount_inr', 'assigned_team']].head(5).to_string(index=False))
    elif args.business_goal:
        print("\n=== QUANTIFIED BUSINESS GOAL ===")
        print(">> 'Cut 30-day repeat contact rate from 34.4% to 22.0%, taking ~1,050 unnecessary contacts")
        print("    out of the quarterly queue and saving Rs 3,04,000/quarter in direct contact costs.'")
    elif args.leaderboard:
        print(f"\n=== AGENT LEADERBOARD — Week {selected_week} ===")
        lb = get_leaderboard(tickets, agents, selected_week, tier=args.tier)
        print(lb[['rank', 'name', 'team', 'tier', 'closed', 'avg_csat', 'fcr_pct', 'low_effort_pct']].head(10).to_string(index=False))
    else:
        res = generate_digest(tickets, selected_week)
        print(res['digest_markdown'])
