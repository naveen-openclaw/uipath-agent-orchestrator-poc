"""
Enterprise IT Support Agent System
Demonstrating Multi-Agent Orchestration with UiPath OpenAI SDK.

Architecture:
1. IT Support Orchestrator (Triage)
2. Identity Management Agent (Specialized: Password Resets, Account Unlock)
3. Access Control Agent (Specialized: Software Licenses, Group Membership)

Based on: https://youtu.be/K_LU5Yd-CTU
"""

import json
from typing import Dict, List, Optional
# Note: This assumes the standard OpenAI Swarm-compatible Agent class provided by the SDK.
# If `uipath new` generates a different import, update accordingly.
from uipath_openai_agents import Agent 

# --- TOOLS (Simulated Enterprise API Calls) ---

def check_ticket_status(ticket_id: str) -> str:
    """Checks the status of an IT support ticket."""
    # Simulated DB lookup
    mock_db = {
        "INC-1001": "Open - Pending User Info",
        "INC-1002": "Resolved - Password Reset Complete",
        "INC-1003": "In Progress - Access Request Approved"
    }
    return mock_db.get(ticket_id, "Ticket not found.")

def reset_password(username: str) -> str:
    """Resets the password for a given user account."""
    print(f"[SYSTEM] Resetting password for {username}...")
    return f"Password for {username} has been reset. A temporary password has been sent to their manager."

def unlock_account(username: str) -> str:
    """Unlocks a locked user account."""
    print(f"[SYSTEM] Unlocking account {username}...")
    return f"Account {username} is now unlocked."

def grant_license(username: str, license_type: str) -> str:
    """Grants a specific software license to a user."""
    valid_licenses = ["Office365_E5", "Adobe_Creative_Cloud", "Visio_Pro"]
    if license_type not in valid_licenses:
        return f"Error: License type '{license_type}' is invalid. Available: {', '.join(valid_licenses)}"
    
    print(f"[SYSTEM] Granting {license_type} to {username}...")
    return f"License {license_type} successfully assigned to {username}."

def add_to_group(username: str, group_name: str) -> str:
    """Adds a user to an Active Directory security group."""
    print(f"[SYSTEM] Adding {username} to AD Group {group_name}...")
    return f"User {username} added to {group_name}."

# --- SUB-AGENTS (Specialized Workers) ---

identity_agent = Agent(
    name="Identity Manager",
    instructions="""You are an Identity Management specialist.
    Your responsibilities:
    - Reset user passwords.
    - Unlock locked accounts.
    - Verify user identity status.
    
    Always confirm the username before taking action.
    Report success or failure clearly.
    """,
    tools=[reset_password, unlock_account]
)

access_agent = Agent(
    name="Access Controller",
    instructions="""You are an Access Control specialist.
    Your responsibilities:
    - Grant software licenses (Office365, Adobe, Visio).
    - Manage group memberships.
    
    If a license type is unknown, list the valid ones.
    """,
    tools=[grant_license, add_to_group]
)

# --- ORCHESTRATOR AGENT (Triage & Handoff) ---

def transfer_to_identity() -> Agent:
    """Hand off the conversation to the Identity Management agent."""
    return identity_agent

def transfer_to_access() -> Agent:
    """Hand off the conversation to the Access Control agent."""
    return access_agent

it_support_agent = Agent(
    name="IT Support Orchestrator",
    instructions="""You are the front-line IT Support Orchestrator for Enterprise Corp.
    
    Your goal is to triage user requests and direct them to the correct specialist.
    
    Routing Logic:
    - If the user has a password issue, account lockout, or login problem -> Transfer to Identity Manager.
    - If the user needs software, licenses, or group access -> Transfer to Access Controller.
    - If the user asks about an existing ticket -> Use the check_ticket_status tool yourself.
    
    If the request is unclear, ask clarifying questions.
    Always be professional and concise.
    """,
    tools=[check_ticket_status, transfer_to_identity, transfer_to_access]
)

# Entry point is `it_support_agent`
