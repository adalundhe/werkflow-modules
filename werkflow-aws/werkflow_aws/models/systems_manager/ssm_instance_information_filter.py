from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMInstanceInformationFilter(BaseModel):
    key: Literal['InstanceIds', 'AgentVersion', 'PingStatus', 'PlatformTypes', 'ActivationIds', 'IamRole', 'ResourceType', 'AssociationStatus']
    valueSet: list[StrictStr]
