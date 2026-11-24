from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoUpdateStreamRequest(BaseModel):
    CurrentVersion: StrictStr
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    DeviceName: StrictStr | None = None
    MediaType: StrictStr | None = None
