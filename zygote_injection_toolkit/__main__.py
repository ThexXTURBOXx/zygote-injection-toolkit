import sys

from .stage1 import Stage1Exploit
from .stage2 import Stage2Exploit


def main(argv: list[str]) -> None:
    print("This package is very experimental!")
    port = 4321
    if argv[1:]:
        try:
            port = int(argv[1])
        except ValueError:
            print(f"Invalid port number: {argv[1]}", file=sys.stderr)
            sys.exit(1)
    stage_1_exploit: Stage1Exploit = Stage1Exploit(port=port)
    if not stage_1_exploit.exploit_stage1():
        print("Stage 1 failed!", file=sys.stderr)
    state_2_exploit: Stage2Exploit = Stage2Exploit(port=port)
    state_2_exploit.exploit_stage2()


if __name__ == "__main__":
    main(sys.argv)
