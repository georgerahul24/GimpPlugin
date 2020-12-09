

from gimpfu import *

def pencildrawing(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    l=image.layers
    layer_copy = pdb.gimp_layer_copy(l[0],False)
    pdb.gimp_image_insert_layer(image, layer_copy,None,1)
    l=image.layers
    layer_copy = pdb.gimp_layer_copy(l[1],False)
    pdb.gimp_image_insert_layer(image, layer_copy,None,2)
    l=image.layers
    pdb.gimp_layer_set_mode(l[1],16)
    pdb.gimp_layer_set_mode(l[0],38)
       
    pdb.gimp_hue_saturation(l[0],0,0,0, -100)


    pdb.gimp_invert(l[1])
    pdb.plug_in_gauss(image,l[1], 15,15, 0.1)

    layer = pdb.gimp_image_merge_visible_layers(image, 0)

    l=image.layers
    pdb.plug_in_gauss(image,l[0], 1,1, 0.1)
    
    pdb.gimp_image_undo_group_end(image)
    
    

register(
    "python-fu-pencildrawing",
    "Pencil colour Effect",
    "Makes your image into pencil coloured drawings",
    "GR", "GR", "2020",
    "pencildrawing",
    "*", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    pencildrawing, menu="<Image>/Filters")  # second item is menu location

main()
