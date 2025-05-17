import os

def print_version():
    print("App Version:", os.environ.get("APP_VERSION", "Unknown"))

if __name__ == "__main__":
    print_version()