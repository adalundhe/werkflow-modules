from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_resource_change_detail import ServiceCatalogResourceChangeDetail


class ServiceCatalogResourceChange(BaseModel):
    Action: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Replacement: StrictStr | None = None
    Scope: list[StrictStr] | None = None
    Details: list[ServiceCatalogResourceChangeDetail] | None = None
