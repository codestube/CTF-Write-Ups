#!/usr/bin/env python3
import re
import sys
import textwrap
from pathlib import Path

WIDTH = 80

BLOCK_RE = re.compile(
    r"(<pre\b[^>]*>\s*<code\b[^>]*>)(.*?)(</code>\s*</pre>)",
    re.IGNORECASE | re.DOTALL,
)

LEADING_WS_RE = re.compile(r"^\s*")

# Examples this tries to align nicely:
#   👤 player: > message...
#   ⚖️ lawyer: message...
#   🚩  FLAG...
PREFIX_PATTERNS = [
    re.compile(r"^(.{0,40}?:\s*(?:>\s*)?)"),  # "player: > " / "judge: "
    re.compile(r"^(\S+\s{2,})"),              # "🚩  " / "🎉  "
]


def hanging_prefix(content: str) -> str:
    for pat in PREFIX_PATTERNS:
        m = pat.match(content)
        if m and m.group(1).strip():
            return m.group(1)
    return ""


def wrap_line(line: str, width: int = WIDTH) -> str:
    if not line.strip():
        return line

    if len(line) <= width:
        return line

    leading = LEADING_WS_RE.match(line).group(0)
    content = line[len(leading):]

    prefix = hanging_prefix(content)
    subsequent_indent = leading + (" " * len(prefix) if prefix else "")

    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=leading,
        subsequent_indent=subsequent_indent,
        expand_tabs=False,
        replace_whitespace=True,
        drop_whitespace=True,
        break_long_words=True,
        break_on_hyphens=False,
    )

    return wrapper.fill(content)


def wrap_block_text(text: str, width: int = WIDTH) -> str:
    lines = text.splitlines(keepends=True)
    out = []

    for line in lines:
        newline = ""
        if line.endswith("\r\n"):
            newline = "\r\n"
            raw = line[:-2]
        elif line.endswith("\n"):
            newline = "\n"
            raw = line[:-1]
        elif line.endswith("\r"):
            newline = "\r"
            raw = line[:-1]
        else:
            raw = line

        wrapped = wrap_line(raw, width)

        wrapped_lines = wrapped.splitlines() or [""]
        for i, part in enumerate(wrapped_lines):
            if i < len(wrapped_lines) - 1:
                out.append(part + newline)
            else:
                out.append(part + newline)

    return "".join(out)


def replacer(match: re.Match) -> str:
    start, body, end = match.groups()
    return start + wrap_block_text(body, WIDTH) + end


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(
            f"usage: {Path(sys.argv[0]).name} input.md [output.md]",
            file=sys.stderr,
        )
        sys.exit(1)

    in_path = Path(sys.argv[1])
    if len(sys.argv) == 3:
        out_path = Path(sys.argv[2])
    else:
        out_path = in_path.with_name(f"{in_path.stem}.wrapped{in_path.suffix}")

    data = in_path.read_text(encoding="utf-8")
    wrapped = BLOCK_RE.sub(replacer, data)
    out_path.write_text(wrapped, encoding="utf-8")

    print(f"[+] wrote {out_path}")


if __name__ == "__main__":
    main()