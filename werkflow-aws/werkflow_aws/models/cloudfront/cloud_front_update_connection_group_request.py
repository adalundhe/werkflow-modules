from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_viewer_fallback import CloudFrontViewerFallback


class CloudFrontUpdateConnectionGroupRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
    Ipv6Enabled: StrictBool | None = None
    AnycastIpListId: StrictStr | None = None
    Enabled: StrictBool | None = None
    ViewerFallback: CloudFrontViewerFallback | None = None
