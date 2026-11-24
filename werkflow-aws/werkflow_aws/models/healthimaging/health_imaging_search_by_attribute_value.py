from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .health_imaging_dicom_study_date_and_time import HealthImagingDICOMStudyDateAndTime


class HealthImagingSearchByAttributeValue(BaseModel):
    DICOMPatientId: StrictStr | None = None
    DICOMAccessionNumber: StrictStr | None = None
    DICOMStudyId: StrictStr | None = None
    DICOMStudyInstanceUID: StrictStr | None = None
    DICOMSeriesInstanceUID: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    DICOMStudyDateAndTime: HealthImagingDICOMStudyDateAndTime | None = None
    isPrimary: StrictBool | None = None
