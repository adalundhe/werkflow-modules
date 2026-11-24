from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_reserved_instances_configuration import EC2ReservedInstancesConfiguration


class EC2ModifyReservedInstancesRequest(BaseModel):
    ReservedInstancesIds: list[StrictStr]
    TargetConfigurations: list[EC2ReservedInstancesConfiguration]
    ClientToken: StrictStr | None = None
