from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KinesisPutRecordsRequestEntry(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Data: StrictBytes | BinaryIO | StrictStr
    ExplicitHashKey: StrictStr | None = None
    PartitionKey: StrictStr | None = None
