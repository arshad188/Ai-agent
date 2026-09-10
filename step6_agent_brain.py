# ============================================================
# AI AGENT - STEP 6
# LLM REASONING BRAIN
# ============================================================

from openai import OpenAI
import os


print("=" * 60)
print("              AI AGENT - STEP 6")
print("                LLM BRAIN")
print("=" * 60)


# ------------------------------------------------------------
# OPENAI CONNECTION
# ------------------------------------------------------------

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# ------------------------------------------------------------
# AVAILABLE TOOLS
# ------------------------------------------------------------

tools = [
    "calculate",
    "search",
    "analyze",
    "learn",
    "write",
    "finish"
]


# ------------------------------------------------------------
# GET USER GOAL
# ------------------------------------------------------------

goal = input("\nWhat is your goal?\n> ")


# ------------------------------------------------------------
# CREATE BRAIN INSTRUCTIONS
# ------------------------------------------------------------

instructions = """
You are the decision-making brain of a simple AI agent.

Your job is to examine the user's goal and choose the
MOST APPROPRIATE action.

Available actions:

calculate
search
analyze
learn
write
finish

Return ONLY one action from the list.

Do not explain your answer.
"""


# ------------------------------------------------------------
# ASK THE LLM
# ------------------------------------------------------------

print("\nAgent brain is thinking...")


response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=goal
)


# ------------------------------------------------------------
# READ DECISION
# ------------------------------------------------------------

decision = response.output_text.strip().lower()


# ------------------------------------------------------------
# CHECK DECISION
# ------------------------------------------------------------

if decision not in tools:

    print("\nWarning:")
    print("The brain returned an unknown action.")
    print("Raw response:", decision)

else:

    print("\nAGENT DECISION")
    print("-" * 60)
    print("Goal    :", goal)
    print("Action  :", decision)


print("\n" + "=" * 60)
print("STEP 6 TEST COMPLETE")
print("=" * 60)