from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeSyncRedaction(BaseModel):
    Type: StrictStr | None = None
