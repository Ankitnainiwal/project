import os
quary=input("What do you want to do ? : ")

while ("exit" not in quary) and ("stop" not in quary) and ("quit" not in quary) and ("terminate" not in quary) and ("nothing" not in quary):
    if("do not" not in quary and "don't" not in quary and "never" not in quary):
        if(("open" in quary or "run" in quary or "execute" in quary) and ("notepad" in quary or "editor" in quary or "text editor" in quary)):
            os.system("notepad "+input('Could you please specify File name with path ? : '))
            
        elif("open" in quary or "run" in quary or "execute" in quary) and ("chrome" in quary or "browser" in quary or "chrome browser" in quary):
            browser=input('Which browser? : ')
            if browser=='chrome':
                site=input("Any specific site you want to visit : ");
                
                #if .exe file exists at default directory then run it else check for possible to run through direct command
                if os.system('IF EXIST "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe". ( "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" '+site+') ELSE (chrome '+site+')')==1:print("DO NOT SUPPORT !!!!")
                
            if browser=='firefox':
                site=input("Any specific site you want to visit : ");
                if os.system('IF EXIST "C:\Program Files (x86)\Mozilla Firefox\firefox.exe". ( "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" '+site+') ELSE (firefox '+site+')')==1:print("DO NOT SUPPORT !!!!")            
                
            if browser=='internet explorer':
                site=input("Any specific site you want to visit : ");
                if os.system('"C:\Program Files\Internet Explorer\iexplore.exe" '+site)==1:print("DO NOT SUPPORT !!!!")            
                
        elif(("open" in quary or "run" in quary or "execute" in quary) and ("control panal" in quary)):
            os.system("control")
            
        elif(("open" in quary or "run" in quary or "execute" in quary) and ("photo viewer" in quary or "photos" in quary or "picasa" in quary)):
            if os.system('"C:\Program Files (x86)\Google\Picasa3\Picasa3.exe"')==1:print("DO NOT SUPPORT !!!!") 
            
        elif("open" in quary or "run" in quary or "execute" in quary) and ("explorer" in quary or "file explorer" in quary):
            os.system("explorer "+input('In which drive? : ')+":")
            
        elif(("open" in quary or "run" in quary or "execute" in quary) and ("calculator" in quary)):
            os.system("calc")
            
        elif("clear" in quary or "clean" in quary)and("screen" in quary): #to clear/clean the workspace/screen
            os.system("cls")
            
        elif("open" in quary or "run" in quary)and("vlc player" in quary or "player" in quary):
            if os.system('IF EXIST "C:\Program Files\VideoLAN\VLC\vlc.exe". ( echo me && "C:\Program Files\VideoLAN\VLC\vlc.exe") ELSE (VLC)')==1:print("DO NOT SUPPORT !!!!")
            
        elif("color" in quary and "text" in quary):
            os.system("color "+input('Enter (0-f) color value for text : '))
            
            #if user know and want to run direct command then he/she can , because sometimes command are shorter to type (like : cls)
        elif("execute" in quary or "run" in quary)and("command" in quary):
            os.system(input('Enter the command : '))
            
        else : print("DO NOT SUPPORT !!!!")
        
    quary=input('Anything more you want to do ? : ')
    