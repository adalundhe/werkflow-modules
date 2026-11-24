from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchVPCOptions(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    EgressEnabled: StrictBool | None = None
