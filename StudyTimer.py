import tkinter as tk
from PIL import Image, ImageTk
import datetime as dt


root = tk.Tk()


#Canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=3)

#buttton
start_text = tk.StringVar()
start_btn = tk.Button(root, command=lambda:start_clock(), textvariable=start_text, background="#00cc00", height=2, width=14)
start_text.set("Start Timer!")
start_btn.grid(column=1, row= 2)

def start_clock():
    global start_time
    start_time = dt.datetime.now()
    # start_text.set("End Timer!")
    start_btn.destroy()
    end_text = tk.StringVar()
    end_btn = tk.Button(root, command=lambda:end_clock(), textvariable=end_text, background="#ff0000", height=2, width=14)
    end_text.set("Stop Timer")
    end_btn.grid(column=1, row= 2)
    
def end_clock():
    end_time = dt.datetime.now()
    time_dif = str(end_time - start_time)
    hours = int(time_dif[0])
    minutes = int(time_dif[2:4])
    result_time = f"{hours}h {round(minutes/60, 2)}min \n Enter this directly into Excel study chart!"
    print(minutes)

    #result lable
    result = tk.Label(root, text=f"Your study time: {result_time}", font=("Raleway", 14))
    result.grid(columnspan=3, column= 0, row= 1)


root.mainloop()