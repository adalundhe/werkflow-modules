from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailSession(BaseModel):
    name: StrictStr | None = None
    url: StrictStr | None = None
    isPrimary: StrictBool | None = None
