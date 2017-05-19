import argparse
from log_parser import LogParser


def parse_arguments():
    """
    Parse the application argument, the log file to be processed
    """
    parser = argparse.ArgumentParser(description='Parse a log file')
    parser.add_argument('log_file', metavar='LogFile', type=str,
                        help='the log file to be parsed')
    return parser.parse_args()


def main():
    """
    Application entry point
    """
    args = parse_arguments()
    log_parser = LogParser(args.log_file)
    log_parser.parse_file()
    print(log_parser.format_result())


if __name__ == '__main__':
    main()
