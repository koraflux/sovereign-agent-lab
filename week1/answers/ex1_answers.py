"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Model provided correct answers for all three formats. I've observed that the format affected model's choice between two pubs (both were correct). With plain format it chose Haymarket, with xml and sandwich - Albanach. The formatting doesnt break correctness on clean data with a strong model, but affects it's preferences.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
It's the Holyrood Arms as it fulfills 2 out of 3 requirements, failing only the status.  Even though, the model didn't fall for this anyway.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
The 'stress-test' didn't work. 8B also gave all three correct answers. Formatting didn't impact decision making event with smaller model. Also, 8B turned out to be even more consistent as it didn't change the choice between Haymarket (in plain) and Albanach (in xml and sandwich). I think it means that for us to see format impacting the choice we need either to have data with stronger distractors or weaker models.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
During this exercise we've explored how context formatting impacts (more likely how it doesn't in our cases) the decision making. Based on the observations, it should impact it when the data has distractors that are very close to the correct answer, the model is small and also probably when the question is not super clear. In my run all gave correct answer. Although, the format can impact which exact answer model chooses among multiple correct options (plain led to Haymarket, xml and sandwich to Albanach). I'll probably consider enhancing data with specific formatting for really complex cases in the future.
"""
