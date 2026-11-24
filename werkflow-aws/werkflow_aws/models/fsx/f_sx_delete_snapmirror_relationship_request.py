from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteSnapmirrorRelationshipRequest(BaseModel):
    SnapmirrorRelationshipId: StrictStr
    ClientRequestToken: StrictStr | None = None
