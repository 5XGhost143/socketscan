import time
from system_utils import check_os_support, check_admin_rights
from network_utils import get_network_connections, format_connection

def main():
    check_os_support()
    check_admin_rights()

    seen_connections = set()
    print(f"{'Proto':<7} {'Local Address':<25} {'Remote Address':<25} {'Status':<20} {'PID':<7} {'Process':<20} {'Path'}")
    print("=" * 140)

    try:
        while True:
            current_set = set()
            connections = get_network_connections()

            for conn in connections:
                data = format_connection(conn)
                conn_id = tuple(data)

                current_set.add(conn_id)

                if conn_id not in seen_connections:
                    print(f"{data[0]:<7} {data[1]:<25} {data[2]:<25} {data[3]:<20} "
                          f"{data[4]:<7} {data[5]:<20} {data[6]}")
                    time.sleep(0.1)

            seen_connections = current_set
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n❎ Real-time monitoring stopped.")

if __name__ == "__main__":
    main()