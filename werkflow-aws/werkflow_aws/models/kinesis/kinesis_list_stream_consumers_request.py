from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisListStreamConsumersRequest(BaseModel):
    StreamARN: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
    StreamId: StrictStr | None = None
