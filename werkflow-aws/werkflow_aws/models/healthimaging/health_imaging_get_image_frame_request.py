from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .health_imaging_image_frame_information import HealthImagingImageFrameInformation


class HealthImagingGetImageFrameRequest(BaseModel):
    datastoreId: StrictStr
    imageSetId: StrictStr
    imageFrameInformation: HealthImagingImageFrameInformation
