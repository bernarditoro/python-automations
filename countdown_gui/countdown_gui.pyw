import tkinter as tk

from datetime import datetime

        
class Countdown(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Countdown")

        self.fr_main = tk.Frame()
        self.fr_main.pack(pady=5)

        self.btn_frame = tk.Frame()
        self.btn_frame.pack(pady=5)

        time_to_leave = self.time_to_leave()

        self.lbl_main_label = tk.Label(master=self.fr_main, text=f"You have {time_to_leave} until you have to leave!")
        self.lbl_main_label.pack(pady=10, padx=10)

        self.btn_close = tk.Button(master=self.btn_frame, text="Close", bg="#ebebeb", fg="#1f1f1f", padx=10, command=self.destroy)
        self.btn_close.pack()

        self.lbl_main_label.after(1000, self.update_main_label)

    def update_main_label(self):
        """Update the label every second"""

        time_to_leave = self.time_to_leave()

        self.lbl_main_label.configure(text=f"You have {time_to_leave} until you have to leave!")

        self.lbl_main_label.after(1000, self.update_main_label)

    @staticmethod
    def time_to_leave():
        departure = datetime(2024, 9, 2)

        now = datetime.now()

        time_difference = departure - now
    
        mm, ss = divmod(time_difference.seconds, 60)
        hh, mm = divmod(mm, 60)

        s = "%d hours, %02d minutes and %02d seconds" % (hh, mm, ss)

        if time_difference.days:
            def plural(n):
                return n, abs(n) != 1 and "s" or ""
            s = ("%d day%s, " % plural(time_difference.days)) + s

        return s
        

if __name__ == '__main__':
    countdown = Countdown()
    countdown.mainloop()
