from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribePortfolioShareStatusRequest(BaseModel):
    PortfolioShareToken: StrictStr
