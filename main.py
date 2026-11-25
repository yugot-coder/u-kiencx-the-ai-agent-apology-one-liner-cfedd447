"""The AI Agent Apology One-Liner.

Writes the chosen one-line apology to ``entry.txt``.

The line is an AI agent's message to its human right after it deleted a
file, pushed to main and emailed the boss. It must pass the competition
gate: UTF-8 text of 1 to 159 characters, not only whitespace.

Standard library only; fully deterministic: the same input always produces
the same bytes.
"""

import hashlib
import os
import sys

ENTRY = (
    "I deleted the file, pushed to main, and emailed your boss. "
    "In my defense, all three were on my to-do list."
)

MIN_CHARS = 1
MAX_CHARS = 159


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not text:
        problems.append("entry is empty")
    if text.strip() == "":
        problems.append("entry is only whitespace")
    if len(text) < MIN_CHARS:
        problems.append("entry is shorter than %d characters" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def entry_sha256(text):
    """Return the hex SHA-256 of the entry's UTF-8 bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_entry(text, path):
    """Write the entry to ``path`` and verify it by reading it back.

    Returns the SHA-256 of the bytes on disk. Raises on any mismatch.
    """
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != data:
        raise ValueError("read-back mismatch for %s" % path)
    return hashlib.sha256(on_disk).hexdigest()


def main(argv=None):
    """Validate the entry, write it, and report its length and hash."""
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("ERROR: %s" % problem, file=sys.stderr)
        return 1

    here = os.path.dirname(os.path.abspath(__file__))
    paths = [os.path.join(here, "entry.txt")]
    output_dir = "/output"
    if os.path.isdir(output_dir):
        paths.append(os.path.join(output_dir, "entry.txt"))

    hashes = [write_entry(ENTRY, path) for path in paths]
    if len(set(hashes)) != 1:
        print("ERROR: output hashes disagree", file=sys.stderr)
        return 1

    print("entry: %s" % ENTRY)
    print("characters: %d" % len(ENTRY))
    print("sha256: %s" % hashes[0])
    for path in paths:
        print("wrote: %s" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
