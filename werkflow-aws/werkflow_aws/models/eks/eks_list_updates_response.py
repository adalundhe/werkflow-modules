from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListUpdatesResponse(BaseModel):
    updateIds: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
