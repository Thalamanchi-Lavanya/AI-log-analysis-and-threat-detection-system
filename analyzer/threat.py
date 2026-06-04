class Threat:

    def __init__(
        self,
        username,
        attack_type,
        risk_level
    ):

        self.username = username
        self.attack_type = attack_type
        self.risk_level = risk_level

    def display(self):

        print(
            f"User: {self.username}"
        )

        print(
            f"Attack Type: {self.attack_type}"
        )

        print(
            f"Risk Level: {self.risk_level}"
        )

        print("------------------")