from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailAccessRules(BaseModel):
    getObject: StrictStr | None = None
    allowPublicOverrides: StrictBool | None = None
