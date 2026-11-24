from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeProductAsAdminRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    SourcePortfolioId: StrictStr | None = None
