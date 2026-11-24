from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_distribution_tenant_summary import CloudFrontDistributionTenantSummary


class CloudFrontListDistributionTenantsByCustomizationResponse(BaseModel):
    NextMarker: StrictStr | None = None
    DistributionTenantList: list[CloudFrontDistributionTenantSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
