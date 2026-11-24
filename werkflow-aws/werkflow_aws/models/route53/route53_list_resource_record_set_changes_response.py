from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_change import Route53ResourceRecordSetChange


class Route53ListResourceRecordSetChangesResponse(BaseModel):
    ResourceRecordSetChanges: list[Route53ResourceRecordSetChange] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
