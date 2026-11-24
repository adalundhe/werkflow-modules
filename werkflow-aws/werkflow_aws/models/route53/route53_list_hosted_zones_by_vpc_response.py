from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_hosted_zone_summary import Route53HostedZoneSummary


class Route53ListHostedZonesByVPCResponse(BaseModel):
    HostedZoneSummaries: list[Route53HostedZoneSummary] | None = None
    MaxItems: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
