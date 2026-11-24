from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_domain_conflict import CloudFrontDomainConflict


class CloudFrontListDomainConflictsResponse(BaseModel):
    DomainConflicts: list[CloudFrontDomainConflict] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
