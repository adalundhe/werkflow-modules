from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseAuthenticationConfiguration(BaseModel):
    RoleARN: StrictStr | None = None
    Connectivity: StrictStr | None = None
