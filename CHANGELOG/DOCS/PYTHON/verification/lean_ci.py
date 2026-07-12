import json
import sys
import re
import hashlib
from datetime import datetime
from pathlib import Path

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', required=True)
    parser.add_argument('--output', default='reports/lean_certificate.json')
    args = parser.parse_args()

    log_content = Path(args.log).read_text()

    theorems = re.findall(r'theorem\s+([A-Za-z0-9_]+)', log_content)
    sorries = len(re.findall(r'\bsorry\b', log_content, re.IGNORECASE))
    errors = len(re.findall(r'error:', log_content, re.IGNORECASE))
    warnings = len(re.findall(r'warning:', log_content, re.IGNORECASE))

    cert = {
        "version": "FC-003.1",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "lean_version": "v4.17.0",
        "theorems_checked": len(set(theorems)),
        "sorries": sorries,
        "errors": errors,
        "warnings": warnings,
        "status": "PASS" if sorries == 0 and errors == 0 else "FAIL",
        "sha256": hashlib.sha256(log_content.encode()).hexdigest(),
        "summary": f"{len(set(theorems))} theorems • {sorries} sorry • {errors} errors"
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(cert, indent=2))

    print(json.dumps(cert, indent=2))
    return 0 if cert["status"] == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
