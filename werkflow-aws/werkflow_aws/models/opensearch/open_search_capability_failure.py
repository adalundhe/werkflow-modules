from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCapabilityFailure(BaseModel):
    reason: StrictStr | None = None
    details: StrictStr | None = None
