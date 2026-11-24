from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListAddonsResponse(BaseModel):
    addons: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
