from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGuardianOptions(BaseModel):
    OptimizedSharedDelivery: StrictStr | None = None
