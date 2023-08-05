import tkinter
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))
    

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("500x200")


longurl_label = tkinter.Label(root, text="Enter Long URL")
longurl_entry = tkinter.Entry(root, width=50)
space1 = tkinter.Label(root, text=" ")
shorturl_label=tkinter.Label(root, text="Output shortened URL") 
shorturl_entry = tkinter.Entry(root, width=50)
space2 = tkinter.Label(root, text=" ")
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten)

longurl_label.pack()
longurl_entry.pack()
space1.pack()
shorturl_label.pack()
shorturl_entry.pack()
space2.pack()
shorten_button.pack()

root.mainloop()