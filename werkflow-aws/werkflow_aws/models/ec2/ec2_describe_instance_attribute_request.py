from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeInstanceAttributeRequest(BaseModel):
    InstanceId: StrictStr
    Attribute: Literal['instanceType', 'kernel', 'ramdisk', 'userData', 'disableApiTermination', 'instanceInitiatedShutdownBehavior', 'rootDeviceName', 'blockDeviceMapping', 'productCodes', 'sourceDestCheck', 'groupSet', 'ebsOptimized', 'sriovNetSupport', 'enaSupport', 'enclaveOptions', 'disableApiStop']
    DryRun: StrictBool | None = None
