from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_tags import CloudFrontTags
from .cloud_front_viewer_fallback import CloudFrontViewerFallback


class CloudFrontCreateConnectionGroupRequest(BaseModel):
    Name: StrictStr
    Ipv6Enabled: StrictBool | None = None
    Tags: CloudFrontTags | None = None
    AnycastIpListId: StrictStr | None = None
    Enabled: StrictBool | None = None
    ViewerFallback: CloudFrontViewerFallback | None = None
