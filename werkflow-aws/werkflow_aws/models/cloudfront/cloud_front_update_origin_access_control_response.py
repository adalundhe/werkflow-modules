from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_control import CloudFrontOriginAccessControl


class CloudFrontUpdateOriginAccessControlResponse(BaseModel):
    OriginAccessControl: CloudFrontOriginAccessControl | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
