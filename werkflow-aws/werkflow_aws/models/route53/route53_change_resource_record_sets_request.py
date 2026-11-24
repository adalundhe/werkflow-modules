from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_change_batch import Route53ChangeBatch


class Route53ChangeResourceRecordSetsRequest(BaseModel):
    HostedZoneId: StrictStr
    ChangeBatch: Route53ChangeBatch
