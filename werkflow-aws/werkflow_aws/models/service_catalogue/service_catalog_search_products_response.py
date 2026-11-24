from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_product_view_aggregation_value import ServiceCatalogProductViewAggregationValue
from .service_catalog_product_view_summary import ServiceCatalogProductViewSummary


class ServiceCatalogSearchProductsResponse(BaseModel):
    ProductViewSummaries: list[ServiceCatalogProductViewSummary] | None = None
    ProductViewAggregations: dict[StrictStr, list[ServiceCatalogProductViewAggregationValue]] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
