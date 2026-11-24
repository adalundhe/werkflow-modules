from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisConsumerDescription(BaseModel):
    ConsumerName: StrictStr | None = None
    ConsumerARN: StrictStr | None = None
    ConsumerStatus: StrictStr | None = None
    ConsumerCreationTimestamp: datetime.datetime | StrictStr | None = None
    StreamARN: StrictStr | None = None
