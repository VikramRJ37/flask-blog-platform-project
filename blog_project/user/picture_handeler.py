import os
from PIL import Image
from flask import current_app
def add_profile_pic(pic_upload,username):
    filename=pic_upload.filename
    exttype=filename.split('.')[-1]
    storage_filename=str(username)+'.'+exttype

    filepath=os.path.join(current_app.root_path,'static/profile_pics',storage_filename)
    opsize=(200,200)
    pic=Image.open(pic_upload)
    pic.thumbnail(opsize)
    pic.save(filepath)
    return storage_filename