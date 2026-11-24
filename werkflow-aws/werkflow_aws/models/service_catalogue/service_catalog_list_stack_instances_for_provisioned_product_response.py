from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_stack_instance import ServiceCatalogStackInstance


class ServiceCatalogListStackInstancesForProvisionedProductResponse(BaseModel):
    StackInstances: list[ServiceCatalogStackInstance] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
