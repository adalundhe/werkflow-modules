from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSAwsVpcConfiguration(BaseModel):
    subnets: list[StrictStr] | None = None
    securityGroups: list[StrictStr] | None = None
    assignPublicIp: StrictStr | None = None
