import pandas
import os
import datetime

from simple_tracking.utils.logger import VisitorLog
from simple_tracking.utils.dt_conversions import dt_fmt


class Reporter(object):

    def __init__(self, log_file=os.path.join('../', VisitorLog.LOG_FILE_NAME)):
        self.__log_file = log_file

    @staticmethod
    def convert_to_datetime(log_time):
        timestamp = log_time[:19]
        return datetime.datetime.strptime(timestamp, dt_fmt)

    def to_dataframe(self):
        df = pandas.read_csv(self.__log_file, sep=VisitorLog.SEP, usecols=[1, 2, 3])
        df['timestamp'] = df['timestamp'].apply(self.convert_to_datetime)
        df.sort_values(by=['timestamp'], inplace=True, ascending=True)  # probably not needed
        return df

    @staticmethod
    def __filter_by_time(df, start_time, end_time):
        # greater than or equal to the start date and smaller than the end date
        mask = (df['timestamp'] >= start_time) & (df['timestamp'] < end_time)
        return df.loc[mask]

    @staticmethod
    def __group_by_column(df, column_name):
        return df.groupby(column_name)

    @staticmethod
    def __count_unique(df, column_name):
        return df[column_name].nunique()

    @staticmethod
    def __count_rows(df, column_name):
        return df[column_name].count()

    def get_report(self, start_time, end_time):
        result = 'No entries'
        df = self.to_dataframe()
        if not df.empty:
            df = self.__filter_by_time(df, start_time, end_time)
            df_groups = self.__group_by_column(df, 'url')

            result = '{}{}{}{}{}{}{}\n'.format(VisitorLog.SEP,
                                               'url'.ljust(14), VisitorLog.SEP,
                                               'page views'.ljust(11), VisitorLog.SEP,
                                               'visitors', VisitorLog.SEP)
            for name, group in df_groups:
                page_count = self.__count_rows(group, 'url')
                unique_visits = self.__count_unique(group, 'userid')
                result += '{}{}{}{}{}{}{}\n'.format(VisitorLog.SEP,
                                                    name.ljust(14), VisitorLog.SEP,
                                                    str(page_count).ljust(11), VisitorLog.SEP,
                                                    str(unique_visits).ljust(8), VisitorLog.SEP)
        return result


if __name__ == '__main__':
    _start_time = datetime.datetime.strptime('2021-05-25 13:07:35', dt_fmt)
    _end_time = datetime.datetime.strptime('2021-05-25 14:07:35', dt_fmt)

