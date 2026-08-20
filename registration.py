"""CLI entrypoint: renamed from `registraion.py` to `registration.py`."""

import sys
from pathlib import Path

# Ensure the script directory is on sys.path so local modules import reliably
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from registration_model import Registration
from store import RegistrationStore


def main():
	print("Event Registration v1 (module-split)")
	reg = Registration.from_input()
	store = RegistrationStore()
	store.save(reg)

	print("\nRegistration saved!\n")
	print("Confirmation:\n")
	info = reg.to_dict()
	print(f"  Name: {info['name']}")
	print(f"  Email: {info['email']}")
	print(f"  Training: {info['training']}")
	print(f"  Date: {info['date']}")
	print("\nYou can find all registrations in 'registrations.json'.")


if __name__ == "__main__":
	main()
