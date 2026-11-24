import datetime
from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .ebs_block import EBSBlock


class EBSListSnapshotBlocksResponse(BaseModel):
    Blocks: list[EBSBlock] | None = None
    ExpiryTime: datetime.datetime | None = None
    VolumeSize: StrictInt | None = None
    BlockSize: StrictInt | None = None
    NextToken: StrictStr | None = None
