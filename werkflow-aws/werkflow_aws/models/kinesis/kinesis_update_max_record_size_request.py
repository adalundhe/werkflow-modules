from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateMaxRecordSizeRequest(BaseModel):
    MaxRecordSizeInKiB: StrictInt
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
