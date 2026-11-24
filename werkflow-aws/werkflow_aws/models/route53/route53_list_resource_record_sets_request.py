from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_rr_type import Route53RRType


class Route53ListResourceRecordSetsRequest(BaseModel):
    HostedZoneId: StrictStr
    StartRecordName: StrictStr | None = None
    StartRecordType: Route53RRType | None = None
    StartRecordIdentifier: StrictStr | None = None
    MaxItems: StrictStr | None = None
