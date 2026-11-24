from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .health_imaging_copy_destination_image_set_properties import HealthImagingCopyDestinationImageSetProperties
from .health_imaging_copy_source_image_set_properties import HealthImagingCopySourceImageSetProperties


class HealthImagingCopyImageSetResponse(BaseModel):
    datastoreId: StrictStr | None = None
    sourceImageSetProperties: HealthImagingCopySourceImageSetProperties | None = None
    destinationImageSetProperties: HealthImagingCopyDestinationImageSetProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
