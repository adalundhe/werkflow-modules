from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_change_batch_summary import Route53ChangeBatchSummary


class Route53ListHostedZoneChangeBatchesResponse(BaseModel):
    ChangeBatchSummaries: list[Route53ChangeBatchSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
