from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogCreateConstraintRequest(BaseModel):
    PortfolioId: StrictStr
    ProductId: StrictStr
    Parameters: StrictStr
    Type: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    Description: StrictStr | None = None
