import tkinter
import customtkinter
from pytube import YouTube

# Function to download youtube videos
def StartDownload():
    try:
        YtLink = link.get()
        YtObject = YouTube(YtLink)
        video = YtObject.streams.get_highest_resolution()
        video.download()
    except:
        FinishLabel.configure(text="Download Error", text_color= "red")
    FinishLabel.configure(text="Downloaded!")

# System setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
Title = customtkinter.CTkLabel(app, text= "Insert a youtube link", font= ("Arial",14))
Title.pack(padx= 10, pady= 10)

# Link input
urlVar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height= 40, textvariable=urlVar)
link.pack()

# Finished downloading
FinishLabel = customtkinter.CTkLabel(app, text="")
FinishLabel.pack()

# Download button
download = customtkinter.CTkButton(app, text= "Download", command=StartDownload)
download.pack(padx=10, pady= 10)

# Run the app
app.mainloop()
