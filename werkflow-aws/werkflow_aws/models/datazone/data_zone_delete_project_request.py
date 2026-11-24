from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDeleteProjectRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    skipDeletionCheck: StrictBool | None = None
