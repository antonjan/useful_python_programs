import pyttsx3, tkinter as tk
def on_click():
    engine = pyttsx3.init()
    engine.say(En.get())
    engine.runAndWait()
window = tk.Tk()
window.geometry("500x200")
Text = tk.Label(window, text="Type Here!")
Text.pack(padx=10, pady=10)
En = tk.Entry()
En.pack(padx=10, pady=10)
Say = tk.Button(text="CLICK ME!", command=on_click)
Say.pack(padx=10, pady=10)
window.mainloop()
