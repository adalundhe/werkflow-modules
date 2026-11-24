from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KinesisRecord(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    SequenceNumber: StrictStr | None = None
    ApproximateArrivalTimestamp: datetime.datetime | StrictStr | None = None
    Data: StrictBytes | Any | None = None
    PartitionKey: StrictStr | None = None
    EncryptionType: StrictStr | None = None
