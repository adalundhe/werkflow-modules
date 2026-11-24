from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisListStreamsRequest(BaseModel):
    Limit: StrictInt | None = None
    ExclusiveStartStreamName: StrictStr | None = None
    NextToken: StrictStr | None = None
