# PO Agent JJ

Your personal workspace for **AI-assisted Product Owner tasks** — user stories, backlog prioritization, sprint planning, release notes, and more.

**Location**: `C:\Users\jeyer\PO Agent JJ`

## Two Ways to Use

### 1. Cursor Chat (this folder)

1. **Open this folder in Cursor** — File → Open Folder → `PO Agent JJ`
2. **Fill in your profile** — edit [profile/product-owner-profile.md](profile/product-owner-profile.md)
3. **Ask in chat**:

   ```
   Write user stories for [feature]
   Prioritize my backlog using RICE
   Plan sprint 12 with 40 points capacity
   ```

Generated artifacts are saved to `outputs/` when substantial.

### 2. Streamlit Web App

```bash
cd "C:\Users\jeyer\PO Agent JJ"
pip install -r requirements.txt
streamlit run app.py
```

Open **http://localhost:8501**. Enter your OpenAI API key in the sidebar (or set `OPENAI_API_KEY` in `.env`).

## Capabilities

| Capability | What it does |
|---|---|
| **User Story Writer** | INVEST-compliant stories with acceptance criteria and story points |
| **Backlog Prioritizer** | MoSCoW, WSJF, RICE, or Value-vs-Effort ranking |
| **Acceptance Criteria Generator** | Given/When/Then scenarios |
| **Sprint Planner** | Sprint goals, capacity planning, risk identification |
| **Release Notes Generator** | Audience-tailored changelogs |
| **Stakeholder Communications** | Status updates and executive summaries |
| **Meeting Prep Assistant** | Agendas and talking points |

## Project Structure

```
PO Agent JJ/
├── .cursor/skills/po-agent/       # Cursor agent skill
│   ├── SKILL.md
│   └── reference.md
├── profile/
│   └── product-owner-profile.md   # Your product & team context
├── outputs/                       # Generated stories, plans, notes
├── agents/                        # Streamlit app agent modules
├── models/                        # Data models
├── utils/                         # LLM client, prompts, export
├── app.py                         # Streamlit UI
├── config.py
├── requirements.txt
└── README.md
```

## Example Prompts (Cursor)

| Prompt | What happens |
|--------|--------------|
| "Write user stories for login with SSO" | INVEST stories + AC |
| "Prioritize these 5 backlog items using MoSCoW" | Ranked list with rationale |
| "Generate acceptance criteria for [story]" | Given/When/Then scenarios |
| "Draft release notes for v2.3" | Saved to outputs/ |
| "Prepare sprint review agenda" | Meeting prep doc |

## Configuration

Copy `.env.example` to `.env` and set your OpenAI API key:

```
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4o
```

## GitHub & Streamlit Cloud Deployment

### Push to GitHub

```bash
cd "C:\Users\jeyer\PO Agent JJ"
git init
git add .
git commit -m "PO Agent JJ — Streamlit app with Cursor workspace"
git branch -M master
git remote add origin https://github.com/jjeyerajha-rgb/po-agent.git
git push -u origin master
```

**Repository**: [github.com/jjeyerajha-rgb/po-agent](https://github.com/jjeyerajha-rgb/po-agent)

### Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Click **New app** (or open existing `po-agent` app → **Settings** → **Reconnect**)
3. Set:
   - **Repository**: `jjeyerajha-rgb/po-agent`
   - **Branch**: `master`
   - **Main file path**: `app.py`
4. Under **Advanced settings → Secrets**, paste:

   ```toml
   OPENAI_API_KEY = "sk-your-actual-key-here"
   OPENAI_MODEL = "gpt-4o"
   ```

5. Click **Deploy**

App URL (after deploy): **https://jjeyerajha-rgb-po-agent.streamlit.app**

### Local secrets (optional)

For local dev without entering the key each time:

```bash
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
# Edit .streamlit\secrets.toml with your key
streamlit run app.py
```

## License

MIT
