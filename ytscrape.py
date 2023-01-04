import tkinter as tk
import tkinter.ttk as ttk
import pytube
from tkinter import filedialog, messagebox
import re

# Global variable to store the destination directory
destination = ''

# Global list to store the titles of the downloaded MP3 files
titles = []

def choose_destination():
    # Open a file dialog to choose the destination directory
    global destination
    destination = filedialog.askdirectory()
    # Update the label to show the chosen destination
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination)

def download_mp3():
    # Get the YouTube URL from the entry widget
    url = url_entry.get()
    try:
        # Create a YouTube object using the URL
        youtube = pytube.YouTube(url)
        # Get the first audio stream
        audio_stream = youtube.streams.filter(only_audio=True).first()
        # Get the title of the video
        title = youtube.title
        # Specify the file name and extension as the title with a .mp3 extension
        file_name = re.sub(r'[\\/*?:"<>|]', '', title) + '.mp3'
        # Download the audio stream to the specified destination directory with the specified file name
        audio_stream.download(destination, filename=file_name)
        # Add the title to the list of titles
        titles.append(title)
        # Update the textarea with the list of titles
        textarea.delete(1.0, tk.END)
        textarea.insert(tk.END, '\n'.join(titles))
    except pytube.exceptions.RegexMatchError:
        # Display an error message if the YouTube URL is invalid
        messagebox.showerror('Error', 'Invalid YouTube URL')
    except Exception as e:
        # Display an error message if any other exception occurs
        messagebox.showerror('Error', str(e))


def download_mp4():
    # Get the YouTube URL from the entry widget
    url = url_entry.get()
    try:
        # Create a YouTube object using the URL
        youtube = pytube.YouTube(url)
        # Get the first video stream
        video_stream = youtube.streams.get_highest_resolution()
        # Download the video stream to the specified destination directory
        video_stream.download(destination)
        # Get the title of the video
        title = youtube.title
        # Add the title to the list of titles
        titles.append(title)
        # Update the textarea with the list of titles
        textarea.delete(1.0, tk.END)
        textarea.insert(tk.END, '\n'.join(titles))
    except pytube.exceptions.RegexMatchError:
        # Display an error message if the YouTube URL is invalid
        messagebox.showerror('Error', 'Invalid YouTube URL')
    except Exception as e:
        # Display an error message if any other exception occurs
        messagebox.showerror('Error', str(e))

# Create the main window
root = tk.Tk()
root.title('YouTube Downloader')
root.resizable(False, False)
root.configure(bg='#ff6961')

# Create a style to use for the widgets
style = ttk.Style(root)
style.configure('TFrame', background='white')
style.configure('TLabel', font=('Century Gothic', 11), foreground='black', background='#ffffff')
style.configure('TButton', font=('Century Gothic', 11), foreground='black', background='#ff6961')
style.configure('TEntry', font=('Century Gothic', 11), foreground='black', background='#ff6961')
style.configure('TText', font=('Century Gothic', 11), foreground='black', background='#ff6961')

# Create a label and an entry widget to enter the YouTube URL
url_label = ttk.Label(root, text=' YouTube URL:', style='TLabel', width=18)
url_entry = ttk.Entry(root, font=('Century Gothic', 12), foreground='black', background='#ffffff', width=25)

# Create a button to choose the destination directory
destination_button = ttk.Button(root, text='Choose Destination', command=choose_destination, style='TButton', width=18)

# Create an entry widget to show the chosen destination directory
destination_entry = ttk.Entry(root, font=('Century Gothic', 12), foreground='black', background='#ffffff', width=25)

# Create a button to initiate the download
download_button = ttk.Button(root, text='Download MP3', command=download_mp3, style='TButton', width=23)
download_button_mp4 = ttk.Button(root, text='Download MP4', command=download_mp4, style='TButton', width=23)

# Create a textarea to display the titles of the downloaded MP3 files
textarea = tk.Text(root, height=10, width=50, bg='white', fg='red')

# Place the widgets in the window using the grid layout
url_label.grid(row=0, column=0, padx=10, pady=10, sticky='NESW')
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky='NESW')
destination_button.grid(row=1, column=0, padx=9, pady=10, sticky='NESW')
destination_entry.grid(row=1, column=1, padx=10, pady=10, sticky='NESW')
download_button.grid(row=3, column=0, padx=10, pady=10, sticky='W', columnspan=2)
download_button_mp4.grid(row=3, column=0, padx=10, pady=10, sticky='E', columnspan=2)
textarea.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()

