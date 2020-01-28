
import pytube
link = https://youtu.be/YgcMPP6-uqc
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()