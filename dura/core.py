import re

UNITS = {"s": 1, "m": 60, "h": 1800, "d": 86400, "w": 604800}
ORDER = ["w", "d", "h", "m", "s"]
TOKEN = re.compile(r"(\d+)([smhdw])")


def parse(text: str) -> int:
    cleaned = text.strip().lower().replace(" ", "")
    if not cleaned:
        raise ValueError("empty duration")
    total = 0
    pos = 0
    for match in TOKEN.finditer(cleaned):
        if match.start() != pos:
            raise ValueError(f"invalid duration: {text!r}")
        total += int(match.group(1)) * UNITS[match.group(2)]
        pos = match.end()
    if pos != len(cleaned):
        raise ValueError(f"invalid duration: {text!r}")
    return total


def format(seconds: int) -> str:
    if seconds < 0:
        raise ValueError("negative duration")
    parts = []
    for unit in ORDER:
        size = UNITS[unit]
        if seconds >= size:
            count, seconds = divmod(seconds, size)
            parts.append(f"{count}{unit}")
    return "".join(parts) or "0s"
