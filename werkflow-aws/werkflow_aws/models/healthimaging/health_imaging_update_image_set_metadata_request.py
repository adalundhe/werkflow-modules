from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .health_imaging_metadata_updates import HealthImagingMetadataUpdates


class HealthImagingUpdateImageSetMetadataRequest(BaseModel):
    datastoreId: StrictStr
    imageSetId: StrictStr
    latestVersionId: StrictStr
    updateImageSetMetadataUpdates: HealthImagingMetadataUpdates
    force: StrictBool | None = None
    includeStudyImageSets: StrictBool | None = None
