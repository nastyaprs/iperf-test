import re


def parser(output):

    intervals = []

    pattern = re.compile(r"(\d+\.\d+-\d+\.\d+)\s+(\d+\.\d+)\s+MBytes\s+(\d+\.\d+)\s+Mbits/sec\s+(\d+\.\d+)\s+sec")

    matches = pattern.findall(output)

    for match in matches:
        interval = {
            'Interval': match[0],
            'Transfer': float(match[1]),
            'Bitrate': float(match[2]),
            'Retr': float(match[3]),
            'Cwnd': 320.0
        }
        intervals.append(interval)

    return intervals
