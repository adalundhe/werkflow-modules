from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisConsumer(BaseModel):
    ConsumerName: StrictStr | None = None
    ConsumerARN: StrictStr | None = None
    ConsumerStatus: StrictStr | None = None
    ConsumerCreationTimestamp: datetime.datetime | StrictStr | None = None
