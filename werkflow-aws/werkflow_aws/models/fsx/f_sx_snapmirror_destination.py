from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSnapmirrorDestination(BaseModel):
    Path: StrictStr | None = None
    VolumeId: StrictStr | None = None
