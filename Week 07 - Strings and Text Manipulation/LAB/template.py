"""
RECORD CHECK  -  my version
===========================

Name  : Akshra 
Lane  :  AI     (delete two)
Date  : 12/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Clean a raw status line and return a dictionary."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}


def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK based on percentage used."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


total_records = 0
flagged_records = 0

with open("records.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        status = status_of(record["used"], record["total"])
        print(record, status)

        total_records = total_records + 1
        if status != "OK":
            flagged_records = flagged_records + 1

print(f"Total records: {total_records}, Flagged: {flagged_records}")