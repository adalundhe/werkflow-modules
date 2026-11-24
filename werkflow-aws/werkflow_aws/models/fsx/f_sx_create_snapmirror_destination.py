from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxCreateSnapmirrorDestination(BaseModel):
    VolumeId: StrictStr
