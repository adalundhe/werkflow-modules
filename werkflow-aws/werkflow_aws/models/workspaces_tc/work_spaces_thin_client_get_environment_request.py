from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientGetEnvironmentRequest(BaseModel):
    id: StrictStr
