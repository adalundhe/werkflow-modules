from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRCreateStudioSessionMappingRequest(BaseModel):
    StudioId: StrictStr
    IdentityType: Literal['USER', 'GROUP']
    SessionPolicyArn: StrictStr
    IdentityId: StrictStr | None = None
    IdentityName: StrictStr | None = None
