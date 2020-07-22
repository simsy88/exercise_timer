import tkinter as tk


class Programme:
    def __init__(self, parent, stations, n_circuits):
        # labels
        self.parent = parent
        self.title_label = tk.Label(parent)
        self.title_label.pack()
        self.details_label = tk.Label(parent)
        self.details_label.pack()
        self.countdown_label = tk.Label(parent)
        self.countdown_label.pack()
        self.programme = stations*n_circuits
        # start the timer
        self.parent.after(0, self.display_station, 0)

    def countdown(self, count, function, *args):
        # change text in label
        self.countdown_label.configure(text=count)
        if count > 0:
            root.after(1000, self.countdown, count - 1, function, *args)
        else:
            root.after(0, function, *args)

    def display_station(self, n):
        self.title_label.configure(text=self.programme[n]['name'])
        self.details_label.configure(text=self.programme[n]['description'])
        self.parent.after(0, self.countdown, self.programme[n]['time'], self.display_rest, n)

    def display_rest(self, n):
        if n == len(self.programme)-1:
            self.title_label.configure(text='Well Done!')
            self.details_label.configure(text='Your workout is complete')
            self.countdown_label.configure(text='')
            self.parent.after(5000, self.parent.destroy)
        else:
            self.title_label.configure(text='Rest')
            self.details_label.configure(text=f'Next station: {self.programme[n + 1]["name"]}')
            self.parent.after(0, self.countdown, self.programme[n]['rest_time'], self.display_station, n+1)


test_programme = [{'name': 'test1', 'description': 'testA', 'time': 3, 'rest_time': 2},
                  {'name': 'test2', 'description': 'testB', 'time': 5, 'rest_time': 10}]

if __name__ == "__main__":
    root = tk.Tk()
    p = Programme(root, test_programme, 2)
    root.mainloop()
