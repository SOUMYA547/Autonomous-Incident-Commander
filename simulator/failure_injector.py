import random

def generate_logs():
    normal = [
        "user login success",
        "payment processed",
        "request completed"
    ]

    errors = [
        "DB error connection failed",
        "timeout error in service",
        "500 internal server error"
    ]

    logs = normal * 5 + random.sample(errors, 2)
    random.shuffle(logs)

    return logs