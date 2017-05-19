import re

LINE_REGEX = r'(response_status|request_to)=\"([0-9a-zA-Z:\/\.\-]+)"'


class LogParser:
    """
    Provides functionality to parse log files
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.urls = {}
        self.status_codes = {}

    @staticmethod
    def order_dict(dictionary):
        """
        Returns a sorted list of key/value from the dictionary
        """
        return sorted(dictionary.items(), key=lambda kv: kv[1],
                      reverse=True)

    @staticmethod
    def format_dict(kv_list):
        """
        Prints the list of key/value in a human understandable manner
        """
        return '\n'.join(['{} - {}'.format(key, value) for
                          key, value in kv_list])

    @staticmethod
    def increment_count(dictionary, key):
        """
        Increments the count of a given key in a dictionary.
        If the key does not exist in the dictionary,
        adds the key with value = 1
        """
        if key:
            if key in dictionary:
                dictionary[key] += 1
            else:
                dictionary[key] = 1

    def process_url(self, url):
        """
        Increments the count of a given url
        """
        LogParser.increment_count(self.urls, url)

    def process_status_code(self, status_code):
        """
        Increments the count of a given status code
        """
        LogParser.increment_count(self.status_codes, status_code)

    def format_result(self):
        """
        Prints the result of the log parsing
        The result is composed by the 3 most accessed urls and
        the count of webhook by status code
        """
        return ('{}\n\n{}'.format(
            LogParser.format_dict(LogParser.order_dict(self.urls)[:3]),
            LogParser.format_dict(LogParser.order_dict(self.status_codes))))

    def process_line(self, line):
        """
        Get the data from the log line.

        Since for this log parser we only need the url and status code,
        only this data is pulled from the line.

        The process of getting the info is:
            1 - using a regex, all the values needed are pulled from the string
            2 - the value is then broken into a dictionary
            3 - the values of the url and status codes are added to the
                counters
        """
        find_result = re.findall(LINE_REGEX, line)
        line_data = {r[0]: r[1] for r in find_result}
        self.process_url(line_data.get('request_to'))
        self.process_status_code(line_data.get('response_status'))

    def parse_file(self):
        """
        Opens the logg file, perform the parse of the file and
        then print the results
        """
        with open(self.file_name, 'r', errors='ignore') as log_file:
            for line in log_file:
                self.process_line(line)
