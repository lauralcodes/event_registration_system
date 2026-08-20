"""Persistence layer for registrations (JSON file)."""

import json
from pathlib import Path
from typing import List

from registration_model import Registration


class RegistrationStore:
    def __init__(self, path: str = "registrations.json"):
        self.path = Path(path)

    def load_all(self) -> List[dict]:
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text())
            return data if isinstance(data, list) else []
        except Exception:
            return []

    def save(self, registration: Registration) -> None:
        data = self.load_all()
        data.append(registration.to_dict())
        self.path.write_text(json.dumps(data, indent=2))
