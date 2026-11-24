from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .health_imaging_image_sets_metadata_summary import HealthImagingImageSetsMetadataSummary
from .health_imaging_sort import HealthImagingSort


class HealthImagingSearchImageSetsResponse(BaseModel):
    imageSetsMetadataSummaries: list[HealthImagingImageSetsMetadataSummary] | None = None
    sort: HealthImagingSort | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
