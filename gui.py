import tkinter as tk
import tkinter.font as tkFont
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

class GUI:
    def __init__(self, on_ocr, on_go):
        self.__root = tk.Tk()
        self.__root.title('screenshot translator')
        self.__root.configure(background='#222222')
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)
        self.__root.resizable(False, False)
        tkFont.nametofont('TkDefaultFont').configure(size=20, family='Consolas')
        
        def on_focus(event):
            if event.widget == self.__root:
                on_ocr()
        self.__root.bind("<FocusIn>", on_focus)
                
        
        self.__btn_ocr = tk.Button(
            background='#222222', 
            activebackground='#333333',
            foreground='#ffffff',
            activeforeground='#ffffff',
            text='OCR',
            border=10,
            borderwidth=4,  
            highlightthickness=4,
            highlightcolor='#dddddd',
            highlightbackground='#dddddd',
            command=on_ocr
        )
        self.__btn_ocr.grid(row=0, column=1, sticky=tk.NSEW)
        
        self.__btn_go = tk.Button(
            background='#222222', 
            activebackground='#333333',
            foreground='#ffffff',
            activeforeground='#ffffff',
            text='GO', 
            border=10,
            borderwidth=4,
            highlightthickness=4,
            highlightcolor='#dddddd',
            highlightbackground='#dddddd',
            command=on_go
        )
        self.__btn_go.grid(row=1, column=1, sticky=tk.NSEW)
        
        self.__text_input = tk.Text(
            background='#222222', 
            foreground='#ffffff',
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground='#dddddd',
            highlightcolor='#dddddd',
            insertbackground='white',
            width=50, height=4,
            spacing2=5,
            padx=10, pady=10,
            font=('Consolas', 20),
        )
        self.__text_input.grid(row=0, column=0)
        
        self.__text_result = tk.Text(
            background='#222222', 
            foreground='#ffffff',
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground='#dddddd',
            highlightcolor='#dddddd',
            width=50, height=10,
            spacing3=5,
            padx=10, pady=10,
            font=('Consolas', 20),
        )
        self.__text_result.grid(row=1, column=0)
        self.__text_result.config(state=tk.DISABLED)
        
    def start(self):
        self.__root.mainloop()
        
    def set_input(self, text):
        self.__text_input.delete('1.0', tk.END)
        self.__text_input.insert(tk.END, text)
        
    def get_input(self):
        return self.__text_input.get('1.0', tk.END)
    
    def set_result(self, text):
        self.__text_result.configure(state=tk.NORMAL)
        self.__text_result.delete('1.0', tk.END)
        self.__text_result.insert(tk.END, text)
        self.__text_result.configure(state=tk.DISABLED)
        