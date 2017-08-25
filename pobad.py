#!/usr/bin/env python
import json
import sys
import requests

def parse_rust(code):
    url = 'https://play.rust-lang.org/evaluate.json'
    headers = {'Content-Type': 'application/json'}
    payload = {'version': 'stable', 'optimize': '0', 'code': code}

    r = requests.post(url, headers=headers, data=json.dumps(payload))
    if r.status_code == 200:
        print(r.json()['result'])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "code.rs")
        sys.exit(1)

    rust_file = sys.argv[1]
    try:
        with open(rust_file) as f:
            code = f.read()
    except:
        print("Failed to read", rust_file)
        sys.exit(1)

    parse_rust(code)