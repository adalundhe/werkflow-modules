from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AccessAnalyzerPolicyGeneration(BaseModel):
    jobId: StrictStr | None = None
    principalArn: StrictStr | None = None
    status: StrictStr | None = None
    startedOn: datetime.datetime | StrictStr | None = None
    completedOn: datetime.datetime | StrictStr | None = None
