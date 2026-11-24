from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribePortfolioRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
