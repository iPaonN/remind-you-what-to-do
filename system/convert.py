"""CALING TIME"""

import re

def convert(time_str: str) -> int:
    """Used to calculating time for input"""
    time_dict = {'s': 1, 'm': 60, 'h':3600, 'd':3600*24}
    # this pattern looks for days, hours, minutes, seconds in the string, etc
    regex_pattern = r"(\d+)([smhd])"
    # matches = re.match(regex_pattern, time_str)
    matches = re.findall(regex_pattern, time_str)
    total_time = 0
    for amount, unit in matches:
        total_time += int(amount) * time_dict[unit]
    return total_time
