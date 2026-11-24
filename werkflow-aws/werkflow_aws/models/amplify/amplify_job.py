from __future__ import annotations
from pydantic import BaseModel
from .amplify_job_summary import AmplifyJobSummary
from .amplify_step import AmplifyStep


class AmplifyJob(BaseModel):
    summary: AmplifyJobSummary | None = None
    steps: list[AmplifyStep] | None = None
