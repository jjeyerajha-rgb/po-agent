# PO Agent — AI Product Owner Assistant

A Streamlit-powered AI agent that helps human Product Owners automate routine tasks so they can focus on strategy, decision-making, and business value.

## Capabilities

| Capability | What it does |
|---|---|
| **User Story Writer** | Generates INVEST-compliant user stories with acceptance criteria, story points, and dependencies |
| **Backlog Prioritizer** | Prioritizes items using MoSCoW, WSJF, RICE, or Value-vs-Effort frameworks |
| **Acceptance Criteria Generator** | Creates Given/When/Then scenarios covering happy paths, edge cases, and errors |
| **Sprint Planner** | Plans sprints with goal setting, capacity planning, and risk identification |
| **Release Notes Generator** | Produces audience-tailored release notes and changelogs |
| **Stakeholder Communications** | Drafts status updates, executive summaries, and tailored messages |
| **Meeting Prep Assistant** | Prepares agendas, talking points, and materials for any ceremony or meeting |

## Quick Start

### 1. Prerequisites

- Python 3.11+
- An OpenAI API key (get one at https://platform.openai.com)

### 2. Install

```bash
cd po-agent
pip install -r requirements.txt
```

### 3. Configure

Copy `.env.example` to `.env` and add your API key:

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY
```

Or simply enter your API key in the sidebar when the app starts.

### 4. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Project Structure

```
po-agent/
├── app.py                      # Streamlit UI
├── config.py                   # Environment configuration
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── agents/
│   ├── base_agent.py           # Base agent class
│   ├── story_writer.py         # User story generation
│   ├── backlog_manager.py      # Backlog prioritization
│   ├── acceptance_criteria.py  # AC generation
│   ├── sprint_planner.py       # Sprint planning
│   ├── release_notes.py        # Release notes
│   ├── stakeholder_comms.py    # Stakeholder communication
│   └── meeting_prep.py         # Meeting preparation
├── models/
│   ├── story.py                # User story model
│   ├── backlog_item.py         # Backlog item model
│   └── sprint.py               # Sprint model
└── utils/
    ├── llm_client.py           # OpenAI API client
    ├── prompts.py              # Prompt templates
    └── export.py               # Export utilities
```

## Customization

- **Model**: Switch between GPT-4o, GPT-4o-mini, GPT-4-turbo, or GPT-3.5-turbo via the sidebar
- **Prompts**: Edit `utils/prompts.py` to tune agent behavior for your domain
- **API**: Supports Azure OpenAI or any compatible API — set `OPENAI_BASE_URL` in `.env`

## License

MIT
