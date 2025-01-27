#!/usr/bin/env python3
import sys
import re

def main() -> int:
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, 'r') as file:
        commit_msg = file.read().strip()

    pattern = r'^JIRA-\d+ - .+$'
    if not re.match(pattern, commit_msg):
        print("ERROR: Commit message does not follow required format: 'JIRA-XXX - Description'")
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())