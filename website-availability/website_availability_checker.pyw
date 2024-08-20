import tkinter as tk
from tkinter import ttk

import requests

import time

from plyer import notification


class WebsiteAvailability(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Check Website Availability")

        self.lbl_title = ttk.Label(text="Enter website URL:")
        self.lbl_title.pack()

        self.url_frame = ttk.Frame()
        self.url_frame.pack(pady=10, padx=10)

        self.ent_website_url = ttk.Entry(master=self.url_frame)
        self.ent_website_url.pack()
        self.ent_website_url.insert(0, "https://")

        self.chb_variable_state = tk.IntVar(value=1) # Tracks the current state of the checkbutton. 0 for unchecked and 1 for checked
        self.chb_schedule_task = ttk.Checkbutton(master=self.url_frame, variable=self.chb_variable_state, text="Automatically check again in 5 minutes")
        self.chb_schedule_task.pack()

        self.btn_check_website = ttk.Button(text="Check Website", command=self.check_website_availability, master=self.url_frame)
        self.btn_check_website.pack()

        self.lbl_result = ttk.Label()

    def check_website_availability(self):
        if website_url:=self.ent_website_url.get():
            try:
                start_time = time.time()

                response = requests.get(website_url, timeout=1)

                end_time = time.time()

                load_time = end_time - start_time

                result_text = (f"{website_url} returned a status of {response.status_code} and had a load time of {round(load_time, 3)} seconds", True) # Return True if request is success with no errors else return False

            except requests.exceptions.MissingSchema:
                result_text = ("Invalid URL: Add 'https://' before the URL", False)

            except requests.exceptions.ConnectionError:
                # TODO: Retry the request in 10 seconds
                result_text = ("Connection refused!", False)

            except requests.exceptions.InvalidURL:
                result_text = ("Invalid URL!", False)

        else:
            result_text = ("Website URL cannot be empty!", False)

        self.lbl_result.configure(text=result_text[0], foreground="green" if result_text[1] and response.status_code == 200 else "red") # Even if the request went through, mark text as red if status code is not OK
        self.lbl_result.pack(pady=4, padx=10)

        if result_text[1]:
            notification.notify(
                title="Website Check",
                message=result_text[0],
                app_name="Website Availability"
            )

            if self.chb_variable_state.get():
                self.after(300000, self.check_website_availability)


check_availability = WebsiteAvailability()
check_availability.mainloop()
