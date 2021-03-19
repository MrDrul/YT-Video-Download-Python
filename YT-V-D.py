#%%
# importing the module  
from pytube import YouTube
from moviepy.editor import * 
import os
import eel
import time

eel.init("web")



@eel.expose
def yes_voch(URL, Download, Type):
    
    mp4 = set(["mp4"])
    mp3 = set(["mp3"])
    both = set(["b"])
    Downloads = set(["d", "D", "downlads" "Downloads"])
    Desktop = set(["", "desktop", "Desktop"])


    reply_Download_path = str(Download)
    if reply_Download_path in Downloads:
      Download = r"/home/n0k1a/Downloads"

    elif reply_Download_path in Desktop:
      Download = r"/home/n0k1a/Desktop"


    else:
      print("Please enter normal ban debil")
      exit()
      


    reply = str(Type).lower().strip()
    if reply in both:
           time.sleep(5)
           yt = YouTube(URL).streams.first().download(Download)
           
           #global mp4_file, mp3_file, videoclip, audioclip

           mp4_file = r"/home/n0k1a/Desktop/Michael Jackson - Billie Jean (Official Video).mp4"#yt.title().replace("Mp4", "mp4") 

           mp3_file = r"/home/n0k1a/Desktop/Michael Jackson - Billie Jean (Official Video).mp4"#yt.title().replace("Mp4", "mp3")
            
           videoclip = VideoFileClip(mp4_file)

           audioclip = videoclip.audio
           audioclip.write_audiofile(mp3_file)

           audioclip.close()
           videoclip.close()
           print("Video Name" + " " + yt.title())
           

    elif reply in mp4:
            yt = YouTube(URL).streams.first().download(Download)
            print("All Done Boodbye :)")
            print("Video Name" + " " + yt.title())
            
    elif reply in mp3:
           yt = YouTube(URL).streams.first().download(Download)

           mp4_file = yt.title().replace("Mp4", "mp4") 

           mp3_file = yt.title().replace("Mp4", "mp3")
            
           videoclip = VideoFileClip(mp4_file)

           audioclip = videoclip.audio
           audioclip.write_audiofile(mp3_file)

           audioclip.close()
           videoclip.close()

           os.remove(yt.title().replace("Mp4", "mp4"))
           print("Video Name" + " " + yt.title())

    else:
      print("Ops something went wrong please try again")
      return yes_voch(URL, Download, Type)

            


eel.start("Main.html", size = (500 , 350), port = (6768), mode = ('chrome'))
# %%
