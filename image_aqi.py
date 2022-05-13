from tkinter import  *
FONT_NAME="Courier"
PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"

# To show the data table for air quality index
def aqi_table():
    window=Tk()
    window.config(padx=80,pady=40)

    canvas=Canvas(width=300,height=300,highlightthickness=0)
    tomato_img=PhotoImage(file="(AQI) Values.png")
    canvas.create_image(180,150,image=tomato_img)
    canvas.grid(row=0,column=1)

    window.mainloop()