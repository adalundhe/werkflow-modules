from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_job_update import GlueJobUpdate


class GlueUpdateJobRequest(BaseModel):
    JobName: StrictStr
    JobUpdate: GlueJobUpdate
