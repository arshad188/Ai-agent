# ============================================================
# SIMPLE AI AGENT - STEP 1
# ============================================================

print("=" * 60)
print("          MY FIRST AI AGENT")
print("=" * 60)

# ------------------------------------------------------------
# 1. AGENT GOAL
# ------------------------------------------------------------

goal = input("\nWhat is the agent's goal? ")

print("\nAGENT BRAIN")
print("-" * 60)

print("Goal received:")
print(goal)

# ------------------------------------------------------------
# 2. THINKING
# ------------------------------------------------------------

print("\nThinking...")

if "learn" in goal.lower():
    decision = "I should find information and study it."

elif "calculate" in goal.lower():
    decision = "I should perform a calculation."

elif "search" in goal.lower():
    decision = "I should search for information."

elif "analyze" in goal.lower():
    decision = "I should collect data and analyze it."

else:
    decision = "I need more information before deciding."

# ------------------------------------------------------------
# 3. DECISION
# ------------------------------------------------------------

print("\nDecision:")
print(decision)

# ------------------------------------------------------------
# 4. ACTION
# ------------------------------------------------------------

print("\nAction:")
print("I will now try to accomplish the goal.")

print("\n" + "=" * 60)
print("AGENT FINISHED")
print("=" * 60)