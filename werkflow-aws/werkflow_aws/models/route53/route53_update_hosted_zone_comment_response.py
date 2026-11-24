from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_hosted_zone_model import Route53HostedZoneModel


class Route53UpdateHostedZoneCommentResponse(BaseModel):
    HostedZone: Route53HostedZoneModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
