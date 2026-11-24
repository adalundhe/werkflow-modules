from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueResponseConfiguration(BaseModel):
    ResultPath: StrictStr | None = None
    ErrorPath: StrictStr | None = None
