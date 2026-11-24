from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)


class EBSListChangedBlocksRequest(BaseModel):
    SecondSnapshotId: StrictStr
    FirstSnapshotId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StartingBlockIndex: StrictInt | None = None
