def read_logs(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()
    return logs