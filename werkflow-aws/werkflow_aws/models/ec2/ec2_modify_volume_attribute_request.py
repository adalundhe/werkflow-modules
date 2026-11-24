from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue


class EC2ModifyVolumeAttributeRequest(BaseModel):
    VolumeId: StrictStr
    AutoEnableIO: EC2AttributeBooleanValue | None = None
    DryRun: StrictBool | None = None
