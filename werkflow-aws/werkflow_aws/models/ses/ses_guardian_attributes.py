from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGuardianAttributes(BaseModel):
    OptimizedSharedDelivery: StrictStr | None = None
