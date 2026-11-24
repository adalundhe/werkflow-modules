from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetProjectRequest(BaseModel):
    spaceName: StrictStr
    name: StrictStr
