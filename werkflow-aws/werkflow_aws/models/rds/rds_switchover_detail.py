from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSSwitchoverDetail(BaseModel):
    SourceMember: StrictStr | None = None
    TargetMember: StrictStr | None = None
    Status: StrictStr | None = None
