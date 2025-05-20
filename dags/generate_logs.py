import random
import time

def generate_log_entry():
    ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    date = time.strftime("[%d/%b/%Y:%H:%M:%S]")  # Format de date
    request = f"GET /path/to/resource HTTP/1.1"
    status_code = random.choice([200, 404, 500])
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    
    return f'{ip} - - {date} "{request}" {status_code} - "{user_agent}"'

# Générer 1000 entrées de logs
with open("logs.txt", "w") as f:
    for _ in range(1000):
        f.write(generate_log_entry() + "\n")

print("Logs générés dans logs.txt")