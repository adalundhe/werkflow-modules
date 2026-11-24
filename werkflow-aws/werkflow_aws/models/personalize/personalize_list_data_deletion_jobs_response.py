from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_data_deletion_job_summary import PersonalizeDataDeletionJobSummary


class PersonalizeListDataDeletionJobsResponse(BaseModel):
    dataDeletionJobs: list[PersonalizeDataDeletionJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
