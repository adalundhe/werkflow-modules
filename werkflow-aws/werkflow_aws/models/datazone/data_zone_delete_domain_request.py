from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDeleteDomainRequest(BaseModel):
    identifier: StrictStr
    clientToken: StrictStr | None = None
    skipDeletionCheck: StrictBool | None = None
    cascadeDelete: StrictBool | None = None
