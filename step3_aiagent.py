# ============================================================
# AI AGENT - STEP 3
# AGENT TOOLS
# ============================================================

print("=" * 60)
print("              AI AGENT - STEP 3")
print("                 AGENT TOOLS")
print("=" * 60)


# ------------------------------------------------------------
# TOOL 1: CALCULATOR
# ------------------------------------------------------------

def calculator():
    print("\n[CALCULATOR TOOL]")

    a = float(input("Enter first number: "))
    operator = input("Enter operator (+ - * /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero."
        result = a / b

    else:
        return "Unknown operator."

    return result


# ------------------------------------------------------------
# TOOL 2: TEXT ANALYZER
# ------------------------------------------------------------

def text_analyzer():
    print("\n[TEXT ANALYZER TOOL]")

    text = input("Enter some text: ")

    words = text.split()

    result = {
        "characters": len(text),
        "words": len(words)
    }

    return result


# ------------------------------------------------------------
# TOOL 3: KNOWLEDGE TOOL
# ------------------------------------------------------------

def knowledge_tool():
    print("\n[KNOWLEDGE TOOL]")

    knowledge = {
        "ai": "Artificial Intelligence is the field of creating systems that perform tasks requiring human-like intelligence.",

        "python": "Python is a programming language widely used in AI, data science and automation.",

        "agent": "An AI agent is a system that can perceive information, make decisions and take actions toward a goal."
    }

    question = input("What do you want to know? ").lower()

    for topic in knowledge:

        if topic in question:
            return knowledge[topic]

    return "I do not have information about that topic yet."


# ------------------------------------------------------------
# AGENT TOOL SELECTOR
# ------------------------------------------------------------

def run_tool(decision):

    if decision == "calculate":
        return calculator()

    elif decision == "analyze":
        return text_analyzer()

    elif decision == "search":
        return knowledge_tool()

    else:
        return "No tool available for this action."


# ------------------------------------------------------------
# MAIN AGENT
# ------------------------------------------------------------

goal = input("\nWhat is your goal? ")

text = goal.lower()

# Decide which tool is appropriate

if "calculate" in text or "math" in text:
    decision = "calculate"

elif "analyze" in text:
    decision = "analyze"

elif "search" in text or "find" in text or "know" in text:
    decision = "search"

else:
    decision = "none"


print("\nAgent thinking...")
print("Goal:", goal)
print("Decision:", decision)


# ------------------------------------------------------------
# USE TOOL
# ------------------------------------------------------------

if decision != "none":

    result = run_tool(decision)

    print("\n[AGENT RESULT]")
    print(result)

else:

    print("\nThe agent does not have a suitable tool yet.")


print("\n" + "=" * 60)
print("STEP 3 COMPLETE")
print("=" * 60)