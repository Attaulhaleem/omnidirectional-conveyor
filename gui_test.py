from guizero import App, Text, TextBox, PushButton, Slider, Picture


def sayMyName():
    msg.value = name.value


def changeTextSize(sliderValue):
    msg.size = sliderValue


app = App(title="Hello world")
msg = Text(
    app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue"
)
name = TextBox(app)
updateText = PushButton(app, command=sayMyName, text="Display my name")
textSize = Slider(app, command=changeTextSize, start=10, end=80)
myCat = Picture(app, image="cat.gif")
app.display()
