import psutil
import time

import json


def log_constructor():
    # CPU logs
    cpu_usage_percentage = psutil.cpu_percent(interval=1)
    cpu_number_logical = psutil.cpu_count()
    cpu_number_physical = psutil.cpu_count(logical=False)
    cpu_t = psutil.cpu_times()
    cpu_per_cpu_percentage = psutil.cpu_percent(interval=1, percpu=True)

    # Networks
    network_num_data = psutil.net_io_counters()

    # Generating log
    log = {
        'metrics_took_at': time.time(),
        'metrics': {
            'cpu':
                {
                    'cpu_usage_percentage': cpu_usage_percentage,
                    'cpu_number_logical': cpu_number_logical,
                    'cpu_number_physical': cpu_number_physical,
                    'cpu_per_cpu_percentage': cpu_per_cpu_percentage,
                    'cpu_times': cpu_t._asdict(),
                },
            'memory': psutil.virtual_memory()._asdict(),
            'network': network_num_data._asdict()
        },
    }

    result = (json.dumps(log, indent=4))
    with open("log.txt", "a") as log_file:
        log_file.write(result)
        log_file.write("\n")

    return result


