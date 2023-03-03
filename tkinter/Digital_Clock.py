import tkinter as ui
import time

window = ui.Tk()
def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    milliseconds = str(int(round(time.time() * 1000)))[-3:]
    am_pm =time.strftime("%p")  
    time_text = hours + ":" + minutes + ":" + seconds + "." + milliseconds + " " + am_pm
    digital_clock_label.config(text = time_text)
    digital_clock_label.after(1000, update_clock)
    
digital_clock_label = ui.Label(window,text = "00:00:00:000", font ="Helvetica 72 bold")
digital_clock_label.pack()

update_clock()
window.mainloop()