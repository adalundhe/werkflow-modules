from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class HealthImagingDICOMTags(BaseModel):
    DICOMPatientId: StrictStr | None = None
    DICOMPatientName: StrictStr | None = None
    DICOMPatientBirthDate: StrictStr | None = None
    DICOMPatientSex: StrictStr | None = None
    DICOMStudyInstanceUID: StrictStr | None = None
    DICOMStudyId: StrictStr | None = None
    DICOMStudyDescription: StrictStr | None = None
    DICOMNumberOfStudyRelatedSeries: StrictInt | None = None
    DICOMNumberOfStudyRelatedInstances: StrictInt | None = None
    DICOMAccessionNumber: StrictStr | None = None
    DICOMSeriesInstanceUID: StrictStr | None = None
    DICOMSeriesModality: StrictStr | None = None
    DICOMSeriesBodyPart: StrictStr | None = None
    DICOMSeriesNumber: StrictInt | None = None
    DICOMStudyDate: StrictStr | None = None
    DICOMStudyTime: StrictStr | None = None
