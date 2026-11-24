from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeAwsVpcConfiguration(BaseModel):
    Subnets: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    AssignPublicIp: StrictStr | None = None
