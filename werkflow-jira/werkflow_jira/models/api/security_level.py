from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityLevel(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    issueSecuritySchemeId: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
