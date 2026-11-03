import sys

from .core import format, parse


def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("usage: dura DURATION...", file=sys.stderr)
        return 2
    for arg in args:
        print(format(parse(arg)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
