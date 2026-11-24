from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerResumeServiceRequest(BaseModel):
    ServiceArn: StrictStr
