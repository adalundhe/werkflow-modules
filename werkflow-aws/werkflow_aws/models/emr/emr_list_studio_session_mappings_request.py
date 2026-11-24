from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRListStudioSessionMappingsRequest(BaseModel):
    StudioId: StrictStr | None = None
    IdentityType: Literal['USER', 'GROUP'] | None = None
    Marker: StrictStr | None = None
