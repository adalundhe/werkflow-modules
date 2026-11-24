from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisSequenceNumberRange(BaseModel):
    StartingSequenceNumber: StrictStr | None = None
    EndingSequenceNumber: StrictStr | None = None
