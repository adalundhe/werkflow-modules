from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDeleteStreamRequest(BaseModel):
    StreamARN: StrictStr
    CurrentVersion: StrictStr | None = None
