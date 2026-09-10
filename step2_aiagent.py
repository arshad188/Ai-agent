# ============================================================
# AI AGENT - STEP 2
# DECISION MAKING BRAIN
# ============================================================

print("=" * 60)
print("              AI AGENT - STEP 2")
print("              DECISION BRAIN")
print("=" * 60)

# ------------------------------------------------------------
# AVAILABLE ACTIONS
# ------------------------------------------------------------

actions = [
    "search",
    "calculate",
    "analyze",
    "learn",
    "write",
    "finish"
]

print("\nAvailable actions:")

for i, action in enumerate(actions, 1):
    print(i, ".", action)

# ------------------------------------------------------------
# RECEIVE GOAL
# ------------------------------------------------------------

goal = input("\nWhat is your goal? ")

print("\nGoal:")
print(goal)

# ------------------------------------------------------------
# THINKING
# ------------------------------------------------------------

print("\nAgent is thinking...")

text = goal.lower()

# ------------------------------------------------------------
# DECISION SYSTEM
# ------------------------------------------------------------

if "search" in text or "find" in text:
    decision = "search"

elif "calculate" in text or "math" in text:
    decision = "calculate"

elif "analyze" in text or "analysis" in text:
    decision = "analyze"

elif "learn" in text or "study" in text:
    decision = "learn"

elif "write" in text or "create" in text:
    decision = "write"

else:
    decision = "finish"

# ------------------------------------------------------------
# DECISION
# ------------------------------------------------------------

print("\nAgent decision:")
print("ACTION =", decision)

# ------------------------------------------------------------
# ACTION
# ------------------------------------------------------------

print("\nAgent will now perform:")
print(decision)

print("\n" + "=" * 60)
print("STEP 2 COMPLETE")
print("=" * 60)