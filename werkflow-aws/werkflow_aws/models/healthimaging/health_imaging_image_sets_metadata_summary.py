from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .health_imaging_dicom_tags import HealthImagingDICOMTags


class HealthImagingImageSetsMetadataSummary(BaseModel):
    imageSetId: StrictStr | None = None
    version: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    lastAccessedAt: datetime.datetime | StrictStr | None = None
    storageTier: StrictStr | None = None
    DICOMTags: HealthImagingDICOMTags | None = None
    isPrimary: StrictBool | None = None
