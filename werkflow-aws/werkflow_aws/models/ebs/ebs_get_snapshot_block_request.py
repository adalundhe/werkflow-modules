from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)


class EBSGetSnapshotBlockRequest(BaseModel):
    SnapshotId: StrictStr
    BlockIndex: StrictInt
    BlockToken: StrictStr
