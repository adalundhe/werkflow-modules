from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_cloud_watch_dashboard import ServiceCatalogCloudWatchDashboard
from .service_catalog_provisioned_product_detail import ServiceCatalogProvisionedProductDetail


class ServiceCatalogDescribeProvisionedProductResponse(BaseModel):
    ProvisionedProductDetail: ServiceCatalogProvisionedProductDetail | None = None
    CloudWatchDashboards: list[ServiceCatalogCloudWatchDashboard] | None = None
    ResponseMetadata: dict[str, Any] | None = None
