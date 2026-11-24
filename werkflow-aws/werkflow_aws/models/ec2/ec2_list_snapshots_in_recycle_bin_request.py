from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ListSnapshotsInRecycleBinRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SnapshotIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
