import tkinter as tk

window = tk.Tk()
frame_overview = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

frame_overview.grid(row=0, column=0)
label = tk.Label(master=frame_overview, text="Portfolio")
label.grid(row=0, column=0)
label_2 = tk.Label(master=frame_overview, text="Live Result")
label_2.grid(row=1, column=1)

frame_chart = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_chart.grid(row=0, column=1)
label3 = tk.Button(master=frame_chart, text="Chart")
label3.grid(row=0, column=0)

window.mainloop()
