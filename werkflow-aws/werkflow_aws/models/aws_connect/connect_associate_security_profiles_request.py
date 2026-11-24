from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_security_profile_item import ConnectSecurityProfileItem


class ConnectAssociateSecurityProfilesRequest(BaseModel):
    InstanceId: StrictStr
    SecurityProfiles: list[ConnectSecurityProfileItem]
    EntityType: Literal['USER', 'AI_AGENT']
    EntityArn: StrictStr
