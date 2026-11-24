from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisRegisterStreamConsumerRequest(BaseModel):
    StreamARN: StrictStr
    ConsumerName: StrictStr
    StreamId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
