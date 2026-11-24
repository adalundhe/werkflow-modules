from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieRevealConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None
    status: StrictStr | None = None
