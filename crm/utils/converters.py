def convert_ts_to_milliseconds(ts):
    return int(round(ts.timestamp() * 1000))
