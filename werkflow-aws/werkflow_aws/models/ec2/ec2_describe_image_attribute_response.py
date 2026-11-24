from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_attribute_value import EC2AttributeValue
from .ec2_block_device_mapping import EC2BlockDeviceMapping
from .ec2_launch_permission import EC2LaunchPermission
from .ec2_product_code import EC2ProductCode


class EC2DescribeImageAttributeResponse(BaseModel):
    Description: EC2AttributeValue | None = None
    KernelId: EC2AttributeValue | None = None
    RamdiskId: EC2AttributeValue | None = None
    SriovNetSupport: EC2AttributeValue | None = None
    BootMode: EC2AttributeValue | None = None
    TpmSupport: EC2AttributeValue | None = None
    UefiData: EC2AttributeValue | None = None
    LastLaunchedTime: EC2AttributeValue | None = None
    ImdsSupport: EC2AttributeValue | None = None
    DeregistrationProtection: EC2AttributeValue | None = None
    ImageId: StrictStr | None = None
    LaunchPermissions: list[EC2LaunchPermission] | None = None
    ProductCodes: list[EC2ProductCode] | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMapping] | None = None
    ResponseMetadata: dict[str, Any] | None = None
