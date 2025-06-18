import datetime

def log_activity(user_id, action):
    with open(f"{user_id}_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().isoformat()
        log_file.write(f"[{timestamp}] {action}\n")