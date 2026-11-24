from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_budget_detail import ServiceCatalogBudgetDetail
from .service_catalog_launch_path import ServiceCatalogLaunchPath
from .service_catalog_product_view_summary import ServiceCatalogProductViewSummary
from .service_catalog_provisioning_artifact import ServiceCatalogProvisioningArtifact


class ServiceCatalogDescribeProductResponse(BaseModel):
    ProductViewSummary: ServiceCatalogProductViewSummary | None = None
    ProvisioningArtifacts: list[ServiceCatalogProvisioningArtifact] | None = None
    Budgets: list[ServiceCatalogBudgetDetail] | None = None
    LaunchPaths: list[ServiceCatalogLaunchPath] | None = None
    ResponseMetadata: dict[str, Any] | None = None
