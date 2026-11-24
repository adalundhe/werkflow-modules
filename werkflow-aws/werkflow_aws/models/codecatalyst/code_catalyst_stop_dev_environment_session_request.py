from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystStopDevEnvironmentSessionRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    id: StrictStr
    sessionId: StrictStr
