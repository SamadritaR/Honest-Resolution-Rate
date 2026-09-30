"""
Honest Resolution Rate (HRR): reference implementation.

Reads a conversation log and reports, side by side:
  containment  = AI conversations that ended without a human transfer
  hrr          = AI conversations with a confirmed outcome AND no same intent
                 repeat contact from the same customer within the window,
                 over ALL conversations the AI started (abandoned included)

Expected CSV columns:
  conversation_id, customer_id, intent, channel, started_at (ISO 8601),
  handled_by (ai | human), transferred (true | false),
  outcome_confirmed (true | false), ended_by_silence (true | false)

Usage:
  python src/hrr.py examples/sample_conversations.csv --window-days 7
"""
import argparse, csv
from collections import defaultdict
from datetime import datetime, timedelta

TRUE = {"true", "1", "yes", "y"}

def load(path):
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            r["started_at"] = datetime.fromisoformat(r["started_at"])
            for k in ("transferred", "outcome_confirmed", "ended_by_silence"):
                r[k] = r[k].strip().lower() in TRUE
            rows.append(r)
    return rows

def repeat_contacts(rows, window):
    """Return ids of conversations followed by a same customer, same intent
    contact on ANY channel within the window."""
    by_key = defaultdict(list)
    for r in rows:
        by_key[(r["customer_id"], r["intent"])].append(r)
    flagged = set()
    for convs in by_key.values():
        convs.sort(key=lambda r: r["started_at"])
        for a, b in zip(convs, convs[1:]):
            if b["started_at"] - a["started_at"] <= window:
                flagged.add(a["conversation_id"])
    return flagged

def compute(rows, window_days=7):
    window = timedelta(days=window_days)
    ai = [r for r in rows if r["handled_by"] == "ai"]
    repeats = repeat_contacts(rows, window)
    n = len(ai)
    contained = [r for r in ai if not r["transferred"]]
    honest = [r for r in ai
              if not r["transferred"]
              and r["outcome_confirmed"]
              and not r["ended_by_silence"]
              and r["conversation_id"] not in repeats]
    dates = sorted(r["started_at"] for r in ai)
    channels = sorted({r["channel"] for r in ai})
    return {
        "n": n,
        "total_volume": len(rows),
        "containment": len(contained) / n if n else 0,
        "hrr": len(honest) / n if n else 0,
        "silence": sum(r["ended_by_silence"] and not r["transferred"] for r in ai),
        "repeat_voided": sum(r["conversation_id"] in repeats and not r["transferred"] for r in ai),
        "start": dates[0].date() if dates else None,
        "end": dates[-1].date() if dates else None,
        "channels": channels,
        "window_days": window_days,
    }

def label(m, judge="rules on system of record", split="AI only"):
    share = m["n"] / m["total_volume"] if m["total_volume"] else 0
    return (f"HRR {m['hrr']:.0%} | n = {m['n']:,} AI conversations | "
            f"{m['start']} to {m['end']} | {' and '.join(m['channels'])}, "
            f"{share:.0%} of total volume | {m['window_days']} day same intent window | "
            f"judged by {judge} | {split}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("log")
    p.add_argument("--window-days", type=int, default=7)
    a = p.parse_args()
    m = compute(load(a.log), a.window_days)
    print(f"Containment (no transfer):          {m['containment']:.1%}")
    print(f"Honest Resolution Rate:             {m['hrr']:.1%}")
    print(f"Gap:                                {(m['containment']-m['hrr'])*100:.1f} points")
    print(f"  ended in silence, counted as contained: {m['silence']}")
    print(f"  voided by repeat contact:               {m['repeat_voided']}")
    print()
    print(label(m))
