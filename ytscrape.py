from os import link
from turtle import title
from pytube import YouTube
from pytube import Playlist
from tkinter import *
import tkinter.scrolledtext as st
from tkinter import messagebox
import os
from tkinter import filedialog

window=Tk()
window.title('YT Downloader')
w_height = 250
w_width = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen_x = (screen_width/2) - (w_width/2)
screen_y = (screen_height/2) - (w_height/2)
window.geometry('%dx%d+%d+%d' % (w_width , w_height, screen_x, screen_y))
canvas = Canvas(window, width=w_width,height=w_height, bg="#ff6961")
canvas.pack(fill="both", expand=True)

e = Entry(canvas, width=50)
e.pack(pady=10)

def click():
    file_path = filedialog.askdirectory()
    link = e.get()
    if link == '':
        messagebox.showerror('Error', 'Please try again!')
    else:
        yt = YouTube(link)
        text_area = st.ScrolledText(canvas,width = 40,fg='#582308', bg="#f5b98c", height = 8, font = ("Bookman Old Style",8))
        text_area.pack(pady=2)
        text_area.insert(INSERT,yt.title+"\n")
        text_area.configure(state ='disabled')
        output = yt.streams.get_audio_only().download(file_path)
        base, ext = os.path.splitext(output)
        new_file = base + '.mp3'
        os.rename(output, new_file)
        messagebox.showinfo("Success", "The file is ready")
def pl():
    file_path = filedialog.askdirectory()
    link = e.get()
    if link == '':
        messagebox.showerror('Error', 'Please enter a valid url!')
    else:
        playlist = Playlist(link)
        # Loop through all videos in the playlist and download them
        mypl = ""
        for video in playlist.videos:
            video_name = video.title
            mypl+=str(video_name+'\n')
            output = video.streams.get_audio_only().download(file_path)
            base, ext = os.path.splitext(output)
            new_file = base + '.mp3'
            os.rename(output, new_file)

        text_area = st.ScrolledText(canvas,width = 40,fg='#582308', bg="#f5b98c", height = 8, font = ("Bookman Old Style",8))
        text_area.pack()
        text_area.insert(INSERT,f"Number of videos: {len(playlist.video_urls)}\n{mypl}")
        text_area.configure(state ='disabled')
        messagebox.showinfo("Success", "The file is ready")
        

button = Button(canvas, text="Single Track", width=42, command=click)
button.pack(pady=2)
button2 = Button(canvas, text="Playlist", width=42, command=pl)
button2.pack(pady=2)

window.mainloop()


# url = str(input("Youtube video url :"))
# youtube = YouTube(url)
# youtube.streams.first().download()

