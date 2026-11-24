from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetDevEnvironmentRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    id: StrictStr
