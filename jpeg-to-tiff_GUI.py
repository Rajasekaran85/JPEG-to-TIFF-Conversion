import sys
import os
from tkinter import filedialog
from tkinter import *
from PIL import Image
import re

# pillow library used
# tkinter library used


def browse_button():
    # user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)


    
def conv():
    print("\n JPEG to TIFF Conversion\n")
    print("\n Date: 25 April 2023 \n\n")

    directory = "TIFF"
    output = filename + "/" + directory
    if os.path.exists(output):
        pass
    else:
        os.mkdir(output)

    f1 = os.listdir(filename) 
    for fname in os.listdir(filename):
        if not fname.endswith(".jpg"):
            continue
        test = os.path.splitext(fname)[0]
        value1 = filename + '/' + fname

        # open the jpeg image
        image = Image.open(value1)

        # define tiff file name as same jpg image name
        name1 = output + '/' + test + ".tif"
        print(name1)

        # get the jpeg image resolution value
        img_dpi = str(image.info['dpi'])
        patn = re.sub(r"[\(\)]", "", img_dpi)
        sp = patn.split(",")[0]
        dpi_val = round(float(sp))  

        # convert to tiff image, resolution value assigned from jpeg image
        image.save(name1, 'tiff', dpi=(dpi_val,dpi_val))

        # The converted tiff image version is lower, so change the tiff version to 6.0 by using the below commands.
        image1 = Image.open(name1)
        image1.tag[33432] = " "
        image1.save(name1, tiffinfo=image1.tag)

    messagebox.showinfo("JPEG to TIFF", "Completed")
    
root = Tk()
root.geometry("400x350")
root.title("JPEG to TIFF Converter")
root.config(bg='#5CB5FA') 

img = "jpeg2tiff-logo.png"
logo = PhotoImage(file=img)
label1 = Label(root, image = logo) 
label1.pack(pady=20)

folder_path = StringVar()
lbl1 = Label(root, text='JPEG to TIFF Conversion', font='helvetica 15', bg='#5CB5FA')
lbl1.pack(pady=10)
button2 = Button(text="Browse", command=browse_button, bg='royalblue', fg = 'white').pack(pady=25)
button3 = Button(text="Submit", command=conv, bg='royalblue', fg = 'white').pack(pady=25)
lbl2 = Label(root, textvariable=folder_path, font='helvetica 12', bg='#5CB5FA')
lbl2.pack(pady=10)

mainloop()

