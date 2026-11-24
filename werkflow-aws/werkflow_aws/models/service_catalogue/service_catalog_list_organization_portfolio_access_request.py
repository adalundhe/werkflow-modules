from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListOrganizationPortfolioAccessRequest(BaseModel):
    PortfolioId: StrictStr
    OrganizationNodeType: Literal['ORGANIZATION', 'ORGANIZATIONAL_UNIT', 'ACCOUNT']
    AcceptLanguage: StrictStr | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
