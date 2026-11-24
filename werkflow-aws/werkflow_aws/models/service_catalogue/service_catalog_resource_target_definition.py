from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogResourceTargetDefinition(BaseModel):
    Attribute: StrictStr | None = None
    Name: StrictStr | None = None
    RequiresRecreation: StrictStr | None = None
