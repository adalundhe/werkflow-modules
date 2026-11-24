from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)


class EBSListSnapshotBlocksRequest(BaseModel):
    SnapshotId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StartingBlockIndex: StrictInt | None = None
