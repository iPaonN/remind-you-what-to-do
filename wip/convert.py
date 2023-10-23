import re
"""CALING TIME"""

def convert(time_str: str) -> int:
    time_dict = {'s': 1, 'm': 60, 'h':3600, 'd':3600*24}
    # this pattern looks for days, hours, minutes, seconds in the string, etc
    regex_pattern = r"^(?P<day>\d+d)?(?P<hour>\d+h)?(?P<minute>\d+m)?(?P<second>\d+s)?"
    matches = re.match(regex_pattern, time_str)
    total_time = 0
    for group in matches.groups():
        if not group:
            continue
        unit = group[-1]
        val = int(group[:-1])
        amount = val * time_dict[unit]
        total_time += amount
    return total_time
