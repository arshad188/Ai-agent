# ============================================================
# AI AGENT - STEP 5
# MEMORY + DECISION BRAIN
# ============================================================

import json
import os

print("=" * 60)
print("              AI AGENT - STEP 5")
print("          MEMORY + DECISION BRAIN")
print("=" * 60)

MEMORY_FILE = "agent_memory.json"


# ------------------------------------------------------------
# LOAD MEMORY
# ------------------------------------------------------------

def load_memory():

    if os.path.exists(MEMORY_FILE):

        try:
            with open(MEMORY_FILE, "r") as file:
                return json.load(file)

        except:
            return []

    return []


# ------------------------------------------------------------
# SAVE MEMORY
# ------------------------------------------------------------

def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


# ------------------------------------------------------------
# REMEMBER
# ------------------------------------------------------------

def remember(memory, user_text, action, result):

    memory.append({
        "user": user_text,
        "action": action,
        "result": str(result)
    })

    save_memory(memory)


# ------------------------------------------------------------
# SEARCH MEMORY
# ------------------------------------------------------------

def search_memory(memory, question):

    question_words = question.lower().split()

    matches = []

    for item in memory:

        old_text = item["user"].lower()

        score = 0

        for word in question_words:

            if len(word) > 2 and word in old_text:
                score += 1

        if score > 0:
            matches.append((score, item))

    # Highest score first
    matches.sort(reverse=True, key=lambda x: x[0])

    return matches


# ------------------------------------------------------------
# DISPLAY MEMORY RESULT
# ------------------------------------------------------------

def show_memory_result(matches):

    print("\n[MEMORY SEARCH]")

    if not matches:
        print("No relevant memory found.")
        return

    for score, item in matches[:3]:

        print("\nRelevant memory:")
        print("User   :", item["user"])
        print("Action :", item["action"])
        print("Result :", item["result"])


# ------------------------------------------------------------
# DECISION BRAIN
# ------------------------------------------------------------

def decide(user_input, memory):

    text = user_input.lower()

    # First check memory
    matches = search_memory(memory, user_input)

    if matches:

        print("\nThe agent found something relevant in memory.")

        show_memory_result(matches)

    else:

        print("\nThe agent found no relevant memory.")


    # Then make a decision

    if "calculate" in text or "math" in text:

        return "calculate"

    elif "search" in text or "find" in text:

        return "search"

    elif "analyze" in text:

        return "analyze"

    elif "learn" in text or "study" in text:

        return "learn"

    else:

        return "none"


# ------------------------------------------------------------
# START AGENT
# ------------------------------------------------------------

memory = load_memory()

print("\nMemory records:", len(memory))

print("\nCommands:")
print("  memory  = show all memory")
print("  exit    = quit")


while True:

    user_input = input("\nYou: ")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if user_input.lower() == "exit":

        break


    # --------------------------------------------------------
    # SHOW ALL MEMORY
    # --------------------------------------------------------

    if user_input.lower() == "memory":

        show_memory_result(
            [(1, item) for item in memory]
        )

        continue


    # --------------------------------------------------------
    # THINK + DECIDE
    # --------------------------------------------------------

    print("\nAgent thinking...")

    action = decide(
        user_input,
        memory
    )

    print("\nDecision:", action)


    # --------------------------------------------------------
    # TEMPORARY RESULT
    # --------------------------------------------------------

    if action == "calculate":

        result = "Calculator should be used."

    elif action == "search":

        result = "Search tool should be used."

    elif action == "analyze":

        result = "Analysis tool should be used."

    elif action == "learn":

        result = "Learning process should begin."

    else:

        result = "No suitable action found."


    print("Result:", result)


    # --------------------------------------------------------
    # SAVE EXPERIENCE
    # --------------------------------------------------------

    remember(
        memory,
        user_input,
        action,
        result
    )

    print("Experience saved to memory.")


print("\n" + "=" * 60)
print("STEP 5 COMPLETE")
print("=" * 60)