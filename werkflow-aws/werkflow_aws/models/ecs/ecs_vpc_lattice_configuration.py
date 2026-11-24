from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_vpc_lattice_advanced_configuration import ECSVpcLatticeAdvancedConfiguration


class ECSVpcLatticeConfiguration(BaseModel):
    roleArn: StrictStr | None = None
    targetGroupArn: StrictStr | None = None
    portName: StrictStr | None = None
    advancedConfiguration: ECSVpcLatticeAdvancedConfiguration | None = None
