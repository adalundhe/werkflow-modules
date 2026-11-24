from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_job_run import GlueJobRun


class GlueGetJobRunsResponse(BaseModel):
    JobRuns: list[GlueJobRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
