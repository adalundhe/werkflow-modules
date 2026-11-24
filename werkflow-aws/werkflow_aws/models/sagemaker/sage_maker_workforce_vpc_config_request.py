from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerWorkforceVpcConfigRequest(BaseModel):
    VpcId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Subnets: list[StrictStr] | None = None
