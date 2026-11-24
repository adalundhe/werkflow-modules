from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_level import SecurityLevel


class SecurityScheme(BaseModel):
    defaultSecurityLevelId: StrictInt | None = None
    description: StrictStr | None = None
    id: StrictInt | None = None
    levels: list[SecurityLevel] | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
