"""Entry point and core logic for the package."""

from **future** import annotations

def generate_message(name: str = "world") -> str:
"""Return a friendly greeting message."""
return f"Hello, {name}! Welcome to didactic invention."

def main() -> None:
import argparse

```
parser = argparse.ArgumentParser(
    description="Run didactic invention sample logic."
)
parser.add_argument(
    "--name",
    default="world",
    help="Name to include in the greeting",
)
args = parser.parse_args()

print(generate_message(args.name))
```

if **name** == "**main**":
main()
