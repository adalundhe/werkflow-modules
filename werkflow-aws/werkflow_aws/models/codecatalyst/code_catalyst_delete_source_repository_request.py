from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteSourceRepositoryRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    name: StrictStr
