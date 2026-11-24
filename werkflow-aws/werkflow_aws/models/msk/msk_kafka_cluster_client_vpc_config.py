from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterClientVpcConfig(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
