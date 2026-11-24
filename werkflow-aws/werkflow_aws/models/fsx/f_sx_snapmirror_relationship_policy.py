from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSnapmirrorRelationshipPolicy(BaseModel):
    PolicyId: StrictStr | None = None
    PolicyName: StrictStr | None = None
