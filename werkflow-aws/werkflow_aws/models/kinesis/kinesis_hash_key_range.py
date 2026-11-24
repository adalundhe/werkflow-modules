from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisHashKeyRange(BaseModel):
    StartingHashKey: StrictStr | None = None
    EndingHashKey: StrictStr | None = None
