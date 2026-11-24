from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_cloud_watch_region import Route53CloudWatchRegion


class Route53AlarmIdentifier(BaseModel):
    Region: Route53CloudWatchRegion | None = None
    Name: StrictStr | None = None
