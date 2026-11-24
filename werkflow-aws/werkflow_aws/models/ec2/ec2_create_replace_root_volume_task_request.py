from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateReplaceRootVolumeTaskRequest(BaseModel):
    InstanceId: StrictStr
    SnapshotId: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ImageId: StrictStr | None = None
    DeleteReplacedRootVolume: StrictBool | None = None
    VolumeInitializationRate: StrictInt | None = None
    VolumeId: StrictStr | None = None
