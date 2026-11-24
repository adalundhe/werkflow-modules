import datetime
from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .ebs_changed_block import EBSChangedBlock


class EBSListChangedBlocksResponse(BaseModel):
    ChangedBlocks: list[EBSChangedBlock] | None = None
    ExpiryTime: datetime.datetime | None = None
    VolumeSize: StrictInt | None = None
    BlockSize: StrictInt | None = None
    NextToken: StrictStr | None = None
