from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogServiceActionSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    DefinitionType: StrictStr | None = None
