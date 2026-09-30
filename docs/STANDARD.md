# The Honest Resolution Standard

September 30, 2026 · Samadrita Roy Chowdhury

AI support vendors publish resolution rates that cannot be compared, because each one counts something different. This standard fixes that with one formula, six disclosures and a one line label any vendor can publish next to its number.

## The problem, in numbers

An audit of ten AI support vendors' public claims (Parloa, Crescendo, Maven AGI, Replicant, Observe.AI, Assembled, Regal, Bland, Gorgias, Avoca) found:

- **1 of 10** discloses its denominator ([Gorgias](https://docs.gorgias.com/en-US/5666070-510391b5092b4ac3afaf46a531bb86dc)).
- **0 of 10** tie the headline number to a check on whether the customer came back.
- **0 of 10** say who decides a conversation counts as resolved.
- **1.05 out of 5** is the average disclosure score across all ten.

The same vendor can publish two numbers for one customer. Maven AGI reports Mastermind at 93% of live chat questions answered and 68% of support page inquiries resolved ([Maven](https://www.mavenagi.com/blog/customer-support-ticket-resolution-statistics)). The headline uses the first.

Who judges matters too. SQM Group finds that FCR measured internally runs 10 to 20% higher than FCR measured by asking customers ([SQM](https://sqmgroup.com/resources/library/blog/calculate-first-call-resolution-rate)).

## The formula: Honest Resolution Rate

A conversation counts as resolved only if the outcome is confirmed and the customer does not come back about the same thing within 7 days.

```math
\text{HRR} = \frac{\text{AI conversations with a confirmed outcome and no same intent repeat contact within 7 days}}{\text{all conversations the AI started, including abandoned ones}}
```

Three rules keep the number honest:

1. **Silence is not resolution.** A customer who stops replying or hangs up counts as not resolved. One week of data can read as 45% or 93% depending on this rule alone ([Customer Service Manager](https://customerservicemanager.com/how-to-read-an-ai-resolution-rate-before-you-believe-it/)).
2. **No human is not the same as resolved.** Handled without a transfer is containment, and it is reported separately.
3. **The window runs across channels.** A chat today and a phone call about the same order on day 4 voids the chat's resolution. SQM counts repeat contact through any channel ([SQM](https://sqmgroup.com/resources/library/blog/calculate-first-call-resolution-rate)).

## Six required disclosures

Every published rate carries all six. Each one closes a gap the audit found, and each already exists somewhere in the market.

| # | Disclosure | What to publish | Gap it closes | Precedent |
| --- | --- | --- | --- | --- |
| 1 | Denominator | Raw count of conversations the AI started, including abandoned and out of scope ones | 9 of 10 vendors publish no denominator | [Gorgias](https://docs.gorgias.com/en-US/5666070-510391b5092b4ac3afaf46a531bb86dc) publishes its formula and changed its denominator in the open |
| 2 | Definition of resolved | Outcome confirmed in a system of record or by the customer; silence excluded | [Replicant](https://www.replicant.com/blog/how-to-measure-voice-ai-success-metrics-that-actually-matter) and Assembled define resolution as no human involved | [Zendesk](https://www.zendesk.com/blog/ai/workflow-automation/automated-resolution-rate/) requires no follow up for the same issue |
| 3 | Repeat contact window | Same customer, same intent, any channel; 7 days by default, longer for claims or disputes | 0 of 10 tie their headline to a repeat check | [SQM](https://sqmgroup.com/resources/library/blog/calculate-first-call-resolution-rate) sets the window by call type, from days to 30 |
| 4 | Who judges | Labeler (rules, LLM, human QA, or customer) plus a human audited sample and its agreement rate | 0 of 10 name the judge | [Avoca](https://www.avoca.ai/coach) reclassifies mislabeled call outcomes; one case averaged 12% wrong |
| 5 | Scope and period | Dates, channels, intents in scope, and that scope's share of total volume | Maven's 93% headline is an answer rate from one channel | [Gorgias](https://docs.gorgias.com/en-US/automate-statistics-81942) moved to total volume so small pilots stop looking large |
| 6 | AI only or blended | The AI only rate, reported apart from any AI plus human rate | Crescendo's 99.8% covers AI and humans together, per a competitor | [Fin](https://fin.ai/learn/fin-vs-crescendo) on blended accuracy |

## The label

All six disclosures fit on one line, so they can sit under any headline number, like a nutrition label.

```
HRR 64% | n = 41,200 AI conversations | Jul 1 to Sep 30, 2026 | chat and voice, 38% of total volume | 7 day same intent window | judged by LLM, 5% human audit, 94% agreement | AI only
```

The figures above are illustrative. A buyer reading two vendors' labels side by side can now see whether the numbers are comparable before comparing them.

## RFP clause, ready to paste

A buyer can adopt the standard today without any vendor agreeing to it first.

> Any resolution, containment, automation or deflection rate the vendor cites in this proposal, in reporting, or on invoices must be stated as an Honest Resolution Rate with all six disclosures: denominator, definition of resolved, repeat contact window, judge and audit agreement rate, scope and period, and AI only versus blended. Where the vendor bills per resolution, the billing definition must match the reported definition. The buyer may audit a random sample of 200 conversations per quarter. If the buyer's labels disagree with the vendor's on more than 5% of the sample, billed resolutions for that quarter are adjusted by the disagreement rate.

The 200 conversation sample and the 5% threshold are starting points for negotiation, not tested values.

## Why a vendor would adopt it first

The first vendor to publish an HRR gets to ask every competitor in a bake off for the same number. Four reasons it pays, and one honest cost:

- **It protects per resolution billing.** Crescendo bills from about $1.25 per resolution and skips unresolved or low CSAT conversations ([Crescendo](https://www.crescendo.ai/blog/ai-agent-for-customer-support-practical-guide-cx-leaders)). A published definition turns a disputed invoice line into an agreed one.
- **The data already exists.** Gorgias already publishes its formula. Avoca already audits outcome labels. Parloa's agents already keep contextual memory across channels, which is exactly what a repeat contact check needs.
- **Vendors already agree in principle.** Maven's own blog says autonomous resolution and FCR should be measured separately ([Maven](https://www.mavenagi.com/blog/first-contact-resolution-statistics)). The standard just makes it the published number.
- **Buyers are already asking.** A trade magazine published a five point checklist for vendor resolution rates in September 2026 ([Customer Service Manager](https://customerservicemanager.com/how-to-read-an-ai-resolution-rate-before-you-believe-it/)).
- **The cost: the number drops.** Maven's Mastermind figure would fall from 93 toward 68. The first mover takes that hit once, and every competitor takes it later, on the buyer's terms.

## Sources

Vendor pages accessed September 30, 2026. The full ten vendor audit is in [`audit/Resolution_Claims_Audit_Day1.xlsx`](../audit/Resolution_Claims_Audit_Day1.xlsx) and [`data/claims_audit.csv`](../data/claims_audit.csv).

- [Gorgias: How metrics are calculated, AI and automation](https://docs.gorgias.com/en-US/5666070-510391b5092b4ac3afaf46a531bb86dc)
- [Gorgias: Automate statistics, denominator change](https://docs.gorgias.com/en-US/automate-statistics-81942)
- [Maven AGI: Customer support ticket resolution statistics](https://www.mavenagi.com/blog/customer-support-ticket-resolution-statistics)
- [Maven AGI: First contact resolution statistics](https://www.mavenagi.com/blog/first-contact-resolution-statistics)
- [Replicant: How to measure voice AI success](https://www.replicant.com/blog/how-to-measure-voice-ai-success-metrics-that-actually-matter)
- [Crescendo: AI agent for customer support, a practical guide](https://www.crescendo.ai/blog/ai-agent-for-customer-support-practical-guide-cx-leaders)
- [Fin: Fin vs Crescendo](https://fin.ai/learn/fin-vs-crescendo)
- [Avoca: Coach and call reclassification](https://www.avoca.ai/coach)
- [Zendesk: Automated resolution rate](https://www.zendesk.com/blog/ai/workflow-automation/automated-resolution-rate/)
- [SQM Group: How to calculate first call resolution](https://sqmgroup.com/resources/library/blog/calculate-first-call-resolution-rate)
- [Customer Service Manager: How to read an AI resolution rate](https://customerservicemanager.com/how-to-read-an-ai-resolution-rate-before-you-believe-it/)
