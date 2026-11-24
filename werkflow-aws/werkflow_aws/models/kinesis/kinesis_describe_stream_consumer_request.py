from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDescribeStreamConsumerRequest(BaseModel):
    StreamARN: StrictStr | None = None
    ConsumerName: StrictStr | None = None
    ConsumerARN: StrictStr | None = None
    StreamId: StrictStr | None = None
