from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_constraint_summary import ServiceCatalogConstraintSummary
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogLaunchPathSummary(BaseModel):
    Id: StrictStr | None = None
    ConstraintSummaries: list[ServiceCatalogConstraintSummary] | None = None
    Tags: list[ServiceCatalogTag] | None = None
    Name: StrictStr | None = None
