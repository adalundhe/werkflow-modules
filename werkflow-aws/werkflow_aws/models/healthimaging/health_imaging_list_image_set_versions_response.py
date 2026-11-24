from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .health_imaging_image_set_properties import HealthImagingImageSetProperties


class HealthImagingListImageSetVersionsResponse(BaseModel):
    imageSetPropertiesList: list[HealthImagingImageSetProperties] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
