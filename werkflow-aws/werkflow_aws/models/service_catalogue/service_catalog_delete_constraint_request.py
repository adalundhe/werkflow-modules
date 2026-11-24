from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDeleteConstraintRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
