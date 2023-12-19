from mmseg.datasets.builder import PIPELINES
from mmseg.datasets.pipelines import ImageToTensor, to_tensor
import numpy as np


# ________________
# Modified version from mmcv to directly convert a tensor to float
# MAKE SURE YOU USE IT ONLY FOR IMAGES

@PIPELINES.register_module()
class ImageToTensorV2(ImageToTensor):
    """Convert image to :obj:`torch.Tensor` by given keys.

    The dimension order of input image is (H, W, C). The pipeline will convert
    it to (C, H, W). If only 2 dimension (H, W) is given, the output would be
    (1, H, W).

    Required keys:

    - all these keys in `keys`

    Modified Keys:

    - all these keys in `keys`

    Args:
        keys (Sequence[str]): Key of images to be converted to Tensor.
    """

    def __init__(self, keys: dict) -> None:
        super(ImageToTensorV2, self).__init__(keys)
        self.keys = keys

    def __call__(self, results):
        return self.transform(results)

    def transform(self, results: dict) -> dict:
        """Transform function to convert image in results to
        :obj:`torch.Tensor` and transpose the channel order.
        Args:
            results (dict): Result dict contains the image data to convert.
        Returns:
            dict: The result dict contains the image converted
            to :obj:``torch.Tensor`` and transposed to (C, H, W) order.
        """
        for key in self.keys:
            img = results[key]
            if len(img.shape) < 3:
                img = np.expand_dims(img, -1)

            results[key] = (to_tensor(img.copy()).permute(2, 0, 1)).contiguous() / 255.

        return results
