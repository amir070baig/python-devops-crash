import psutil
import json
from datetime import datetime

def get_system_health():
    health = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }
    return health

if __name__ == "__main__":
    data = get_system_health()
    print(json.dumps(data, indent=4))
