from storage.vector_memory import VectorMemory
from core.error_classifier import classify_error

class MemoryAgent:

    def __init__(self):

        self.vector_db = VectorMemory()

    def save_entry(self, entry):

        category = classify_error(
            entry["error"]
        )

        entry["category"] = category

        self.vector_db.add_memory(
            entry["error"],
            entry
        )

    def get_similar_errors(self, error):

        category = classify_error(error)

        return self.vector_db.search_memory(
            error,
            category
        )
    
    def get_latest_status(self, error):

        similar = self.get_similar_errors(error)

        if len(similar) == 0:
            return None

        return similar[-1]["status"]