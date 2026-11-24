from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .health_imaging_dicom_updates import HealthImagingDICOMUpdates


class HealthImagingMetadataUpdates(BaseModel):
    DICOMUpdates: HealthImagingDICOMUpdates | None = None
    revertToVersionId: StrictStr | None = None
