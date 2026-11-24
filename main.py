#!/usr/bin/env python3
"""Say What Actually Broke — one honest error line, no network, deterministic."""
import os

ENTRY = "Your retry loop retried so hard it DDoS'd our own database. Turn the retries off, let the database breathe, then try just once."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
