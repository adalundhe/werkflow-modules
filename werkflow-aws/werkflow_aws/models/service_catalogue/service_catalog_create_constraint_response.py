from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_constraint_detail import ServiceCatalogConstraintDetail


class ServiceCatalogCreateConstraintResponse(BaseModel):
    ConstraintDetail: ServiceCatalogConstraintDetail | None = None
    ConstraintParameters: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
