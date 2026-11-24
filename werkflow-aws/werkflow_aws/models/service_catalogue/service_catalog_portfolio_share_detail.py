from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogPortfolioShareDetail(BaseModel):
    PrincipalId: StrictStr | None = None
    Type: StrictStr | None = None
    Accepted: StrictBool | None = None
    ShareTagOptions: StrictBool | None = None
    SharePrincipals: StrictBool | None = None
