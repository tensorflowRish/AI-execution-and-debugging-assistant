from core.prompt_manager import build_debug_prompt

class DebuggerAgent:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, error, memory_context, attempt_number, latest_status, escalation_level):
        prompt = build_debug_prompt(error, memory_context, attempt_number, latest_status, escalation_level)
        return self.llm.ask(prompt)