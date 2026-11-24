from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2JA4Fingerprint(BaseModel):
    FallbackBehavior: StrictStr | None = None
