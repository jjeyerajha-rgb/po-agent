# PO Agent JJ — Reference

## User Story Format

```
As a [persona],
I want [goal],
So that [benefit].

**Story points**: [1|2|3|5|8|13|21]
**Labels**: [feature|bug|tech-debt|spike]
**Dependencies**: [if any]

### Acceptance Criteria
- Given [context], When [action], Then [outcome]
```

Apply **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable. Split stories >8 points.

## Prioritization Frameworks

| Framework | Use when |
|-----------|----------|
| **MoSCoW** | Stakeholder alignment on must-haves vs nice-to-haves |
| **RICE** | Data-driven ranking (Reach × Impact × Confidence / Effort) |
| **WSJF** | Cost of delay matters (SAFe environments) |
| **Value vs Effort** | Quick visual prioritization |

Always include **rationale** for each ranking decision.

## Acceptance Criteria Standards

- Given/When/Then (Gherkin) format
- Cover: happy path, edge cases, error handling
- Include NFRs when relevant: performance, accessibility, security
- Implementation-agnostic — describe behavior, not UI internals

## Sprint Plan Structure

1. **Sprint goal** — one clear outcome
2. **Capacity** — points available vs team velocity
3. **Selected stories** — ordered with dependencies noted
4. **Risks & dependencies** — blockers, external teams
5. **Success metrics** — how to know the sprint succeeded

## Release Notes Audiences

| Audience | Tone | Include |
|----------|------|---------|
| End users | Plain language, benefits-focused | Features, fixes, known issues |
| Executives | Business impact | Outcomes, metrics, strategic alignment |
| Developers | Technical detail | API changes, migrations, breaking changes |

## Meeting Prep Templates

- **Sprint Planning**: goal candidates, backlog top items, capacity, risks
- **Sprint Review**: demo order, metrics, stakeholder questions
- **Retrospective**: data points, themes, action item prompts
- **Backlog Refinement**: stories to refine, open questions, estimation prep

## Human PO Decisions (do not automate)

- Final priority calls conflicting with strategy
- Scope cuts or trade-off decisions
- Stakeholder negotiations and commitments
- Go/no-go on releases

Flag these explicitly when the agent output touches them.
