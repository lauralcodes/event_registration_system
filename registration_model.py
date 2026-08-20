"""Registration model: handles input and validation for a participant."""

from datetime import datetime


class Registration:
    trainings = ["Python Basics", "Data Science", "Web Development"]

    def __init__(self, name: str, email: str, training: str, date: str):
        self.name = name
        self.email = email
        self.training = training
        self.date = date

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "training": self.training,
            "date": self.date,
            "registered_at": datetime.now().isoformat(),
        }

    @classmethod
    def from_input(cls) -> "Registration":
        name = cls._get_nonempty_input("Participant name: ")
        email = cls._get_valid_email("Email: ")
        training = cls._choose_training()
        date = cls._get_valid_date("Event date (YYYY-MM-DD): ")
        return cls(name, email, training, date)

    @staticmethod
    def _get_nonempty_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Please enter a value.")

    @staticmethod
    def _get_valid_email(prompt: str) -> str:
        while True:
            email = input(prompt).strip()
            if "@" in email and "." in email:
                return email
            print("Please enter a valid email (must contain '@' and '.')")

    @classmethod
    def _choose_training(cls) -> str:
        print("Available trainings:")
        for i, opt in enumerate(cls.trainings, start=1):
            print(f"  {i}. {opt}")
        while True:
            choice = input(f"Choose training (1-{len(cls.trainings)}): ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(cls.trainings):
                    return cls.trainings[idx]
            print("Please choose a number from the list.")

    @staticmethod
    def _get_valid_date(prompt: str) -> str:
        while True:
            s = input(prompt).strip()
            try:
                d = datetime.strptime(s, "%Y-%m-%d").date()
                return d.isoformat()
            except ValueError:
                print("Please enter a date in YYYY-MM-DD format, e.g. 2026-08-20")
