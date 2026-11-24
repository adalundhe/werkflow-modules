from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_change_batch_model import Route53ChangeBatchModel
from .route53_change_batch_summary import Route53ChangeBatchSummary


class Route53GetHostedZoneChangeBatchResponse(BaseModel):
    ChangeBatchSummary: Route53ChangeBatchSummary | None = None
    ChangeBatch: Route53ChangeBatchModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
