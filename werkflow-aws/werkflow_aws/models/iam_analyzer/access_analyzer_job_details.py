from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_job_error import AccessAnalyzerJobError


class AccessAnalyzerJobDetails(BaseModel):
    jobId: StrictStr | None = None
    status: StrictStr | None = None
    startedOn: datetime.datetime | StrictStr | None = None
    completedOn: datetime.datetime | StrictStr | None = None
    jobError: AccessAnalyzerJobError | None = None
