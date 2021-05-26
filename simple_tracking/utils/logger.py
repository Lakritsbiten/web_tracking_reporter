import datetime
import os

from simple_tracking.utils.singleton import Singleton
from simple_tracking.utils.dt_conversions import datetime_from_local_to_utc, dt_fmt


class VisitorLog(metaclass=Singleton):
    LOG_FILE_NAME = 'visitors.log'
    SEP = '|'

    def __init__(self, logfile=os.path.join('../', LOG_FILE_NAME)):
        self.__log_file = logfile
        self.write_header()

    def write_header(self):
        if not os.path.exists(self.__log_file):
            with open(self.__log_file, 'w+') as f:
                f.write('|timestamp|url|userid|\n')

    def visit_entry(self, local_time, url, user_id):
        utc_timestamp = datetime_from_local_to_utc(local_time).strftime(dt_fmt)
        timezone = 'UTC'
        a_visit = '{}{}{} {}{} {}{} {}\n'.format(self.SEP, utc_timestamp, timezone, self.SEP, url, self.SEP,
                                                 user_id, self.SEP)
        return a_visit

    def log(self, url, userid):
        local_time = datetime.datetime.now()
        with open(self.__log_file, "a+") as f:
            print('Logging visit to {} by userid {} in logfile {}'
                  .format(url, userid, os.path.abspath(self.__log_file)))
            f.write(self.visit_entry(local_time, url, userid))


if __name__ == '__main__':
    print(id(VisitorLog('../../')))
