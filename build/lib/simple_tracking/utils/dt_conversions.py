import datetime
import time

dt_fmt = '%Y-%m-%d %H:%M:%S'

def datetime_from_local_to_utc(local_datetime):
    now_timestamp = time.time()
    offset = datetime.datetime.utcfromtimestamp(now_timestamp) - datetime.datetime.fromtimestamp(now_timestamp)
    return local_datetime + offset


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset
