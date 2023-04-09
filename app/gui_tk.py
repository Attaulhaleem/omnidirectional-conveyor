from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
# root.state("zoomed")
main_frame = ttk.Frame(root, padding=10)

title_frame = ttk.Frame(main_frame, borderwidth=5, relief="ridge")

title_image = Image.open("app/assets/hexagons1.png")
title_image = title_image.resize((120, 120))
title_image = ImageTk.PhotoImage(title_image, palette="#ff49a4")

title_image_label = ttk.Label(title_frame, anchor="w", image=title_image)

title_text_label = ttk.Label(
    title_frame,
    text="OmniVeyor GUI",
    font=("TkHeadingFont", 30),
    anchor="center",
)

subtitle_label = ttk.Label(
    title_frame,
    text="Atta ul Haleem\tInshal Khan\tMustafa Ansari\tShaheer Ahmed",
    font=("TkMenuFont", 10),
    anchor="center",
)


main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
title_frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
title_image_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
title_text_label.grid(column=1, row=0, sticky=(N, S, E, W))
subtitle_label.grid(column=1, row=1, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)

# content.grid(column=0, row=0, sticky=(N, S, E, W))
# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

root.mainloop()


# root = Tk()
# content = ttk.Frame(root, padding=10)
# frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)

# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()

# onevar.set(True)
# twovar.set(False)
# threevar.set(True)

# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")

# content.grid(column=0, row=0, sticky=(N, S, E, W))
# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# content.columnconfigure(0, weight=3)
# content.columnconfigure(1, weight=3)
# content.columnconfigure(2, weight=3)
# content.columnconfigure(3, weight=1)
# content.columnconfigure(4, weight=1)
# content.rowconfigure(1, weight=1)

# root.mainloop()
