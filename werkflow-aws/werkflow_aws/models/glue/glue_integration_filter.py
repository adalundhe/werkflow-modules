from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIntegrationFilter(BaseModel):
    Name: StrictStr | None = None
    Values: list[StrictStr] | None = None
