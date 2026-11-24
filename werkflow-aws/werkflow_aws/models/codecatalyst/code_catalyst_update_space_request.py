from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystUpdateSpaceRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
