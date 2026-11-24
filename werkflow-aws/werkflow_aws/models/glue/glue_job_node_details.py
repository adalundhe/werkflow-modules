from __future__ import annotations
from pydantic import BaseModel
from .glue_job_run import GlueJobRun


class GlueJobNodeDetails(BaseModel):
    JobRuns: list[GlueJobRun] | None = None
