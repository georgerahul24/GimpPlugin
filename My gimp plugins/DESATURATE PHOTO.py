'''Created by George Rahul '''
from gimpfu import *

def DESATURATEPHOTO(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    # function code goes here...
    pdb.gimp_message("eXTREME UNMASK STARTEDWITH DESATURATION")
    pdb.plug_in_unsharp_mask(image, drawable, 6,5,0.119)
    pdb.gimp_desaturate_full(drawable,0)
    
    #pdb.plug_in_gauss(image, drawable, 2, 2,1)
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-CONVERT-TO-BLACK-AND-WHITE",
    "GR",
    "unsharp mask and desaturate",
    "GR", "GR", "2020",
    "DESATURATE PHOTO",
    "RGB", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    DESATURATEPHOTO, menu="<Image>/Filters")  # second item is menu location

main()
#RADIUS 6.22 AMT 5 THRESH 0.119
