import mouse
import time
import os
import subprocess

#consider a start recording trigger (middle button) and a start to run the program (a little gui)

def program_writer(record):
    print(record)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "Automator.py")
    with open(file_path, "w") as f:
        f.write("import mouse" + "\n")
        f.write("import time" + "\n")
        i = 0
        for item in record:
            coord = str(record[i][1])    
            delimiters = "()"
            for delimiter in delimiters:
                coord = coord.replace(delimiter, "")
            f.write("mouse.move(" + coord + ", absolute=True, duration=1)" + "\n" )
            f.write("mouse.click('" + str(record[i][0]) + "') \n")
            i += 1   
    subprocess.run([r"C:\Users\bradl\AppData\Local\Microsoft\WindowsApps\python.exe", 
                    "C:/Users/bradl/Desktop/Automator.py"])
    
def main():
    record_raw = []
    global record_filtered 
    record_filtered = []
    while not mouse.is_pressed(button='middle'):
        x = str(mouse.get_position())
        if mouse.is_pressed(button='left'):
            print("left, " + x)
            record_raw.append(["left", x])
        if mouse.is_pressed(button='right'):
            print("right, " + x)
            record_raw.append(["right", x])
        else:
            time.sleep(0.01)
        for item in record_raw:
            if item not in record_filtered:
                record_filtered.append(item)
        time.sleep(0.01)
    program_writer(record_filtered)

main()
