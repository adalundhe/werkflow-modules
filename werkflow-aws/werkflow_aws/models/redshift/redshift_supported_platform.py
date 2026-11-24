from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftSupportedPlatform(BaseModel):
    Name: StrictStr | None = None
