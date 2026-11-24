from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDescribeStreamSummaryRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
