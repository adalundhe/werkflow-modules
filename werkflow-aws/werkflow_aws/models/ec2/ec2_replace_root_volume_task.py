from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2ReplaceRootVolumeTask(BaseModel):
    ReplaceRootVolumeTaskId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    TaskState: StrictStr | None = None
    StartTime: StrictStr | None = None
    CompleteTime: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ImageId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    DeleteReplacedRootVolume: StrictBool | None = None
