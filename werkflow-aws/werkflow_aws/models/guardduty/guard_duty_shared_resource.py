from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutySharedResource(BaseModel):
    ResourceType: StrictStr | None = None
    Identifier: StrictStr | None = None
