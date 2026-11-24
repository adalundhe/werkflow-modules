from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteProjectRequest(BaseModel):
    spaceName: StrictStr
    name: StrictStr
