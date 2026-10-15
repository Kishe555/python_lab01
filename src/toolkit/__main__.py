import argparse
import sys

from .calculator import solve
from .converter import convert
from .errors import ToolkitError

def main() -> float:
    parser = argparse.ArgumentParser(description="Калькулятор и конвертер")

    commands = parser.add_subparsers(dest="command", required=True)

    calc_parser = commands.add_parser("calc")
    calc_parser.add_argument("expression")

    convert_parser = commands.add_parser("convert")
    convert_parser.add_argument("value")
    convert_parser.add_argument("--from", dest="unit1", required=True)
    convert_parser.add_argument("--to", dest="unit2", required=True)

    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = solve(args.expression)

        else:
            result = convert(args.value, args.unit1, args.unit2)
        print(result)

    except ToolkitError as e:

        print(e, file=sys.stderr)

        sys.exit(2)

if __name__ == "__main__":
    main()


#python -m pytest --cov=src/toolkit --cov-report=term-missing
#команда в терминал для проверки покрытия тестами