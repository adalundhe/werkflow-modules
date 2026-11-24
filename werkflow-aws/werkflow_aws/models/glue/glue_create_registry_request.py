from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateRegistryRequest(BaseModel):
    RegistryName: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
