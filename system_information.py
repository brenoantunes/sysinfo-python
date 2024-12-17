import platform
import os
import psutil
import wmi
import subprocess

def get_system_info():
    system_info = {}

    # Sistema Operacional e Edição
    if platform.system() == "Windows":
        c = wmi.WMI()
        for os_info in c.Win32_OperatingSystem():
            system_info['Sistema Operacional'] = os_info.Caption  # Inclui a edição (ex: Windows 10 Pro)
        
        # Marca, Modelo e Número de Série
        for system in c.Win32_ComputerSystem():
            system_info['Marca'] = system.Manufacturer
            system_info['Modelo'] = system.Model

        for bios in c.Win32_BIOS():
            system_info['Número de Série'] = bios.SerialNumber

    else:
        # Para outros sistemas
        system_info['Sistema Operacional'] = platform.system() + " " + platform.release()
        system_info['Marca'] = "Não disponível"
        system_info['Modelo'] = "Não disponível"
        system_info['Número de Série'] = "Não disponível"

    # Processador
    system_info['Processador'] = platform.processor()

    # Memória RAM
    total_memory = psutil.virtual_memory().total / (1024 ** 3)
    system_info['Memória RAM'] = f"{total_memory:.2f} GB"

    return system_info

def save_to_txt(data, filename="system_info.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Informações salvas em {filename}")

if __name__ == "__main__":
    info = get_system_info()
    save_to_txt(info)
