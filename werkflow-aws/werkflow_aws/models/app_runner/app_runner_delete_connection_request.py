from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDeleteConnectionRequest(BaseModel):
    ConnectionArn: StrictStr
