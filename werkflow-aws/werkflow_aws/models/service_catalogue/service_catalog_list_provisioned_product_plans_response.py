from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioned_product_plan_summary import ServiceCatalogProvisionedProductPlanSummary


class ServiceCatalogListProvisionedProductPlansResponse(BaseModel):
    ProvisionedProductPlans: list[ServiceCatalogProvisionedProductPlanSummary] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
