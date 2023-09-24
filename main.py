import sys
import random
import wmi
import multiprocessing
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QGuiApplication, QColor
from PySide6.QtQml import  QQmlApplicationEngine


        
colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]
        
def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])
    
    
def get_process_info():    

    f = wmi.WMI()
    processes = []
    
    for process in f.Win32_PerfFormattedData_PerfProc_Process():
        
        p_name = process.Name
        p_pid = str(process.IDProcess)
        p_cpu = str(process.PercentProcessorTime)
        print(p_cpu)
        try:
            p_ram = str(int(process.TotalP) / (1024*1024))
        except (ValueError, TypeError):
            p_ram = 'N/A'
        processes.append({"PID": p_pid, "Name": p_name, "CPU": p_cpu , "RAM": p_ram})
        
        
    return processes


arr = get_process_info()
app = QApplication()
table = QTableWidget()
table.setRowCount(len(arr))
table.setColumnCount(4)
table.setHorizontalHeaderLabels(["PID", "Name", "CPU Usage", "RAM Usage"])

#processes = [{"PID": 1, "Name": "Test 1"},{"PID": 2, "Name": "Test 2"},{"PID":3, "Name": "Test 3"}]
i=0

for process in arr:
    
    item_name = QTableWidgetItem(process["Name"])
    item_pid = QTableWidgetItem(str(process["PID"]))
    item_cpu = QTableWidgetItem(str(process["CPU"]))
    item_ram = QTableWidgetItem(str(process["RAM"]))
    
    
    
    table.setItem(i, 0, item_pid)
    table.setItem(i, 1, item_name)
    table.setItem(i, 2, item_cpu)
    table.setItem(i, 3, item_ram)
   
    
    i+=1
    
table.show()
sys.exit(app.exec())