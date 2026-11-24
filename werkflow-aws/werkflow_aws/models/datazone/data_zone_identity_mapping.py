from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneIdentityMapping(BaseModel):
    usernameAttribute: StrictStr | None = None
    prefix: StrictStr | None = None
