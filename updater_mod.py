import os, time, glob, pathlib,shutil,datetime
from shutil import copyfile, rmtree

now = datetime.datetime.now()
file_log = open('log.txt', 'w', encoding='utf-8')
file_log.write("""
========================
Робот обновления процессингого центра 3-CardF
Updater 3-CardF v 1.0
Обновляемый список модулей:
Acquirer, Issuer, GateVisa2, GateVisa3, Spars, HUMR, SYSMON, EMS,
KEYDB, HSMHOST, HSMGATE, Router, InterCHange, Iswitch, GateAFS, 
Multigate, MuxgateMon, GateWay4, MuxGate, GateMIR, GATEMC
Процесс обновления доступен в лог файле log.txt, если будет найден неизвестный модуль, то это будет указано в лог файле
c0d3d by RabbitPul9 2021
========================
\n""")
file_log.write(str(now) + " Робот обновления 3-CardF запущен\n")

path = "C:\\Release\\"
# Sort file names with path
file_list = os.listdir(path)
full_list = [os.path.join(path, i) for i in file_list]
last_catalog = full_list[0-1]
print(last_catalog)
listik = []
list_mods = ['0773200.exe', '0773200.exe', '0081500.exe', '0081600.exe', '0193000.exe', '0049200.exe', '0020100.exe', '0081900.exe',
'0193100.exe', '0192000.exe', '0210900.exe', '0055100.exe', '0055000.exe', '0055000.exe', '0055000.exe', '0774600.exe', '0196000.exe',
'0081700.exe', '0200200.exe', '0191100.exe', '0077900.exe']#список модулей для обновления
for root, dirs, files in os.walk(last_catalog):  
    for filename in files:
        #print(filename)
        list_upd = filename
        #print(list_upd)
        listik.append(list_upd)
        #print(last_catalog + '\\' + filename)
        if filename in list_mods:
            file_log.write(str(now) + f" Найден для обновления модуль {filename}\n")
            print("Копирование модуля " + filename)
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\\EXE220")
            file_log.write(str(now) + f" Модуль {filename} обновлен\n")
        else: 
            file_log.write(str(now) + " Найден неизвестный модуль, требуется обновление в ручном режиме\n")
