#!/usr/bin/env python3
"""binary-converter — Binary Converter"""
import sys, json, argparse
from datetime import datetime, timezone

def main():
    parser = argparse.ArgumentParser(description="Binary Converter")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()
    result = {"tool": "binary-converter", "version": "1.0.0", "author": "Jose Zuma"}
    if args.json: print(json.dumps(result, indent=2))
    else: print(f"{result['tool']} v{result['version']} — {desc}")

if __name__ == "__main__":
    main()
