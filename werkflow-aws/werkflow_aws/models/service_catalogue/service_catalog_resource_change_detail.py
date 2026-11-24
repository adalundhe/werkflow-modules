from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_resource_target_definition import ServiceCatalogResourceTargetDefinition


class ServiceCatalogResourceChangeDetail(BaseModel):
    Target: ServiceCatalogResourceTargetDefinition | None = None
    Evaluation: StrictStr | None = None
    CausingEntity: StrictStr | None = None
