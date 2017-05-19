import log_parser


def test_order_dict():
    dictionary = {'a': 1, 'b': 234, 'c': 5, 'd': 9}
    expected = [('b', 234), ('d', 9), ('c', 5), ('a', 1)]
    kv_list = log_parser.LogParser.order_dict(dictionary)
    assert kv_list == expected


def test_order_empty_dict():
    dictionary = {}
    expected = []
    kv_list = log_parser.LogParser.order_dict(dictionary)
    assert kv_list == expected


def test_order_dict_single_element():
    dictionary = {'a': 1}
    expected = [('a', 1)]
    kv_list = log_parser.LogParser.order_dict(dictionary)
    assert kv_list == expected


def test_format_dict():
    kv_list = [('b', 234), ('d', 9), ('c', 5), ('a', 1)]
    expected = 'b - 234\nd - 9\nc - 5\na - 1'
    result = log_parser.LogParser.format_dict(kv_list)
    assert result == expected


def test_increment_count():
    dictionary = {}
    expected = {'a': 1}
    log_parser.LogParser.increment_count(dictionary, 'a')
    assert dictionary == expected

    expected = {'a': 2}
    log_parser.LogParser.increment_count(dictionary, 'a')
    assert dictionary == expected

    expected = {'a': 2, 'b': 1}
    log_parser.LogParser.increment_count(dictionary, 'b')
    assert dictionary == expected


def test_process_url():
    parser = log_parser.LogParser('log.txt')
    expected = {'http://localhost': 1}
    parser.process_url('http://localhost')
    assert parser.urls == expected


def test_process_status_code():
    parser = log_parser.LogParser('log.txt')
    expected = {'400': 1}
    parser.process_status_code('400')
    assert parser.status_codes == expected


def test_process_line():
    line = 'level=info request_to="http://localhost" response_status="200"'
    parser = log_parser.LogParser('log.txt')
    urls_expected = {'http://localhost': 1}
    status_codes_expected = {'200': 1}
    parser.process_line(line)
    assert parser.urls == urls_expected
    assert parser.status_codes == status_codes_expected


def test_process_line_strange_url():
    line = ('level=info request_to="http://localHost-13.com.br/test" '
            'response_status="200"')
    parser = log_parser.LogParser('log.txt')
    urls_expected = {'http://localHost-13.com.br/test': 1}
    status_codes_expected = {'200': 1}
    parser.process_line(line)
    assert parser.urls == urls_expected
    assert parser.status_codes == status_codes_expected


def test_process_file():
    parser = log_parser.LogParser('log.txt')
    urls_expected = {'http://localHost-13.com.br/test': 2,
                     'http://localhost': 1}
    status_codes_expected = {'200': 2, '400': 1}
    parser.parse_file()
    assert parser.urls == urls_expected
    assert parser.status_codes == status_codes_expected


def test_format_result():
    parser = log_parser.LogParser('log.txt')
    urls_expected = {'http://localHost-13.com.br/test': 2,
                     'http://localhost': 1}
    status_codes_expected = {'200': 2, '400': 1}
    parser.parse_file()
    assert parser.urls == urls_expected
    assert parser.status_codes == status_codes_expected
    result = parser.format_result()
    expected = ('http://localHost-13.com.br/test - 2\n'
                'http://localhost - 1\n\n'
                '200 - 2\n'
                '400 - 1')
    assert result == expected
