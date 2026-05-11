from core.llm_client import LLMClient
from agents.debugger_agent import DebuggerAgent
from agents.memory_agent import MemoryAgent
from core.escalation_engine import EscalationEngine
from core.formatter import format_response
from core.error_classifier import classify_error

def main():

    llm = LLMClient()

    debugger = DebuggerAgent(llm)

    memory = MemoryAgent()

    escalator = EscalationEngine()

    print("-- AI Debugging Assistant --")

    error = input("\nPaste your error:\n")

    similar_errors = memory.get_similar_errors(error)

    #print("DEBUG:", similar_errors)

    if len(similar_errors) == 0:
        attempt_number = 1
    else:
        attempt_number = max(
            [m.get("attempt_number", 1) for m in similar_errors]
        ) + 1

    latest_status = memory.get_latest_status(error)

    escalation_level = escalator.get_level(
    attempt_number,
    similar_errors,
    latest_status
    )

    result = debugger.analyze(
        error,
        similar_errors,
        attempt_number,
        latest_status,
        escalation_level
    )

    print("\n-- Analysis --\n")

    format_response(result)

    attempted_fix = input(
        "\nWhat fix did you try?\n"
    )

    outcome = input(
        "\nDid it work or fail?\n"
    )

    memory.save_entry({
        "error": error,
        "attempted_fix": attempted_fix,
        "status": outcome.lower(),
        "attempt_number": attempt_number
    })
    

if __name__ == "__main__":
    main()