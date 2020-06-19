import PySimpleGUI as sg
from PIL import Image
import os

layout = [[sg.Text('It will compress one file in different sizes save in same folder.')], 
    [sg.Text('locate Image File', size=(19, 1)), sg.Input(size=(20,1),key='file'), sg.FileBrowse()],
    [sg.Text('Destination folder', size=(19, 1)), sg.Input(size=(20,1),key='dest'), sg.FolderBrowse()],
            [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

try:
    os.mkdir(os.getcwd()+'\\output')
except:
    pass

def convert_quality(path,dest,quality=70,grayscale=False):
    foo = Image.open(path)
    if grayscale == True:
        foo = foo.convert('L')
    x = int(foo.size[0]*(quality/100))
    y = int(foo.size[1]*(quality/100))
    foo = foo.resize((x,y),Image.ANTIALIAS)
    foo.save(dest,optimize=True,quality=quality)




window = sg.Window('Image multiple compresseer', layout, default_element_size=(80, 1), grab_anywhere=False)
event, values = window.read()
window.close()
if event == 'Submit':
    pass
else:
    exit(0)


for i in range(5,100):
    fil = values['file']
    dest = values['dest']
    dest = dest+"/"+str(i)+".png"
    convert_quality(fil,dest,i)