import os
import time 
import shutil

def clear_folders(fullpath, days=7):  
    SECONDS_IN_DAY  = 86400
    
    os.chdir(os.path.join(os.getcwd(),fullpath))
    list_of_files = os.listdir()
    current_time = time.time()
    
    print(current_time)
    
    for i in list_of_files: 
        file_location= os.path.join(os.getcwd(),fullpath)
        file_time = os.stat(file_location).st_mtime
        
        if file_time < current_time - SECONDS_IN_DAY * days: 
            print(f"Deleting: {i}...")
            
            if os.path.isfile(file_location):
                os.remove(file_location)
                
            elif os.path.isdir(file_location):
                shutil.rmtree(file_location)
                

    