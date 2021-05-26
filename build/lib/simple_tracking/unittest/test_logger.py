import unittest
from datetime import datetime
from simple_tracking.utils.logger import VisitorLog


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.__logger = VisitorLog()

    def test_log_entry_without_daylight_saving(self):
        timestamp = 1545730073      # 2018-12-25 09:27:53
        dt = datetime.fromtimestamp(timestamp)
        log_entry = self.__logger.visit_entry(dt, '/unittest_example.html', 12345)
        expected_result = '|2018-12-25 08:27:53UTC |/unittest_example.html |12345 |\n'
        self.assertEqual(log_entry, expected_result)

    def test_log_entry_with_daylight_saving(self):
        timestamp = 1588734073      # 2020-05-06 03:01:13
        dt = datetime.fromtimestamp(timestamp)
        log_entry = self.__logger.visit_entry(dt, '/root/unittest_example.html', 6789)
        expected_result = '|2020-05-06 03:01:13UTC |/root/unittest_example.html |6789 |\n'
        self.assertEqual(log_entry, expected_result)