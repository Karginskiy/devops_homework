import sys
import sched
import socket
import time

hosts_to_resolve = []
timer_value = 30000
resolved_hosts = {}


def repeatable_ip_resolver():
    for host in hosts_to_resolve:
        try:
            previous_ip = resolved_hosts.get(host)
            resolved_ip = socket.gethostbyname(host)
            if previous_ip is not None and previous_ip != resolved_ip:
                print("[ERROR] {} IP mismatch: {} {}".format(host, previous_ip, resolved_ip))

            resolved_hosts.update({host: resolved_ip})
            print("{} - {}".format(host, resolved_ip))
        except Exception:
            print("Cannot find ip for host: " + host)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('''
================================ HELP ================================
    use ip_resolver.py [<timer>] <host1> [<host2>] [<hostN>] where are 
        <timer> - interval between process of resolving in millis
        <host1> - <hostN> - hosts to resolve and check ip
======================================================================
''')

    if len(sys.argv) > 1:
        is_timer_value_provided = False
        if sys.argv[1].isdigit():
            is_timer_value_provided = True
            timer_value = int(sys.argv[1])
        slice_index = 2 if is_timer_value_provided else 1
        for arg in sys.argv[slice_index:]:
            hosts_to_resolve.append(arg)

while True:
    repeatable_ip_resolver()
    time.sleep(timer_value / 1000)




