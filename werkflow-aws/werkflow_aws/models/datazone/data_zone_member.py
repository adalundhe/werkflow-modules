from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMember(BaseModel):
    userIdentifier: StrictStr | None = None
    groupIdentifier: StrictStr | None = None
