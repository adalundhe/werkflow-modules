from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDeleteServiceRequest(BaseModel):
    ServiceArn: StrictStr
