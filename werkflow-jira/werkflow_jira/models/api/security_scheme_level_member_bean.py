from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecuritySchemeLevelMemberBean(BaseModel):
    parameter: StrictStr | None = None
    type: StrictStr | None = None
