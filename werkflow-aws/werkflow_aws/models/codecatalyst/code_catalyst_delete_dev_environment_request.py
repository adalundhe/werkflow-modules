from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteDevEnvironmentRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    id: StrictStr
