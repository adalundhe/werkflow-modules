from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientDeleteEnvironmentRequest(BaseModel):
    id: StrictStr
    clientToken: StrictStr | None = None
