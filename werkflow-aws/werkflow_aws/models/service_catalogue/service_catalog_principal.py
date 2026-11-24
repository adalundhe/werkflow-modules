from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogPrincipal(BaseModel):
    PrincipalARN: StrictStr | None = None
    PrincipalType: StrictStr | None = None
