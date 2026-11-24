from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogUsageInstruction(BaseModel):
    Type: StrictStr | None = None
    Value: StrictStr | None = None
