from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import  messagebox
from tkinter.ttk import Combobox
from pytube import YouTube
window = Tk()
window.title("YTdownloader")
window.geometry("400x400")

# Def for browse window

def browse():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_file.set(directory)
# Def for download video
    
def download():
    try:
        video_url = entry_url.get()
        save_dir = download_file.get()
        res_video = res_combo.get()
        yt = YouTube(video_url)
        yt.streams.filter(res=res_video).first().download(save_dir)
        messagebox.showinfo("Download","Download Completly")
    except:
        messagebox.showerror("Error","Error to download video")
    
    

# Label for link from video
label_url = Label(window,text="Video link:",fg="green",font=(5))
label_url.place(x=0,y=30)
# Entry for input url

entry_url = Entry(window,width=40)
entry_url.place(x=110,y=35)

# Label resolusions 
label_res = Label(window,text="Resolution :",fg="green",font=(5))
label_res.place(x=0,y=110)

# combocox for resolution
resolustions = ["144p","240p","360p","480p","720p","1080p"]
res_combo = Combobox(window,values=resolustions,width=40)
res_combo.place(x=115,y=115)

# label for save video

label_save = Label(window,text="Save to :",fg="green",font=(5))
label_save.place(x=0,y=200)

# Entry for Save video
download_file = StringVar()
entry_save = Entry(window,width=30,textvariable=download_file)
entry_save.place(x=110,y=205)

# Button for open window to save video
btn_open = Button(window,text="Open",width=10,bg="green",command=browse)
btn_open.place(x=310,y=203)
# Button for Download video
btn_download = Button(window,text="Download",width=15,height=3,command=download)
btn_download.place(x=155,y=300)

window.mainloop()