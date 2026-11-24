from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_reserved_instances_configuration import EC2ReservedInstancesConfiguration


class EC2ReservedInstancesModificationResult(BaseModel):
    ReservedInstancesId: StrictStr | None = None
    TargetConfiguration: EC2ReservedInstancesConfiguration | None = None
