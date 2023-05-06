import pyautogui
import random
import tkinter as tk
from tkinter import ttk

class ClickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mark GIlbert Reginio")

        # Create x-coordinate label and entry field
        self.x_label = ttk.Label(master, text="X-coordinate:")
        self.x_label.pack()
        self.x_entry = ttk.Entry(master)
        self.x_entry.pack()

        # Create y-coordinate label and entry field
        self.y_label = ttk.Label(master, text="Y-coordinate:")
        self.y_label.pack()
        self.y_entry = ttk.Entry(master)
        self.y_entry.pack()

        # Create number of clicks label and entry field
        self.num_clicks_label = ttk.Label(master, text="Number of clicks:")
        self.num_clicks_label.pack()
        self.num_clicks_entry = ttk.Entry(master)
        self.num_clicks_entry.pack()

        # Create sleep time label and entry field
        self.sleep_time_label = ttk.Label(master, text="Sleep time (ms):")
        self.sleep_time_label.pack()
        self.sleep_time_entry = ttk.Entry(master)
        self.sleep_time_entry.pack()

        # Create randomized interval checkbox
        self.randomize_interval_var = tk.BooleanVar()
        self.randomize_interval_checkbox = ttk.Checkbutton(master, text="Randomize interval", variable=self.randomize_interval_var)
        self.randomize_interval_checkbox.pack()

        # Create run button
        self.run_button = ttk.Button(master, text="Run", command=self.run_clicks)
        self.run_button.pack()

    def run_clicks(self):
        # Get x and y coordinates from entry fields
        x = int(self.x_entry.get())
        y = int(self.y_entry.get())

        # Get number of clicks from entry field
        num_clicks = int(self.num_clicks_entry.get())

        # Get sleep time from entry field
        sleep_time = int(self.sleep_time_entry.get())

        # Determine if interval should be randomized
        if self.randomize_interval_var.get():
            # Generate random interval between 0.5 and 1.5 times the specified sleep time
            min_interval = int(0.5 * sleep_time)
            max_interval = int(1.5 * sleep_time)
            interval = random.randint(min_interval, max_interval)
        else:
            interval = sleep_time

        # Click the specified coordinates the specified number of times
        for i in range(num_clicks):
            pyautogui.click(x=x, y=y)
            if i < num_clicks - 1:
                # Sleep for the specified interval (with optional randomization)
                time.sleep(interval / 1000)
    
def main():
    root = tk.Tk()
    clicker_gui = ClickerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
