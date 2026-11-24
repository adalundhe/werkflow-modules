from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeImageAttributeRequest(BaseModel):
    Attribute: Literal['description', 'kernel', 'ramdisk', 'launchPermission', 'productCodes', 'blockDeviceMapping', 'sriovNetSupport', 'bootMode', 'tpmSupport', 'uefiData', 'lastLaunchedTime', 'imdsSupport', 'deregistrationProtection']
    ImageId: StrictStr
    DryRun: StrictBool | None = None
