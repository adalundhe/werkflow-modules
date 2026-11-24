from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .health_imaging_dicom_import_job_properties import HealthImagingDICOMImportJobProperties


class HealthImagingGetDICOMImportJobResponse(BaseModel):
    jobProperties: HealthImagingDICOMImportJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
