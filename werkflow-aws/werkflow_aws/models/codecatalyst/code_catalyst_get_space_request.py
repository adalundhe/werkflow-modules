from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetSpaceRequest(BaseModel):
    name: StrictStr
