import platform
import ctypes
import os
import sys

def check_os_support():
    system = platform.system()
    if system == "Windows":
        release = platform.release()
        if release not in ("10", "11"):
            print(f"❌ Unsupported Windows version: {release}. Only Windows 10 and newer are supported.")
            sys.exit(1)
    elif system == "Linux":
        return
    else:
        print(f"❌ Unsupported operating system: {system}. Only Windows 10+ and Linux are supported.")
        sys.exit(1)

def is_admin():
    try:
        if os.name == 'nt':
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except Exception:
        return False

def check_admin_rights():
    if not is_admin():
        system = platform.system()
        if system == "Windows":
            print("❌ No Admin Rights. Please run as Administrator.")
        elif system == "Linux":
            print("❌ No Admin Rights. Please run with sudo.")
        else:
            print("❌ No Admin Rights. Please run with appropriate privileges.")
        sys.exit(1)