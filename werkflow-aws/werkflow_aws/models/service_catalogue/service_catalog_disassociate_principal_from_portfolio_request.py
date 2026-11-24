from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogDisassociatePrincipalFromPortfolioRequest(BaseModel):
    PortfolioId: StrictStr
    PrincipalARN: StrictStr
    AcceptLanguage: StrictStr | None = None
    PrincipalType: Literal['IAM', 'IAM_PATTERN'] | None = None
