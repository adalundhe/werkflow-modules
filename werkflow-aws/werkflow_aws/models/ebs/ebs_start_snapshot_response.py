import datetime
from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .ebs_tag import EBSTag
from .ebssse_type import EBSSSEType
from .ebs_status import EBSStatus


class EBSStartSnapshotResponse(BaseModel):
    Description: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Status: EBSStatus | None = None
    StartTime: datetime.datetime | None = None
    VolumeSize: StrictInt | None = None
    BlockSize: StrictInt | None = None
    Tags: list[EBSTag] | None = None
    ParentSnapshotId: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    SseType: EBSSSEType | None = None
