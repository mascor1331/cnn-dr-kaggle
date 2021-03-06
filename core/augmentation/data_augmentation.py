from skimage import io
from keras.preprocessing.image import ImageDataGenerator
from scipy.ndimage.interpolation import zoom
import numpy as np

def zoom_image(image, zoom_range, fill_mode='constant', cval=0.):
    if zoom_range[0] == 1 and zoom_range[1] == 1:
        z = 1
    else:
        z = np.random.uniform(zoom_range[0], zoom_range[1], 1)[0]

    zoomed_image = zoom(image, [z, z, 1], mode=fill_mode, cval=cval)

    target_size = image.shape
    zoomed_size = zoomed_image.shape

    return zoomed_image[int(zoomed_size[0]/2-target_size[0]/2):int(zoomed_size[0]/2+target_size[0]/2),
                        int(zoomed_size[1]/2-target_size[1]/2):int(zoomed_size[1]/2+target_size[1]/2),
                        :]

def get_image_data_generator(data_type, config):

    if (data_type=="training"):
        # datagen will be as follows:
        datagen = ImageDataGenerator(
            # For more information about these parameters
            # visit: https://keras.io/preprocessing/image/
            featurewise_center = (config['featurewise_center']=='True'),
            featurewise_std_normalization = (config['featurewise_std_normalization']=='True'),
            fill_mode = config['fill_mode'],
            cval = float(config['cval']),
            horizontal_flip = (config['horizontal_flip'] =='True'),
            vertical_flip = (config['vertical_flip'] == 'True'),
            rescale = float(config['rescale'])
            )
    else: # data_type == "validation" or data_type == "test"
        # datagen will be only rescale
        datagen = ImageDataGenerator(
            featurewise_center = (config['featurewise_center']=='True'),
            featurewise_std_normalization = (config['featurewise_std_normalization']=='True'),
            rescale = float(config['rescale'])
            )

    # return our datagen object
    return datagen
