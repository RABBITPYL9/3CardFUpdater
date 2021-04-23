import stopmodule
import startmodule


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
for root, dirs, files in os.walk(last_catalog):  
    for filename in files:
        #print(filename)
        list_upd = filename
        #print(list_upd)
        listik.append(list_upd)
        #print(last_catalog + '\\' + filename)
        if filename == '0773200.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateVisa3\n")
            print("Копирование модуля GateVisa3")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateVisa3 обновлен\n")
        elif filename == '0773100.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateVisa2\n")
            print("Копирование модуля GateVisa2")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateVisa2 обновлен\n")
        elif filename == '0081500.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateMC\n")
            print("Копирование модуля GateMC")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateMC обновлен\n")
        elif filename == '0081600.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateMIR\n")
            print("Копирование модуля GateMIR")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateMIR обновлен\n")
        elif filename == '0193000.exe':
            file_log.write(str(now) + " Найден для обновления модуль MuxGate\n")
            print("Копирование модуля MuxGate")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль MuxGate обновлен\n")
        elif filename == '0049200.exe':
            file_log.write(str(now) + " Найден для обновления модуль Issuer\n")
            print("Копирование модуля Issuer")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль Issuer обновлен\n")
        elif filename == '0020100.exe':
            file_log.write(str(now) + " Найден для обновления модуль Acquirer\n")
            print("Копирование модуля Acquirer")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль Acquirer обновлен\n")
        elif filename == '0081900.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateWay4\n")
            print("Копирование модуля GateWay4")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateWay4 обновлен\n")
        elif filename == '0193100.exe':
            file_log.write(str(now) + " Найден для обновления модуль MuxGateMon\n")
            print("Копирование модуля MuxGateMon")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль MuxGateMon обновлен\n")
        elif filename == '0192000.exe':
            file_log.write(str(now) + " Найден для обновления модуль MultiGate\n")
            print("Копирование модуля MultiGate")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль MultiGate обновлен\n")
        elif filename == '0210900.exe':
            file_log.write(str(now) + " Найден для обновления модуль GateAFS\n")
            print("Копирование модуля GateAFS")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль GateAFS обновлен\n")
        elif filename == '0055100.exe':
            file_log.write(str(now) + " Найден для обновления модуль Iswitch\n")
            print("Копирование модуля Iswitch")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль Iswitch обновлен\n")
        elif filename == '0055000.exe':
            file_log.write(str(now) + " Найден для обновления модуль InterChange\n")
            print("Копирование модуля InterChange")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль InterChange обновлен\n")
        elif filename == '0055000.exe':
            file_log.write(str(now) + " Найден для обновления модуль Router\n")
            print("Копирование модуля Router")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль Router обновлен\n")
        elif filename == '0774500.exe':
            file_log.write(str(now) + " Найден для обновления модуль HSMGATE\n")
            print("Копирование модуля HSMGATE")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль HSMGATE обновлен\n")
        elif filename == '0774600.exe':
            file_log.write(str(now) + " Найден для обновления модуль HSMHOST\n")
            print("Копирование модуля HSMHOST")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль HSMHOST обновлен\n")
        elif filename == '0196000.exe':
            file_log.write(str(now) + " Найден для обновления модуль KEYDB\n")
            print("Копирование модуля KEYDB")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль KEYDB обновлен\n")
        elif filename == '0081700.exe':
            file_log.write(str(now) + " Найден для обновления модуль EMS\n")
            print("Копирование модуля EMS")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль EMS обновлен\n")
        elif filename == '0200200.exe':
            file_log.write(str(now) + " Найден для обновления модуль SYSMON\n")
            print("Копирование модуля SYSMON")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль SYSMON обновлен\n")
        elif filename == '0191100.exe':
            file_log.write(str(now) + " Найден для обновления модуль HUMR\n")
            print("Копирование модуля HUMR")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль HUMR обновлен\n")
        elif filename == '0077900.exe':
            file_log.write(str(now) + " Найден для обновления модуль SPARS\n")
            print("Копирование модуля SPARS")
            shutil.copy(last_catalog + '\\' + filename, "C:\\UC3D\EXE220")
            file_log.write(str(now) + " Модуль SPARS обновлен\n")
        else: 
            file_log.write(str(now) + " Найден неизвестный модуль, требуется обновление в ручном режиме\n")

startmodule.test_login(driver)
startmodule.start_pc(driver)
