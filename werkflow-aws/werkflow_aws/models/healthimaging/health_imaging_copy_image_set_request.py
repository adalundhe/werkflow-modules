from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .health_imaging_copy_image_set_information import HealthImagingCopyImageSetInformation


class HealthImagingCopyImageSetRequest(BaseModel):
    datastoreId: StrictStr
    sourceImageSetId: StrictStr
    copyImageSetInformation: HealthImagingCopyImageSetInformation
    force: StrictBool | None = None
    promoteToPrimary: StrictBool | None = None
