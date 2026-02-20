# Enterprise IT Support Agent (UiPath OpenAI SDK POC)

A Proof of Concept (POC) demonstrating **Agentic Orchestration** using the UiPath OpenAI Agents SDK.
This project implements the "Orchestrator Pattern" shown in the [UiPath OpenAI Agents Quick Start video](https://youtu.be/K_LU5Yd-CTU).

## Architecture

**1. Orchestrator Agent (IT Support)**
   - Triages incoming requests.
   - Handles basic queries (e.g., ticket status).
   - Routes complex tasks to specialized sub-agents.

**2. Specialized Sub-Agents**
   - **Identity Agent:** Manages passwords and account unlocks.
   - **Access Agent:** Grants software licenses and group memberships.

**3. Simulated Tools**
   - Python functions acting as enterprise API mocks (e.g., `reset_password`, `grant_license`).

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (Recommended package manager)
- OpenAI API Key
- UiPath Automation Cloud Account

## Setup Instructions

1.  **Initialize Environment**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install uipath-openai-agents openai
    ```

2.  **Configure Environment Variables**
    Create a `.env` file in the root directory:
    ```bash
    OPENAI_API_KEY=sk-proj-...
    ```

3.  **Authenticate with UiPath**
    ```bash
    uipath auth
    ```

4.  **Initialize Project**
    This generates necessary metadata files (`entry-points.json`, etc.):
    ```bash
    uipath init
    ```

5.  **Run Locally**
    Test the agent with a sample query:
    ```bash
    uipath run agent '{"messages": "I need a Visio license."}'
    ```
    *Expected Behavior:* The Orchestrator should hand off the request to the **Access Agent**, which will then ask for clarification or execute the tool.

6.  **Deploy to Orchestrator**
    Package and publish to your personal workspace:
    ```bash
    uipath pack
    uipath publish --my-workspace
    ```

## Extending the Project

- **Real Integration:** Replace the simulated tools in `main.py` with actual API calls (ServiceNow, Active Directory, Azure AD).
- **More Agents:** Add an `HR Agent` for PTO requests (as seen in the video).
- **UiPath Studio:** Use `uipath push` to edit the agent flow visually in Studio.

## EB-1A Significance

This project demonstrates **Architectural Leadership** in Agentic Systems:
- **Scalability:** The orchestrator pattern allows adding new capabilities without modifying the core logic.
- **Enterprise-Readiness:** Separation of concerns (Identity vs. Access) mimics real-world IT governance.
- **Standardization:** Uses the official SDK patterns, suitable for enterprise adoption.
