import numpy as np

def mask2rgb(mask: np.array, palette: list[list]):
    """
    Maps output class segmentation mask to RGB image.

    :param mask: np.array(int) of produced segmentation mask
    :param palette: (optional) list of lists of RGB values to use for masks.
    :return: np.array(H, W, 3) of rgb values for corresponding segmentation masks
    """
    img = np.zeros((mask.shape[0], mask.shape[1], 3))
    for l in np.unique(mask):
        img[mask == int(l)] = palette[int(l)]
    return img.astype(int)
