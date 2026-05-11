class EscalationEngine:

    def get_level(self, attempt_number, similar_errors, latest_status):

        if attempt_number == 1:
            return 1

        failed_count = len([
            m for m in similar_errors
            if m.get("status") == "failed"
        ])

        worked_count = len([
            m for m in similar_errors
            if m.get("status") == "worked"
        ])

        if failed_count >= 2 and worked_count >= 1:
            return 4

        if failed_count >= 2:
            return 3

        if attempt_number == 2:
            return 2

        return 1