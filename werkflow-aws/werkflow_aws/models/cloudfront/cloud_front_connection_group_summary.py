from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_viewer_fallback import CloudFrontViewerFallback


class CloudFrontConnectionGroupSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    RoutingEndpoint: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ETag: StrictStr | None = None
    AnycastIpListId: StrictStr | None = None
    Enabled: StrictBool | None = None
    Status: StrictStr | None = None
    IsDefault: StrictBool | None = None
    ViewerFallback: CloudFrontViewerFallback | None = None
