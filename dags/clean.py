import re

def clean_and_transform_logs(logs):
    cleaned_logs = []
    log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[^]]+)\] "(?P<request>[^"]+)" (?P<status>\d+)')

    for log in logs:
        match = log_pattern.match(log.strip())
        if match:
            log_data = {
                "ip": match.group("ip"),
                "date": match.group("date"),
                "request": match.group("request"),
                "status": match.group("status")
            }
            cleaned_logs.append(log_data)

    return cleaned_logs