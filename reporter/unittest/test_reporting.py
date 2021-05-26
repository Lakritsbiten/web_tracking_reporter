import unittest
from io import StringIO
from datetime import datetime

from reporter import reporting
from simple_tracking.utils.dt_conversions import dt_fmt

test_case_1 = \
            """|timestamp|url|userid|
            |2013-09-01 09:00:00UTC |/contact.html |12345 |
            |2013-09-01 09:00:00UTC |/contact.html |12346 |
            |2013-09-01 10:00:00UTC |/contact.html |12345 |
            |2013-09-01 10:01:00UTC |/about.html   |12347 |
            |2013-09-01 11:00:00UTC |/contact.html |12347 |"""

test_case_1_expected_result = \
                                """|url           |page views |visitors|
|/about.html   |1          |1       |
|/contact.html |3          |2       |
"""


class TestReporting(unittest.TestCase):

    def test_group_by_url_and_filter_by_time(self):
        in_mem_csv = StringIO(test_case_1)
        start_time = datetime.strptime('2013-09-01 09:00:00', dt_fmt)
        end_time = datetime.strptime('2013-09-01 10:59:59', dt_fmt)

        result = reporting.Reporter(in_mem_csv).get_report(start_time, end_time)
        self.assertEqual(result, test_case_1_expected_result)
