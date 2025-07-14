import psutil
import socket

def get_process_info(pid):
    try:
        p = psutil.Process(pid)
        return p.name(), p.exe()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None, None

def resolve_port(port):
    try:
        return socket.getservbyport(port)
    except:
        return str(port)

def protocol_name(conn):
    proto = ''
    if conn.type == socket.SOCK_STREAM:
        proto = 'TCP'
    elif conn.type == socket.SOCK_DGRAM:
        proto = 'UDP'
    else:
        proto = str(conn.type)

    if conn.family == socket.AF_INET6:
        proto += 'v6'
    else:
        proto += 'v4'
    return proto

def format_connection(conn):
    proto = protocol_name(conn)
    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
    raddr = f"{conn.raddr.ip}:{resolve_port(conn.raddr.port)}" if conn.raddr else ""
    status = conn.status if conn.status else ""
    pid = conn.pid

    name, exe = get_process_info(pid) if pid else (None, None)

    return (
        proto,
        laddr,
        raddr,
        status,
        str(pid) if pid else '',
        name if name else '',
        exe if exe else ''
    )

def get_network_connections():
    return psutil.net_connections(kind='inet')