"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. Would you like me to:

1. Search for venues with a lower capacity (e.g., 250-299)?
2. Look for venues with vegan options that aren't strictly "available" (but might require booking)?
3. Suggest alternative dietary accommodation options?

Let me know how you'd like to proceed!
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
At first search_venues returned two pubs for 160 guests with vegan options: the Albanach and the Haymarket Vaults. After changing status of the Albanach to full in mcp_venue_server and re-running it, the first query return only the Haymarket Vaults and Albanach was filtered out by the status check. The only change was in the data, it shows that the tool layer is decoupled. Interesting also that the agent recovered from validation error on the first search_venues call by re-wrapping args in {"input": {}}
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 55   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
In the experiment I changed Albanach's status on the server and the client bahaviour changed without touching client code. We can call it something like a live contract, it's not just code separation. I expect that this will be very helpful when we'll have both langgraph and rasa agents as this way we will probably avoid duplicating code of our tools. Adding new tools this way doesn't increase complexity, compared to the original approach.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner - strong-reasoning model (i.e. Qwen3-Next-Thinking or DeepSeek R1). Taks the task and produces an ordered list of subtasks. Lives in the autonomous-loop half, upstream of the ReAct loop
- Executor - fast model for tool-calling (Qwen3-32B or Llama 70B) that runs a ReAct cycle for each subtask, using tools.
- Shared MCP tool gateway. Gets called by both autonomous-loop and the structured-agent. Lives in a shared part.
- Memory - filesystem memory and a vector db for RAG. It will give persistent context between sessions and a knowledge base. Lives in a shared part.
- Rasa CALM - this is the structured agent for confirming the booking. Structured and deterministic. Lives in structured-agent part.
- Guardrails and observability layer - tracing, limits, safety checks. Wraps both agents. Lives in a shared part.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
FILL ME IN
"""