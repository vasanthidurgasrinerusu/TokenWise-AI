class ApprovalManager:

    def request_approval(self, action: str, filename: str):

        print("\n===== FILE CHANGE APPROVAL =====")

        print("Action:", action)
        print("Target File:", filename)

        while True:

            choice = input(
                "\nDo you approve this change? (yes/no): "
            ).strip().lower()

            if choice in ("yes", "y"):
                print("Approval granted.")
                return True

            elif choice in ("no", "n"):
                print("Change rejected.")
                return False

            else:
                print("Please enter yes or no.")