import psutil
import collections
import time

import json


def log_constructor():

    # CPU logs
    cpu_usage_percentage = psutil.cpu_percent(interval = 1)
    cpu_number_logical = psutil.cpu_count()
    cpu_number_physical = psutil.cpu_count(logical=False)
    cpu_times = psutil.cpu_times()
    cpu_per_cpu_percentage = psutil.cpu_percent(interval=1, percpu=True)

    # Networks
    #  connections = psutil.net_connections(kind='inet4')
    net_addresses = psutil.net_if_addrs()
    network_interfaces = {interface : net_addresses[interface][0].address for interface in net_addresses}
    network_interfaces = collections.OrderedDict(sorted(network_interfaces.items()))

    # Memory
    memory = psutil.virtual_memory()

    # Generating log
    log = {
        'metrics_took_at':  time.time(),
        'metrics': {
            'cpu':
                {
                'cpu_usage_percentage':     cpu_usage_percentage,
                'cpu_number_logical':       cpu_number_logical,
                'cpu_number_physical':      cpu_number_physical,
                'cpu_per_cpu_percentage':   cpu_per_cpu_percentage,
                'cpu_times':                cpu_times._asdict(),
                },
            'memory': psutil.virtual_memory()._asdict(),
            'network': [network_interfaces,],
        },
    }

    return log


if __name__ == "__main__":
    print(json.dumps(log_constructor(), indent=4))
