from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAAUpdateNetworkConfigurationInput(BaseModel):
    SecurityGroupIds: list[StrictStr]
