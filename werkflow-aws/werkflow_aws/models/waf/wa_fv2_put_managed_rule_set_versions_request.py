from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_version_to_publish import WAFv2VersionToPublish


class WAFv2PutManagedRuleSetVersionsRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    LockToken: StrictStr
    RecommendedVersion: StrictStr | None = None
    VersionsToPublish: dict[StrictStr, WAFv2VersionToPublish] | None = None
