from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KinesisPutRecordRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Data: StrictBytes | BinaryIO | StrictStr
    StreamName: StrictStr | None = None
    PartitionKey: StrictStr | None = None
    ExplicitHashKey: StrictStr | None = None
    SequenceNumberForOrdering: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
    DryRun: StrictBool | None = None
