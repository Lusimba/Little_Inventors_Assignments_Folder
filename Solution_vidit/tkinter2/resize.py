from PIL import Image
file_in = '/Users/ved/Desktop/python/Little_Inventors_Assignments_Folder/Solution_vidit/tkinter2/pictures_for_coding/Shardstone.png'
pil_image = Image.open(file_in)
print("image.size   = (%d, %d)" % pil_image.size)
print("image.format = %s" % pil_image.format)  # 'JPEG'
print("image.mode   = %s" % pil_image.mode)    # 'RGB'
file_out = 'Shardstone200x100.png'
image200x100 = pil_image.resize((200, 100), Image.ANTIALIAS)
image200x100.save(file_out)
print("File saved as %s" % file_out)
import tkinter as tk
from PIL import ImageTk
root = tk.Tk()
root.title(file_in)
tk_image1 = ImageTk.PhotoImage(pil_image)
tk_image2 = ImageTk.PhotoImage(image200x100)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)
root.mainloop()