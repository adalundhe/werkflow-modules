from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteSpaceRequest(BaseModel):
    name: StrictStr
