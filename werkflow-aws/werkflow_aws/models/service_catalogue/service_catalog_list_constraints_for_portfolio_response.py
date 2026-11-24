from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_constraint_detail import ServiceCatalogConstraintDetail


class ServiceCatalogListConstraintsForPortfolioResponse(BaseModel):
    ConstraintDetails: list[ServiceCatalogConstraintDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
