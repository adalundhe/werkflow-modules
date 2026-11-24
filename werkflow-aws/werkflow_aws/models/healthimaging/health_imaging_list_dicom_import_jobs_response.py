from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .health_imaging_dicom_import_job_summary import HealthImagingDICOMImportJobSummary


class HealthImagingListDICOMImportJobsResponse(BaseModel):
    jobSummaries: list[HealthImagingDICOMImportJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
