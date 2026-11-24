from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_service_action_summary import ServiceCatalogServiceActionSummary


class ServiceCatalogListServiceActionsForProvisioningArtifactResponse(BaseModel):
    ServiceActionSummaries: list[ServiceCatalogServiceActionSummary] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
