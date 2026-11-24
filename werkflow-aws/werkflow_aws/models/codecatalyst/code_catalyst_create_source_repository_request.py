from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateSourceRepositoryRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    name: StrictStr
    description: StrictStr | None = None
