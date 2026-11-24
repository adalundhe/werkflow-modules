from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_job_summary import AmplifyJobSummary


class AmplifyStopJobResponse(BaseModel):
    jobSummary: AmplifyJobSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
