from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingDICOMStudyDateAndTime(BaseModel):
    DICOMStudyDate: StrictStr
    DICOMStudyTime: StrictStr | None = None
