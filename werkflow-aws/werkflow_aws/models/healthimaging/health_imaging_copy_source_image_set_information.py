from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .health_imaging_metadata_copies import HealthImagingMetadataCopies


class HealthImagingCopySourceImageSetInformation(BaseModel):
    latestVersionId: StrictStr
    DICOMCopies: HealthImagingMetadataCopies | None = None
