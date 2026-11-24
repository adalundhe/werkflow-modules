from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystUpdateProjectRequest(BaseModel):
    spaceName: StrictStr
    name: StrictStr
    description: StrictStr | None = None
