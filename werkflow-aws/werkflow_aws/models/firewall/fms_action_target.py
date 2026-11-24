from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSActionTarget(BaseModel):
    ResourceId: StrictStr | None = None
    Description: StrictStr | None = None
