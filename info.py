import platform
import psutil
import os
import shutil
import subprocess
import GPUtil
import re

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

print ("""                                            
███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗
████╗ ████║██╔══██╗██║   ██║██║██╔════╝
██╔████╔██║███████║██║   ██║██║███████╗
██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║
██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║
╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
                  """)

print(f"🎉 A warm welcome from Peharge 🎉\n")

def check_cuda():
    try:
        output = subprocess.check_output(["nvidia-smi"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True if "CUDA" in output else False
    except Exception:
        return False

def check_rocm():
    try:
        output = subprocess.check_output(["rocm-smi"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True if "ROCm" in output else False
    except Exception:
        return False

def get_system_info():
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    cpu = platform.processor()
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # in GB

    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    total_storage = round(total_storage / (1024 ** 3), 2)  # in GB
    free_storage = round(free_storage / (1024 ** 3), 2)  # in GB

    gpus = GPUtil.getGPUs()
    gpu_info = [(gpu.name, gpu.memoryTotal) for gpu in gpus]

    cuda_support = check_cuda()
    rocm_support = check_rocm()

    return {
        "OS": f"{blue}{os_name} {os_release} {reset}(Version: {os_version})",
        "CPU": f"{blue}{cpu}{reset}",
        "RAM": f"{blue}{ram} GB{reset}",
        "Storage": f"Total: {blue}{total_storage} GB{reset}, {blue}Free: {free_storage} GB{reset}",
        "GPU": gpu_info,
        "CUDA Support": f"{blue}{cuda_support}{reset}",
        "ROCm Support": f"{blue}{rocm_support}{reset}"
    }

def mavis_compatibility(ram, cuda_support, rocm_support):
    if ram < 8:
        return f"{red}MAVIS is not supported on this system.{reset}"
    elif 8 <= ram < 15:
        return f"{red}MAVIS in limited mode is supported.{reset}"
    elif 15 < ram < 63:
        return f"{green}MAVIS 11B is supported.{reset}"
    elif ram > 64:
        return f"{green}MAVIS 90B is supported.{reset}"

def remove_color_codes(text):
    return re.sub(r'\033\[[0-9;]*m', '', text)

def main():
    system_info = get_system_info()

    print("System Information:")
    print("-------------------")
    for key, value in system_info.items():
        if key == "GPU":
            if value:
                print(f"{key}: {', '.join([f'{gpu[0]} ({gpu[1]} MB)' for gpu in value])}")
            else:
                print(f"{key}: No GPU detected")
        else:
            print(f"{key}: {value}")

    ram_str = remove_color_codes(system_info["RAM"])
    ram = float(ram_str.split()[0])

    cuda_support = check_cuda()
    rocm_support = check_rocm()

    compatibility = mavis_compatibility(ram, cuda_support, rocm_support)
    gpu_or_cpu = "GPU" if cuda_support or rocm_support else "CPU"

    print("\nCompatibility and Execution Mode:")
    print("-----------------------------------")
    print(compatibility)
    print(f"Execution Mode: {blue}{gpu_or_cpu}{reset}\n")
    print("Flask information:")
    print("-----------------------------------")

if __name__ == "__main__":
    main()
