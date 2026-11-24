from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSOptionGroupMembership(BaseModel):
    OptionGroupName: StrictStr | None = None
    Status: StrictStr | None = None
