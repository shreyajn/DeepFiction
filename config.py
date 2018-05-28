#sj2842
#all paths must be changed before attempting to try any testing 
"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = True

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = '/Users/shreyajain/storyteller/'
paths['sktables'] = '/Users/shreyajain/storyteller/'

# Decoder
paths['decmodel'] = '/Users/shreyajain/storyteller/romance.npz'
paths['dictionary'] = '/Users/shreyajain/storyteller/romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = '/Users/shreyajain/storyteller/coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = '/Users/shreyajain/storyteller/vgg19.pkl'
paths['pycaffe'] = 'Users/shreyajain/storyteller/caffe/python'
paths['vgg_proto_caffe'] = '/Users/shreyajain/storyteller/VGG_ILSVRC_19_layers_deploy.prototxt'
paths['vgg_model_caffe'] = '/Users/shreyajain/storyteller/VGG_ILSVRC_19_layers.caffemodel'


# COCO training captions
paths['captions'] = '/Users/shreyajain/storyteller/coco_train_caps.txt'

# Biases
paths['negbias'] = '/Users/shreyajain/storyteller/caption_style.npy'
paths['posbias'] = '/Users/shreyajain/storyteller/romance_style.npy'
