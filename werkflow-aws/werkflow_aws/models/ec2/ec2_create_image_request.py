from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_block_device_mapping import EC2BlockDeviceMapping
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateImageRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    SnapshotLocation: Literal['regional', 'local'] | None = None
    BootModeOverride: Literal['uefi'] | None = None
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    NoReboot: StrictBool | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMapping] | None = None
