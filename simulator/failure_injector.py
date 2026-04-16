import os

def kill_db():
    os.system("docker stop aiops-agentic-system-db-1")

def high_latency():
    print("Simulating latency spike...")

def inject_failure():
    choice = input("Choose failure (db/latency): ")

    if choice == "db":
        kill_db()
    elif choice == "latency":
        high_latency()