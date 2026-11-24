from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogAssociatePrincipalWithPortfolioRequest(BaseModel):
    PortfolioId: StrictStr
    PrincipalARN: StrictStr
    PrincipalType: Literal['IAM', 'IAM_PATTERN']
    AcceptLanguage: StrictStr | None = None
