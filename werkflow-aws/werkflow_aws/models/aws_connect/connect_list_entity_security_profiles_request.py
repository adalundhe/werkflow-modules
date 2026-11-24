from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListEntitySecurityProfilesRequest(BaseModel):
    InstanceId: StrictStr
    EntityType: Literal['USER', 'AI_AGENT']
    EntityArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
