from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRGetStudioSessionMappingRequest(BaseModel):
    StudioId: StrictStr
    IdentityType: Literal['USER', 'GROUP']
    IdentityId: StrictStr | None = None
    IdentityName: StrictStr | None = None
