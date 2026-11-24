from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateProjectRequest(BaseModel):
    spaceName: StrictStr
    displayName: StrictStr
    description: StrictStr | None = None
