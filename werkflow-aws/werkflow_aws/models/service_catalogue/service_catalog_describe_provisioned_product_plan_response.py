from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioned_product_plan_details import ServiceCatalogProvisionedProductPlanDetails
from .service_catalog_resource_change import ServiceCatalogResourceChange


class ServiceCatalogDescribeProvisionedProductPlanResponse(BaseModel):
    ProvisionedProductPlanDetails: ServiceCatalogProvisionedProductPlanDetails | None = None
    ResourceChanges: list[ServiceCatalogResourceChange] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
