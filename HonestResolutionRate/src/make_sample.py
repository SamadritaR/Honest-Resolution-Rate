"""Generate a SYNTHETIC conversation log for demonstrating hrr.py.
These are not real vendor numbers. Rates below are assumptions for illustration."""
import csv, random
from datetime import datetime, timedelta
random.seed(7)
INTENTS = ["order_status", "refund", "address_change", "billing_question", "cancel"]
CHANNELS = ["chat", "voice"]
start = datetime(2026, 7, 1)
rows, cid = [], 0
for cust in range(1, 1201):
    intent = random.choice(INTENTS)
    t = start + timedelta(minutes=random.randint(0, 60 * 24 * 85))
    for attempt in range(3):
        cid += 1
        ai = random.random() < 0.8
        transferred = ai and random.random() < 0.18
        silence = ai and not transferred and random.random() < 0.14
        confirmed = ai and not transferred and not silence and random.random() < 0.85
        rows.append(dict(conversation_id=f"c{cid}", customer_id=f"u{cust}", intent=intent,
            channel=random.choice(CHANNELS), started_at=t.isoformat(timespec="minutes"),
            handled_by="ai" if ai else "human", transferred=str(transferred).lower(),
            outcome_confirmed=str(confirmed).lower(), ended_by_silence=str(silence).lower()))
        # unresolved or silent conversations often come back within days
        comes_back = (silence or not confirmed) and random.random() < 0.55 or random.random() < 0.06
        if not comes_back: break
        t += timedelta(hours=random.randint(2, 24 * 9))
with open("examples/sample_conversations.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(len(rows), "rows written")
