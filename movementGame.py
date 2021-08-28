import tkinter as tk
import tkinter.ttk as ttk
import random
import timeit

clicks = -1
zero_time = 0
# tkinter is so bad and I have no idea what I am doing :)


class App(ttk.Frame):
    def __init__(self, master, **kwargs):
        super(App, self).__init__(master=master, **kwargs)
        master.wm_geometry('1080x720')
        self.frame = f = tk.Frame(self, width=83, height=32, relief=tk.SUNKEN, borderwidth=1, bg='pink')
        b = ttk.Button(f, text="Click", command=self.move_frame)
        # e = ttk.Button(f, text="exit", command=self.exit_button)

        # e.place(x=-200, y=-200)
        b.place(x=2, y=2)
        f.place(x=2, y=2)

        self.label = tk.Label(self, text='Click to start', bg='pink')
        self.label.place(relx=0.4, rely=0.0, relwidth=0.2, relheight=.1)

        self.place(relheight=1.0, relwidth=1.0)
        print()

    def move_frame(self):
        # x = self.frame.winfo_x()
        y = round(random.uniform(self.winfo_height() / 10, self.winfo_height() * 9 / 10 - 16), 0)
        # y = self.frame.winfo_y()
        x = round(random.uniform(self.winfo_height() / 10, self.winfo_width() * 9 / 10 - 42), 0)
        self.frame.place(x=x)
        self.frame.place(y=y)
        update_clicks(self)

    def exit_button(self):
        print('exiting')


def update_clicks(self):
    global clicks
    global zero_time
    clicks = clicks + 1

    start = timeit.default_timer()
    end = timeit.timeit()

    if clicks < 1:
        zero_time = start-end
        # zero_time accounts for how long before first button is pressed

    if clicks != 0:
        avg = round(((start - end - zero_time) / clicks * 1000))
        change_text(self, avg)
        print(clicks, "    ", round(start - end - zero_time, 3))

    if (clicks % 10 == 0) & (clicks != 0):
        print()
        print(round(start - end - zero_time, 4), " seconds to complete ", clicks)
        # exit()


def change_text(self, avg):
    self.label['text'] = (clicks, "\navg ms: \n", avg)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
