from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_share_error import ServiceCatalogShareError


class ServiceCatalogShareDetails(BaseModel):
    SuccessfulShares: list[StrictStr] | None = None
    ShareErrors: list[ServiceCatalogShareError] | None = None
