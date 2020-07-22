import tkinter as tk
from tkinter import font

from playsound import playsound

from programme_directory import test_programme, upper_programme


class Programme:
    def __init__(self, parent, stations, n_circuits):
        # base stuff
        self.parent = parent
        self.huge_font = font.Font(self.parent, size=120)
        self.big_font = font.Font(self.parent, size=80)
        self.small_font = font.Font(self.parent, size=40)
        self.programme = stations * n_circuits
        # labels
        self.title_label = tk.Label(parent)
        self.title_label.config(font=self.big_font)
        self.title_label.pack(fill=tk.BOTH, expand=1)
        self.details_label = tk.Label(parent)
        self.details_label.config(font=self.small_font)
        self.details_label.pack(fill=tk.BOTH, expand=1)
        self.countdown_label = tk.Label(parent)
        self.countdown_label.config(font=self.huge_font)
        self.countdown_label.pack(fill=tk.BOTH, expand=1)
        # start the timer
        self.parent.after(0, self.display_station, 0)

    def countdown(self, count, function, *args):
        # change text in label
        self.countdown_label.configure(text=count)
        if count > 0:
            root.after(1000, self.countdown, count - 1, function, *args)
        else:
            playsound('whistle.wav', block=False)
            root.after(0, function, *args)

    def display_station(self, n):
        self.title_label.configure(text=self.programme[n]['name'], background='orange')
        self.details_label.configure(text=self.programme[n]['description'], background='orange')
        self.countdown_label.configure(background='orange')
        self.parent.after(0, self.countdown, self.programme[n]['time'], self.display_rest, n)

    def display_rest(self, n):
        if n == len(self.programme)-1:
            self.title_label.configure(text='Well Done!', background='black', foreground='white')
            self.details_label.configure(text='Your workout is complete', background='white', foreground='black')
            self.countdown_label.configure(text='', background='black', foreground='white')
            self.parent.after(3000, self.parent.destroy)
        else:
            self.title_label.configure(text='Rest', background='lightblue')
            self.details_label.configure(text=f'Next station: {self.programme[n + 1]["name"]}', background='lightblue')
            self.countdown_label.configure(background='lightblue')
            self.parent.after(0, self.countdown, self.programme[n]['rest_time'], self.display_station, n+1)


if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
#    p = Programme(root, upper_programme, 3)
    p = Programme(root, test_programme, 2)
    root.mainloop()
