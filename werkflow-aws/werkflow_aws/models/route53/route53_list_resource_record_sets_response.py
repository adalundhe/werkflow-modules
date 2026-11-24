from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_resource_record_set import Route53ResourceRecordSet
from .route53_rr_type import Route53RRType


class Route53ListResourceRecordSetsResponse(BaseModel):
    ResourceRecordSets: list[Route53ResourceRecordSet] | None = None
    IsTruncated: StrictBool | None = None
    NextRecordName: StrictStr | None = None
    NextRecordType: Route53RRType | None = None
    NextRecordIdentifier: StrictStr | None = None
    MaxItems: StrictStr | None = None
