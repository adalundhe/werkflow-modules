from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogDescribePortfolioSharesRequest(BaseModel):
    PortfolioId: StrictStr
    Type: Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT', 'ORGANIZATION_MEMBER_ACCOUNT']
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
