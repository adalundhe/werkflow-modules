from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_job_summary import AmplifyJobSummary


class AmplifyListJobsResponse(BaseModel):
    jobSummaries: list[AmplifyJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
