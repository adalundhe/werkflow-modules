from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateDefaultScreenScheme(BaseModel):
    screenSchemeId: StrictStr | None = None
