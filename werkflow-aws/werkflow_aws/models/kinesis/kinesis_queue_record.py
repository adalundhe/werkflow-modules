from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class KinesisQueueRecord(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    ReceiptHandle: StrictStr | None = None
    RecordId: StrictStr | None = None
    PartitionKey: StrictStr | None = None
    Data: StrictBytes | Any | None = None
    ApproximateArrivalTimestamp: datetime.datetime | StrictStr | None = None
    FirstReceiveTimestamp: datetime.datetime | StrictStr | None = None
    ReceiveCount: StrictInt | None = None
