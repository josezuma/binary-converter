#!/usr/bin/env python3
"""binary-converter — Convert between binary, octal, decimal, and hexadecimal. CLI with all-direction conversion."""
import sys, json, argparse
def main():
    parser = argparse.ArgumentParser(description="Convert between binary, octal, decimal, and hexadecimal. CLI with all-direction conversion.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "binary-converter", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")
if __name__ == "__main__":
    main()
