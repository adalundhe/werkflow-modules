from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_dataset_import_job_summary import PersonalizeDatasetImportJobSummary


class PersonalizeListDatasetImportJobsResponse(BaseModel):
    datasetImportJobs: list[PersonalizeDatasetImportJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
