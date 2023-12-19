import tkinter
import customtkinter
from pytube import YouTube

# Function to download youtube videos
def start_Download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color= "white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error", text_color= "red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progressPercent.configure(text=per + '%')
    progressPercent.update()

    # Updating progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# System setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text= "Insert a youtube link", font= ("Arial",14))
title.pack(padx= 10, pady= 10)

# Link input
urlVar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height= 40, textvariable=urlVar)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Percentage
progressPercent = customtkinter.CTkLabel(app, text="0%")
progressPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx= 10, pady= 10)

# Download button
download = customtkinter.CTkButton(app, text= "Download", command=start_Download)
download.pack(padx=10, pady= 10)

# Run the app
app.mainloop()
