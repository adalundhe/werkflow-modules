from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class FSxUpdateSnapmirrorRelationshipRequest(BaseModel):
    SnapmirrorRelationshipId: StrictStr
    ClientRequestToken: StrictStr | None = None
    PolicyId: StrictStr | None = None
    TransferSchedule: StrictStr | None = None
    ThrottleInKbps: StrictInt | None = None
    State: Literal['SNAPMIRRORED', 'PAUSED', 'BROKEN_OFF'] | None = None
