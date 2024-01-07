import os
import datetime

def log_rotate(dir):
     file = os.listdir(dir)
     for i in file:
      type = i[-4:]
      if(type == ".log"):  
        sta = os.stat(f"{dir}/{i}")
        time = datetime.datetime.fromtimestamp(sta.st_mtime)
        thr = datetime.datetime.now()-datetime.timedelta(hours=24)
        if(time >= thr):
             name = i +"-"+ datetime.datetime.now().strftime("%d-%m-%y")
             if(name in file):
                pass
             else:
                os.rename(f"{dir}/{i}", f"{dir}/{name}")
                print(f"\n\n\n {name}  is new file.")
         
       

dir = input("input absolute path where log rotation need to run - ")        
log_rotate(dir)
print("\n\n\n Log rotation successful")                       
