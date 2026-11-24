from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisDeleteStreamRequest(BaseModel):
    StreamName: StrictStr | None = None
    EnforceConsumerDeletion: StrictBool | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
