from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogConstraintDetail(BaseModel):
    ConstraintId: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Owner: StrictStr | None = None
    ProductId: StrictStr | None = None
    PortfolioId: StrictStr | None = None
