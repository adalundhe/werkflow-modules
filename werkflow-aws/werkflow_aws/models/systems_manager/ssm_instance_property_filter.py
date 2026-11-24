from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMInstancePropertyFilter(BaseModel):
    key: Literal['InstanceIds', 'AgentVersion', 'PingStatus', 'PlatformTypes', 'DocumentName', 'ActivationIds', 'IamRole', 'ResourceType', 'AssociationStatus']
    valueSet: list[StrictStr]
