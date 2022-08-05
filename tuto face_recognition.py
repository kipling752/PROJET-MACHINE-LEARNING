#!/usr/bin/env python
# coding: utf-8

# In[5]:


import face_recognition 

from PIL import Image,ImageDraw

img = face_recognition.load_image_file("classe.jpeg") # upload image

sp = face_recognition.face_locations(img) #detect face

# Create new image
image_pil = Image.fromarray(img)
draw = ImageDraw.Draw(image_pil)

for head in sp:
    y0, x0, y1, x1 = head
#Paint
    draw.rectangle(((x0, y0), (x1,y1)), outline=(255,255,0))
#Show new image    
image_pil.show()


# In[ ]:




