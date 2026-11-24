from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogConstraintSummary(BaseModel):
    Type: StrictStr | None = None
    Description: StrictStr | None = None
