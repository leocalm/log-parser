import argparse
from log_parser import LogParser


def parse_arguments(argv=None):
    """
    Parse the application argument, the log file to be processed
    """
    parser = argparse.ArgumentParser(description='Parse a log file')
    parser.add_argument('log_file', metavar='LogFile', type=str,
                        help='the log file to be parsed')
    return parser.parse_args(argv)


def main(argv=None):
    """
    Application entry point
    """
    args = parse_arguments(argv)
    log_parser = LogParser(args.log_file)
    log_parser.parse_file()
    print(log_parser.format_result())


if __name__ == '__main__':
    main()
