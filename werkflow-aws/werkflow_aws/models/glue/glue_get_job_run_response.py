from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_job_run import GlueJobRun


class GlueGetJobRunResponse(BaseModel):
    JobRun: GlueJobRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
