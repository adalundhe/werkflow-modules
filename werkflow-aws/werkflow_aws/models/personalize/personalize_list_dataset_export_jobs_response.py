from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_dataset_export_job_summary import PersonalizeDatasetExportJobSummary


class PersonalizeListDatasetExportJobsResponse(BaseModel):
    datasetExportJobs: list[PersonalizeDatasetExportJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
