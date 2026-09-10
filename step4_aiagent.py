# ============================================================
# AI AGENT - STEP 4
# AGENT MEMORY
# ============================================================

import json
import os

print("=" * 60)
print("              AI AGENT - STEP 4")
print("                 AGENT MEMORY")
print("=" * 60)


MEMORY_FILE = "agent_memory.json"


# ------------------------------------------------------------
# LOAD LONG-TERM MEMORY
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
# SAVE LONG-TERM MEMORY
# ------------------------------------------------------------

def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


# ------------------------------------------------------------
# ADD MEMORY
# ------------------------------------------------------------

def remember(memory, user_text, agent_action, result):

    entry = {
        "user": user_text,
        "action": agent_action,
        "result": str(result)
    }

    memory.append(entry)

    save_memory(memory)


# ------------------------------------------------------------
# SHOW MEMORY
# ------------------------------------------------------------

def show_memory(memory):

    print("\n" + "-" * 60)
    print("AGENT MEMORY")
    print("-" * 60)

    if not memory:
        print("Memory is empty.")
        return

    for i, item in enumerate(memory, 1):

        print("\nMemory", i)
        print("User   :", item["user"])
        print("Action :", item["action"])
        print("Result :", item["result"])


# ------------------------------------------------------------
# START AGENT
# ------------------------------------------------------------

memory = load_memory()

print("\nMemory loaded:", len(memory), "records")


while True:

    print("\n")
    user_input = input("You: ")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if user_input.lower() == "exit":

        print("\nAgent shutting down...")
        break

    # --------------------------------------------------------
    # SHOW MEMORY
    # --------------------------------------------------------

    if user_input.lower() == "memory":

        show_memory(memory)
        continue

    # --------------------------------------------------------
    # SIMPLE DECISION
    # --------------------------------------------------------

    text = user_input.lower()

    if "calculate" in text:

        action = "calculate"
        result = "Calculator tool selected."

    elif "search" in text:

        action = "search"
        result = "Search tool selected."

    elif "analyze" in text:

        action = "analyze"
        result = "Analysis tool selected."

    else:

        action = "none"
        result = "I need a suitable tool for this task."

    # --------------------------------------------------------
    # DISPLAY DECISION
    # --------------------------------------------------------

    print("\nAgent decision:", action)
    print("Agent result  :", result)

    # --------------------------------------------------------
    # REMEMBER
    # --------------------------------------------------------

    remember(
        memory,
        user_input,
        action,
        result
    )

    print("Memory saved.")


print("\n" + "=" * 60)
print("STEP 4 COMPLETE")
print("=" * 60)