from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_domains_operation_summary import Route53DomainsOperationSummary


class Route53DomainsListOperationsResponse(BaseModel):
    Operations: list[Route53DomainsOperationSummary] | None = None
    NextPageMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
