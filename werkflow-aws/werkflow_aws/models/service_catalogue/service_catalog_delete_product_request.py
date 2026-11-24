from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDeleteProductRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
