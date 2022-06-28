import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor
import UIControls as event_handlers

window = tk.Tk()
window.title("Screenshot Sorter")
window["background"]="#96B0FF"
window.geometry("700x400+700+200")
frm_centre_top = tk.Frame(pady=30)
frm_centre_top["background"]="#96B0FF"
frm_centre_mid = tk.Frame(pady=30)
frm_centre_mid["background"]="#96B0FF"
frm_centre_lower = tk.Frame(pady=10)
frm_centre_lower["background"]="#96B0FF"
frm_centre_bottom = tk.Frame(pady=20)
frm_centre_bottom["background"]="#96B0FF"
lbl_title = ttk.Label(master=frm_centre_top, text=event_handlers.title_text)
lbl_title["background"]="#96B0FF"
lbl_subtitle = ttk.Label(master=frm_centre_mid, text=event_handlers.subtitle_text)
lbl_subtitle["background"]="#96B0FF"
textvar = tk.StringVar(window, value=event_handlers.directory_default)
entry_file_dir = ttk.Entry(master=frm_centre_lower, width=50, textvariable=textvar)
lbl_filedir_instructions = ttk.Label(master=frm_centre_lower, text=event_handlers.instructions_text)
lbl_filedir_instructions["background"]="#96B0FF"
btn_start = ttk.Button(master=frm_centre_bottom, text="Sort")
btn_safe = ttk.Button(master=frm_centre_bottom, text="Safe Sort")
btn_close = ttk.Button(master=frm_centre_bottom, text="Quit")

lbl_title.pack(), lbl_subtitle.pack(), frm_centre_top.pack(), frm_centre_mid.pack()
entry_file_dir.pack(), lbl_filedir_instructions.pack(), frm_centre_lower.pack()
btn_start.pack(), btn_safe.pack(), btn_close.pack(), frm_centre_bottom.pack()

"""Lamda function: used because the bind function doesn't expect a function to be
called, it just wants a function. I've written a lambda function which the bind calls
allowing me to pass arguments to the actual event handler"""
btn_close.bind("<Button-1>", lambda event: event_handlers.quit_program(event, window))
btn_start.bind("<Button-1>", lambda event: event_handlers.submit_directory(event, entry_file_dir))
btn_safe.bind("<Button-1>", lambda event: event_handlers.submit_safe(event, entry_file_dir))
window.mainloop()
