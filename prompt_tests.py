import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "prompt_tests.json"

def load_tests():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def display_tests(tests):
    print("=" * 60)
    print("PROMPT TESTING REPORT")
    print("=" * 60)

    for index, test in enumerate(tests, start=1):
        print(f"\nTest #{index}")
        print(f"Task: {test['task']}")
        print(f"Prompt type: {test['prompt_type']}")
        print(f"Prompt: {test['prompt']}")
        print(f"Observation: {test['result']}")

if __name__ == "__main__":
    tests = load_tests()
    display_tests(tests)
