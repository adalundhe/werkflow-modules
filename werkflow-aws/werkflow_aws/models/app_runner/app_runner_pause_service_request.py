from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerPauseServiceRequest(BaseModel):
    ServiceArn: StrictStr
