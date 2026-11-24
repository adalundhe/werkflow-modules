from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2EventActorReference(BaseModel):
    EventActorId: StrictStr | None = None
    EventActorValue: StrictStr | None = None
