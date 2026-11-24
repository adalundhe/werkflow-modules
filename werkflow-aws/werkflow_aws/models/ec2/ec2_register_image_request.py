from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_block_device_mapping import EC2BlockDeviceMapping
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2RegisterImageRequest(BaseModel):
    Name: StrictStr
    ImageLocation: StrictStr | None = None
    BillingProducts: list[StrictStr] | None = None
    BootMode: Literal['legacy-bios', 'uefi', 'uefi-preferred'] | None = None
    TpmSupport: Literal['v2.0'] | None = None
    UefiData: StrictStr | None = None
    ImdsSupport: Literal['v2.0'] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    Architecture: Literal['i386', 'x86_64', 'arm64', 'x86_64_mac', 'arm64_mac'] | None = None
    KernelId: StrictStr | None = None
    RamdiskId: StrictStr | None = None
    RootDeviceName: StrictStr | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMapping] | None = None
    VirtualizationType: StrictStr | None = None
    SriovNetSupport: StrictStr | None = None
    EnaSupport: StrictBool | None = None
