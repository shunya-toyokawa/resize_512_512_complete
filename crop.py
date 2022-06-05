from PIL import Image
import numpy as np
import pandas as pd


zahyou = pd.read_csv("detection_Result.csv",header=None)
print(zahyou)

x= int(zahyou[2].values)
y= int(zahyou[3].values)
width= int(zahyou[4].values)
height= int(zahyou[5].values)

img = Image.open("test.jpg")
#output = img.crop((x,y,x+width,y+height))
print(width,height)

w,h=img.size
print(width/w)

center_x= x+width*0.5
center_y=y+height*0.5

#output = img.crop((center_x - (((height*3)/4)/2) ,y,center_x + (((height*3)/4)/2) ,y+height))
output = img.crop((center_x - (height/2) ,y, center_x + (height/2) ,y+height))

output.save("out_crop.png")

