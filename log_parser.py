def parse_logs(raw_logs):
    cleaned = []

    for log_block in raw_logs:
        lines = log_block.split("\n")
        for line in lines:
            if line.strip():
                cleaned.append(line.strip())

    return cleaned