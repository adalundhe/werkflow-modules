from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDeleteServiceActionRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
