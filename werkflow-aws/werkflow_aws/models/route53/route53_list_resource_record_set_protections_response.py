from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_protection import Route53ResourceRecordSetProtection


class Route53ListResourceRecordSetProtectionsResponse(BaseModel):
    ResourceRecordSetProtections: list[Route53ResourceRecordSetProtection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
